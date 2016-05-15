# -*- coding: utf-8 -*-
"""
    Project            : nuke.irrigator
    File name          : moisture.py @ UTF-8
    Version            : 0.0.1
    Author             : Gabor Wnuk <gabor.wnuk@me.com>

    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
"""

__author__ = 'Gabor Wnuk'
__date__ = '$Date: 2016-05-08 11:30:44 +0200 (Sun, 8 May 2016) $'


from datetime import datetime
from nuke.irrigator import db
from nuke.irrigator import gpio
from nuke.irrigator import settings

import time


def measure():
    # Send TRIG signal
    gpio.setup([settings.ULTRASONIC_SENSOR_TRIG_GPIO],
                 direction=gpio.GPIO.OUT,
                 initial_value=gpio.GPIO.LOW)
    time.sleep(0.2)

    gpio.GPIO.output(settings.ULTRASONIC_SENSOR_TRIG_GPIO, gpio.GPIO.HIGH)
    time.sleep(0.00001)
    gpio.GPIO.output(settings.ULTRASONIC_SENSOR_TRIG_GPIO, gpio.GPIO.LOW)

    # Measure echo timedelta
    echo_start = None
    echo_end = None

    gpio.GPIO.setup(settings.ULTRASONIC_SENSOR_ECHO_GPIO, gpio.GPIO.IN)
    while gpio.GPIO.input(settings.ULTRASONIC_SENSOR_ECHO_GPIO) == 0:
        echo_start = time.time()

    while gpio.GPIO.input(settings.ULTRASONIC_SENSOR_ECHO_GPIO) == 1:
        echo_end = time.time()

    echo_timedelta = echo_end - echo_start

    # Cleanup gpio's
    gpio.cleanup([settings.ULTRASONIC_SENSOR_TRIG_GPIO,
                  settings.ULTRASONIC_SENSOR_ECHO_GPIO])

    """Distance = speed * time / 2

    Time - echo to - and - from, that's why we divide by 2.

    Speed of sound at sea level = 343 m/s or 34300 cm / s, thus
    distance = 17150 * time (unit cm).
    """
    distance = echo_timedelta * 17150

    if 2 < distance < 400:
        distance += settings.CALIBRATION_DIFFERENCE
        water_per_cm = settings.WATER_TANK_CAPACITY / \
                               (settings.DISTANCE_FROM_SENSOR_WHEN_EMPTY -
                                settings.DISTANCE_FROM_SENSOR_WHEN_FULL)

        water_height = settings.DISTANCE_FROM_SENSOR_WHEN_EMPTY - distance

        if water_height < 0:
            water_height = 0

        return water_height * water_per_cm

    else:
        return None


def save(level=0, date_time=datetime.now()):
    if level > 100:
        level = 100
    elif level < 0:
        level = 0

    db.insert('water_supply', fields=('date_time', 'level'),
                              values=(date_time, level))


def get_current_supply():
    """
    Returns current water supply (previously saved in "percent" value).

    :return: Percent value (0-100) of water supply. Default: 0.
    """
    results = db.query('SELECT * FROM water_supply ORDER BY date_time DESC LIMIT 1',
                       one=True)

    if results:
        return results["level"]

    return 0
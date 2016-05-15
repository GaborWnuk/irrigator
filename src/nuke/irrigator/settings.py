# -*- coding: utf-8 -*-
"""
    Project            : nuke.irrigator
    File name          : settings.py @ UTF-8
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
__date__ = '$Date: 2016-05-07 18:47:03 +0200 (Sat, 7 May 2016) $'

import sqlite3

SQLITE_PATH = '/Users/GaborWnuk/irrigator.db'

"""Geolocation (for weather
"""
LATITUDE_AND_LONGITUDE = (52.227578, 20.986796)

"""Water pump
"""
WATER_PUMP_RELAY_GPIO = 4
WATER_PUMP_LITER_PER_MINUTE = 3.4

"""Ultrasonic sensor (Water level)
"""
ULTRASONIC_SENSOR_TRIG_GPIO = 20
ULTRASONIC_SENSOR_ECHO_GPIO = 21

# Tank capacity in liters
WATER_TANK_CAPACITY = 60

# Distance between sensor and water when tank is full (cm)
DISTANCE_FROM_SENSOR_WHEN_FULL = 5

# Distance between sensor and bottom of the tank when tank is empty (cm)
DISTANCE_FROM_SENSOR_WHEN_EMPTY = 61

# Calibration difference
CALIBRATION_DIFFERENCE = -2.3

# Water level warning (in liters)
WATER_LEVEL_WARNING = 10

# Water level error (in liters), pump won't start below this level
# as some pumps shouldn't work dry
WATER_LEVEL_ERROR = 5


""" SQLite database helpers
"""
def dict_factory(cursor, row):
    dictionary = {}
    for idx, column in enumerate(cursor.description):
        dictionary[column[0]] = row[idx]
    return dictionary


def get_db():
    db = sqlite3.connect(SQLITE_PATH)
    db.row_factory = dict_factory

    return db

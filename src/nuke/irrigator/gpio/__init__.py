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
__date__ = '$Date: 2016-05-08 13:31:22 +0200 (Sun, 8 May 2016) $'

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def setup(gpios=[], direction=GPIO.OUT, initial_value=GPIO.LOW):
    GPIO.setmode(GPIO.BCM)
    for gpio in gpios:
        GPIO.setup(gpio, direction, initial=initial_value)


def cleanup(gpios=[]):
    GPIO.cleanup(gpios)
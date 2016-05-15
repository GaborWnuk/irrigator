# -*- coding: utf-8 -*-
"""
    Project            : nuke.irrigator
    File name          : __init__.py @ UTF-8
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
__date__ = '$Date: 2016-05-14 20:16:44 +0200 (Sat, 14 May 2016) $'

from datetime import datetime
import requests
import sys
from nuke.irrigator import db
from nuke.irrigator import settings

ICON_MAP = {'1d': "clear-day", '1n': 'clear-night', '2d': 'partly-cloudy-day',
            '2n': 'partly-cloudy-night', '3d': 'cloudy', '3n': 'cloudy',
            '4': 'cloudy', '5d': 'rain', '5n': 'rain', '6': 'rain',
            '7': 'rain', '8': 'rain', '9': 'rain',
            '10': 'sleet', '11d': 'snow', '11n': 'snow', '12': 'snow',
            '13': 'fog'}


def update():
    geolocation_data = 'http://pogoda.wp.pl/city.json?lat=%s&lon=%s' % (settings.LATITUDE_AND_LONGITUDE[0],
                                                                       settings.LATITUDE_AND_LONGITUDE[1])

    city_id = requests.get(geolocation_data).json()['cityid']


    weather_data = requests.get('https://api.o2.pl/weather/api/o2/weather?cid=%s&days=4' % city_id).json()

    city_name = weather_data['cityName']

    for day in weather_data['days']:
        date_time = datetime.fromtimestamp(day['date'])

        highest_temp = -sys.maxint
        icon = ""
        precipitation = 0

        for hour in day['timeOfDay']:
            if hour['temperature'] > highest_temp:
                highest_temp = hour['temperature']
                icon = ICON_MAP[hour['icon']]
                precipitation = hour['precipitation']


        db.insert('weather', fields=('city_name', 'date_time', 'temperature', 'icon', 'precipitation'),
                    values=(city_name, date_time, highest_temp, icon, precipitation))

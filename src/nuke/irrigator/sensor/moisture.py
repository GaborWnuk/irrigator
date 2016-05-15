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
__date__ = '$Date: 2016-05-07 19:09:01 +0200 (Sat, 7 May 2016) $'

from datetime import datetime
from datetime import timedelta
import mcp3008
from nuke.irrigator import db

def save(sensor_id, level=0, date_time=datetime.now()):
    if level > 100:
        level = 100
    elif level < 0:
        level = 0

    # Round to the nearest hour
    date_time = date_time - timedelta(minutes=date_time.minute % 60,
                                      seconds=date_time.second,
                                      microseconds=date_time.microsecond)

    db.insert('moisture_level', fields=('sensor_id', 'date_time', 'level'),
                                values=(sensor_id, date_time, level))


def get_last_month_avg():
    results = db.query('SELECT *, AVG(level) AS average FROM moisture_level ' \
                        'GROUP BY date_time ORDER BY date_time DESC LIMIT 720')

    return results



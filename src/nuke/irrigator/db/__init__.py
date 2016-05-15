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
__date__ = '$Date: 2016-05-07 19:35:33 +0200 (Sat, 7 May 2016) $'

from nuke.irrigator import settings


def insert(table, fields=(), values=(), db=settings.get_db()):
    cursor = db.cursor()
    query = 'INSERT OR REPLACE INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    cursor.execute(query, values)
    db.commit()

    row_id = cursor.lastrowid
    cursor.close()

    return row_id


def query(query, args=(), one=False, db=settings.get_db()):
    cursor = db.execute(query, args)
    results = cursor.fetchall()
    cursor.close()
    return (results[0] if results else None) if one else results
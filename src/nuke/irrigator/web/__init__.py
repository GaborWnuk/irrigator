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
__date__ = '$Date: 2016-05-14 16:07:10 +0200 (Sat, 14 May 2016) $'

import urllib
import os
import sqlite3
from nuke.irrigator import settings

WEB_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)))
DB_SCHEMA = os.path.join(os.path.dirname(os.path.abspath(__file__))) + '/../../../../irrigator.sql'

DEPENDENCIES = {'https://cdnjs.cloudflare.com/ajax/libs/react/15.0.2/react.js': '%s/static/js/react.js' % WEB_DIRECTORY,
                'https://cdnjs.cloudflare.com/ajax/libs/react/15.0.2/react-dom.js': '%s/static/js/react.dom.js' % WEB_DIRECTORY,
                'https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.23/browser.min.js': '%s/static/js/babel.js' % WEB_DIRECTORY,
                'https://use.fontawesome.com/588e87d716.js': '%s/static/js/fontawesome.js' % WEB_DIRECTORY,
                'https://code.jquery.com/jquery-2.2.3.min.js': '%s/static/js/jquery.js' % WEB_DIRECTORY,
                'http://omnipotent.net/jquery.sparkline/2.1.2/jquery.sparkline.min.js': '%s/static/js/jquery.sparkline.js' % WEB_DIRECTORY,
                'https://raw.githubusercontent.com/flot/flot/master/jquery.flot.js': '%s/static/js/jquery.flot.js' % WEB_DIRECTORY,
                'https://raw.githubusercontent.com/MichaelZinsmaier/CurvedLines/master/curvedLines.js': '%s/static/js/jquery.flot.curvedlines.js' % WEB_DIRECTORY,
                'https://raw.githubusercontent.com/chartjs/Chart.js/master/dist/Chart.min.js': '%s/static/js/chart.js' % WEB_DIRECTORY,
                'https://cdn.socket.io/socket.io-1.4.5.js': '%s/static/js/socket.io.js' % WEB_DIRECTORY,
                'https://raw.githubusercontent.com/darkskyapp/skycons/master/skycons.js': '%s/static/js/skycons.js' % WEB_DIRECTORY,

                'http://bernii.github.io/gauge.js/dist/gauge.min.js': '%s/static/js/gauge.js' % WEB_DIRECTORY,
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css': '%s/static/css/bootstrap.css' % WEB_DIRECTORY,
                'https://raw.githubusercontent.com/minddust/bootstrap-progressbar/master/css/bootstrap-progressbar-3.3.4.min.css': '%s/static/css/bootstrap.progressbar.css' % WEB_DIRECTORY}


def printf(text):
    print '[    >>   ] %s' % text


def _download_file(source, destination):
    printf('Downloading %s to %s ...' % (source, destination))
    urllib.urlretrieve(source, destination)


def recreate_db_schema():
    printf('Recreating SQLite database schema at %s ...' % settings.SQLITE_PATH)

    try:
        os.remove(settings.SQLITE_PATH)
    except OSError:
        pass

    connection = sqlite3.connect(settings.SQLITE_PATH)
    with open(DB_SCHEMA, 'rt') as schema_file:
        schema = schema_file.read()
        connection.executescript(schema)

    connection.close()


def build():
    recreate_db_schema()

    for key in DEPENDENCIES.keys():
        _download_file(key, DEPENDENCIES[key])
    pass
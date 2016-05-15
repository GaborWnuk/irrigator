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
__date__ = '$Date: 2016-05-07 18:48:11 +0200 (Sat, 7 May 2016) $'

import click
from flask import Flask
from flask import g
from flask import render_template
from flask import Response
import json
from nuke.irrigator import db
from nuke.irrigator import settings
from nuke.irrigator import weather
from nuke.irrigator import web
from os import path

"""Flask web application.
"""
template_folder = path.join(path.dirname(path.abspath(__file__)), 'web/templates')
static_folder = path.join(path.dirname(path.abspath(__file__)), 'web/static')

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

def app_get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = settings.get_db()
    return db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/weather')
def api_weather():
    weather_results = db.query('SELECT * FROM weather WHERE date_time >= date(\'now\', \'start of day\') ORDER BY date_time ASC LIMIT 5',
                               db=app_get_db())

    return Response(response=json.dumps(weather_results), status=200,
                    mimetype="application/json")


@app.route('/api/plants')
def api_plants():
    plants_results = [{'plant_name': 'Pomidory',
                        'count': 11,
                        'color': '#BDC3C7'},
                      {'plant_name': 'Poziomka',
                        'count': 7,
                        'color': '#9B59B6'},
                      {'plant_name': 'Truskawka',
                        'count': 4,
                        'color': '#E74C3C'},
                      {'plant_name': 'Papryka',
                        'count': 4,
                        'color': '#26B99A'},
                      {'plant_name': 'Bazylia',
                        'count': 2,
                        'color': '#3498DB'}]

    return Response(response=json.dumps(plants_results), status=200,
                    mimetype="application/json")


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


"""Option groups, run parameters and so on.
"""
@click.group()
def greet():
    pass


@greet.command()
@click.option('--host', default='0.0.0.0',
                help='The hostname to listen on. Default: 0.0.0.0.')
@click.option('--port', default=5000,
                help='The port of the webserver. Defaults: 5000.')
@click.option('--debug', is_flag=True, help='If given, enables debug mode.')
def runserver(host, port, debug):
    app.run(host=host, port=port, debug=debug)


@greet.command()
def weatherservice():
    weather.update()


@greet.command()
def build():
    web.build()


def main():
    greet()


if __name__ == '__main__':
    main()

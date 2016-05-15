import React from 'react'

import { SinglePanel } from '../single-panel'
import { SkyconsIcon } from '../skycons'

export class WeatherDay extends React.Component {
    render() {
        const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        /*
        Date parsing is completely different between Safari and Chrome :)
        I love JavaScript.
         */
        var splitted_date = this.props.date_time.split(/[^0-9]/);
        var date = new Date (splitted_date[0], splitted_date[1]-1, splitted_date[2],
                             splitted_date[3], splitted_date[4], splitted_date[5]);

        return (<div className="col-sm-2">
                    <div className="daily-weather">
                      <h2 className="day">{days[date.getDay()]}</h2>
                      <h3 className="degrees">{this.props.temperature}</h3>
                      <SkyconsIcon height="32" width="32" icon={this.props.icon}></SkyconsIcon>
                      <h5>{this.props.precipitation}%</h5>
                    </div>
                  </div>)
    }
}

export class Weather extends React.Component {
    getInitialState() {
        return { weather: [] };
    }

    componentDidMount() {
        $.ajax({
            url: 'api/weather',
            dataType: 'json',
            cache: false,
            success: function(weather) {
                this.setState({"weather": weather})
            }.bind(this),
            error: function(xhr, status, err) {
                console.error('/api/weather', status, err.toString());
            }.bind(this)
        });
    }

    render() {
        var weather = this.state.weather;
        var date = new Date();
        const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        var formatted_date = ('0' + date.getHours()).slice(-2) + ":" + ('0' + date.getMinutes()).slice(-2)
        if (weather.length > 0) {
            return (
                    <SinglePanel title="Weather">
                        <div className="row">
                          <div className="col-sm-12">
                            <div className="temperature"><b>{days[date.getDay()]}</b>, {formatted_date}
                            </div>
                          </div>
                        </div>
                        <div className="row">
                          <div className="col-sm-4">
                            <div className="weather-icon">
                              <span><SkyconsIcon height="84" width="84" icon={ weather[0].icon }></SkyconsIcon></span>
                            </div>
                          </div>
                          <div className="col-sm-8">
                            <div className="weather-text">
                              <h2>{ weather[0].city_name }<p><i>Częściowe zachmurzenie</i></p></h2>
                            </div>
                          </div>
                        </div>
                        <div className="col-sm-12">
                          <div className="weather-text pull-right">
                            <h3 className="degrees">{ weather[0].temperature }</h3>
                          </div>
                        </div>
                        <div className="clearfix"></div>


                        <div className="row weather-days">
                            {this.state.weather.map(function(weather_day) {
                                return <WeatherDay key={ weather_day.date_time } date_time={ weather_day.date_time } temperature={ weather_day.temperature } icon={ weather_day.icon } precipitation={ weather_day.precipitation }></WeatherDay>;
                            })}
                          <div className="clearfix"></div>
                        </div>
                    </SinglePanel>
                )
        }
        else {
            return ( <div className="col-md-4 col-sm-6 col-xs-12"></div> )
        }
    }
}

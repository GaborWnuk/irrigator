var SinglePanel = React.createClass({
    render: function() {
        return (<div className="col-md-4 col-sm-6 col-xs-12">
                    <div className="x_panel">
                      <div className="x_title">
                        <h2>{ this.props.title }</h2>
                        <div className="clearfix"></div>
                      </div>
                      <div className="x_content">
                        { this.props.children }
                      </div>
                    </div>
                  </div>)
    }
})

/*
    Weather
 */
var SkyconsIcon = React.createClass({
    getInitialState() {
        return {
            random_id: Math.random().toString(36).substring(7),
            skycons: new Skycons({'color': '#73879C'})
        };
    },
    componentDidMount: function() {
        this.state.skycons.add(document.getElementById(this.state.random_id), this.props.icon);
        this.state.skycons.play()
    },

    render: function() {
        return ( <canvas height={this.props.width} width={this.props.height} className={this.props.icon} id={this.state.random_id}></canvas> )
    }
})

var WeatherDay = React.createClass({
    render: function() {
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
});

var Weather = React.createClass({
    getInitialState: function() {
        return {weather: []};
    },
    componentDidMount: function() {
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
    },
    render: function() {
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

});

ReactDOM.render(
  <Weather />,
  document.getElementById('weather')
);

/*
    Plants
 */
var PlantRow = React.createClass({
    render: function () {
        var style = { color: this.props.color }

        return (<tr>
                  <td><p><i className="fa fa-square" style={style}></i>{ this.props.name } </p></td>
                  <td>{ this.props.count }</td>
                 </tr> )
    }
})

var Plants = React.createClass({
    getInitialState: function() {
        return {plants: []};
    },
    componentDidMount: function() {
        $.ajax({
            url: 'api/plants',
            dataType: 'json',
            cache: false,
            success: function(plants) {
                this.setState({"plants": plants})
            }.bind(this),
            error: function(xhr, status, err) {
                console.error('/api/plants', status, err.toString());
            }.bind(this)
        });

    },
    render: function() {
        if (this.state.plants.length > 0)
        {
            var labels = [], data = [], backgroundColor = [];

            this.state.plants.forEach( plant => {
                labels.push(plant.plant_name);
                data.push(plant.count);
                backgroundColor.push(plant.color);
            });

            this.state.chart = new Chart(document.getElementById("plants_chart"), {
                                  type: 'doughnut',
                                  tooltipFillColor: "rgba(51, 51, 51, 0.55)",
                                  data: {
                                    labels: labels,
                                    datasets: [{
                                      data: data,
                                      backgroundColor: backgroundColor,
                                    }]
                                  },
                                  options: {
                                    legend: false,
                                    responsive: false
                                  }
                                })
        }

        return (
                 <SinglePanel title="Plants">
                    <table className="plants">
                      <tbody>
                        <tr>
                          <th className="top5">
                            <p>Top 5</p>
                          </th>
                          <th>
                            <div className="col-lg-7 col-md-7 col-sm-7 col-xs-7">
                              <p className="">Name</p>
                            </div>
                            <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 right">
                              <p className="">Count</p>
                            </div>
                          </th>
                        </tr>
                        <tr>
                          <td>
                            <canvas id="plants_chart" height="140" width="140"></canvas>
                          </td>
                          <td>
                            <table className="tile_info">
                                <tbody>
                                { this.state.plants.map(function(plant) {
                                    return <PlantRow key={ plant.plant_name } name={ plant.plant_name } color={ plant.color } count={ plant.count }/>
                                })}
                              </tbody>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                </SinglePanel>
            )
    }

});

ReactDOM.render(
  <Plants />,
  document.getElementById('plants')
);

/*
    Moisture
 */
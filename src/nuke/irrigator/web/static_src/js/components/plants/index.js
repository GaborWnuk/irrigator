import React from 'react'

import { SinglePanel } from '../single-panel'
import { Chart } from '../../vendors/chart.js'

export class PlantRow extends React.Component {
    render() {
        var style = { color: this.props.color }

        return (<tr>
                  <td><p><i className="fa fa-square" style={style}></i>{ this.props.name } </p></td>
                  <td>{ this.props.count }</td>
                 </tr> )
    }
}

export class Plants extends React.Component {
    getInitialState() {
        return { plants: [] };
    }

    componentDidMount() {
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
    }

    render() {
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

        return (<SinglePanel title="Plants">
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
}

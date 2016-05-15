import React from 'react'

export class SinglePanel extends React.Component {
    render() {
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
                </div>
        )
    }
}



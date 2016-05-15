var Panel = React.createClass({
    render: function() {
        return (<div className="col-md-4 col-sm-6 col-xs-12">
                    <div className="x_panel">
                      <div className="x_title">
                        <h2>{ this.props.title } <small>Source: pogoda.wp.pl</small></h2>
                        <div className="clearfix"></div>
                      </div>
                      <div className="x_content">
                        { this.children }
                      </div>
                    </div>
                  </div>)
    }
})


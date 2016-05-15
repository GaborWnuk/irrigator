import React from 'react'

import { Skycons } from '../../vendors/skycons.js'

export default class SkyconsIcon extends React.Component {
    getInitialState() {
        return {
            random_id: Math.random().toString(36).substring(7),
            skycons: new Skycons({'color': '#73879C'})
        };
    }

    componentDidMount() {
        this.state.skycons.add(document.getElementById(this.state.random_id), this.props.icon);
        this.state.skycons.play()
    }

    render() {
        return (<canvas height={this.props.width}
                    width={this.props.height}
                    className={this.props.icon}
                    id={this.state.random_id}>
                </canvas> )
    }
}


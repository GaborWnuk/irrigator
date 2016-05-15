import React from 'react'
import ReactDOM from 'react-dom'

require('expose?$!expose?jQuery!./vendors/jquery.js');
require("expose?$!./vendors/jquery.flot.js");

import bootstrap from '../css/vendors/bootstrap.css'
import styles from '../css/s.css'

import { SinglePanel } from './components/single-panel'
console.log(SinglePanel)

/*
import { Weather } from './components/weather'
console.log(Weather)
import { Plants } from './components/plants'
console.log(Plants);

React.render(
  <Weather />,
  document.getElementById('weather')
);

React.render(
  <Plants />,
  document.getElementById('plants')
);
*/

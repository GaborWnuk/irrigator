import React from 'react'
import ReactDOM from 'react-dom'

require('expose?$!expose?jQuery!./vendors/jquery.js');
require("expose?$!./vendors/jquery.flot.js");

import bootstrap from '../css/vendors/bootstrap.css'
import styles from '../css/s.css'

import { Weather } from './components/weather'
import { Plants } from './components/plants'

console.log(Weather);

React.render(
  <Weather />,
  document.getElementById('weather')
);

React.render(
  <Plants />,
  document.getElementById('plants')
);

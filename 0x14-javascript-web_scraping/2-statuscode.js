#!/usr/bin/node
/** File:  2-statuscode.js
*   Author: Christabell Wamalwa */

const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});

#!/usr/bin/node
/** File:  1-writeme.js
*   Author: Christabell Wamalwa*/

const process = require('process');
const filesystem = require('fs');

const file = process.argv[2];
const text = process.argv[3];

filesystem.writeFile(file, text, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  }
});

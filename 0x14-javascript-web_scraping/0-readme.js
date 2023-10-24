#!/usr/bin/node
/** File:  0-readme.js
*   Author: Christabell Wamalwa */

const process = require('process');
const filesystem = require('fs');

const file = process.argv[2];

filesystem.readFile(file, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});

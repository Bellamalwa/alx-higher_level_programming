#!/usr/bin/node
/** File:  1-writeme.js
*   Author: Christabell Wamalwa */

const fs = require('fs');
const path = process.argv[2];
const argms = process.argv[3];

fs.writeFile(path, argms, function (err) {
  if (err) {
    console.log(err);
  }
});

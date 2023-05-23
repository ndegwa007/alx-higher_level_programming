#!/usr/bin/node
// script reads and prints contents of a file
const fs = require('fs');

const file = process.argv[2];
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

#!/usr/bin/node
// scripts writes a string to a file

const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];
fs.writeFile(filename, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});

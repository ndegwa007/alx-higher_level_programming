#!/usr/bin/node
// script gets the content of a webpage and stores in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
	  return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
	  return;
  }

  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});

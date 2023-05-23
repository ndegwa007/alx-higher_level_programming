#!/usr/bin/node
// script that displays the status code of a GET request
const request = require('request');
const req_url = process.argv[2];
request.get(req_url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

#!/usr/bin/node
// script that displays the status code of a GET request
const request = require('request');
const reqUrl = process.argv[2];
request.get(reqUrl, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

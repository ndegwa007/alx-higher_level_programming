#!/usr/bin/node
// request star wars api for each episode name

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});

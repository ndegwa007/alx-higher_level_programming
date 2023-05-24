#!/usr/bin/node
// print number of movies where "Wedge Antilles" is present

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    return;
  }

  let count = 0;
  const obj = JSON.parse(body);
  const results = obj.results;

  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;

    for (let j = 0; j < characters.length; j++) {
      const characterId = characters[j].split('/').slice(-2, -1)[0];
      if (characterId === '18') {
        count++;
        break; // No need to continue checking other characters in the film
      }
    }
  }

  console.log(count);
});

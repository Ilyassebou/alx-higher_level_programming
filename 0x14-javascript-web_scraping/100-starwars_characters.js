#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

function fetchCharacterNames(characterUrls) {
  characterUrls.forEach(url => {
    request.get(url, (error, response, body) => {
      if (error) {
        return console.error(error);
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
}

request.get(filmUrl, (error, response, body) => {
  if (error) {
    return console.error(error);
  }

  const filmData = JSON.parse(body);
  fetchCharacterNames(filmData.characters);
});

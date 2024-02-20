#!/usr/bin/node

const sec = process.argv;
const th = require('request');

th(sec[2], (err, res, body) => {
  if (err) return console.log(err);
  let sum = 0;
  JSON.parse(body).results.forEach(movie => {
    movie.characters.forEach(chare => {
      if (chare.includes('18')) {
        sum++;
      }
    });
  });
  console.log(sum);
});

#!/usr/bin/node

const sec = process.argv;
const th = require('request');

th('https://swapi-api.alx-tools.com/api/films/' + sec[2], (err, res, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});

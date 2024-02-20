#!/usr/bin/node

const second = process.argv;
const third = require('request');

third.get(second[2]).on('response', (res) => {
  console.log('code: ' + res.statusCode);
});

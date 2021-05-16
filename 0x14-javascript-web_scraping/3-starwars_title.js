#!/usr/bin/node
const req = require('request');
let link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(link, function (err, res, b) {
  console.log(err || JSON.parse(b).title);
});

#!/usr/bin/node
const req = require('request');
let link = 'https://swapi-api.hbtn.io/api/films/:id' + process.argv[2];
req(link, function (error, response, b) {
  console.log(error || JSON.parse(b).title);
});

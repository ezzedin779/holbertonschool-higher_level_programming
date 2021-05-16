#!/usr/bin/node
const req = require('request');
req.get(process.argv[2], function (error, res, b) {
  let num = 0;
  if (error) {
    console.log(error);
  }
  const info = JSON.parse(b);
  for (let i = 0; info.results[i] !== undefined; i++) {
    if (info.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      num++;
    }
  }
  console.log(num);
});

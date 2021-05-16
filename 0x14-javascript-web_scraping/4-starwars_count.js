#!/usr/bin/node
const req = require('request');
req.get(process.argv[2], function (err, res, b) {
  if (err) {
	  console.log(err);
  }
  let num = 0;
  const info = JSON.parse(b);
  for (let i = 0; info.results[i] !== undefined; i++) {
    if (info.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      num++;
    }
  }
  console.log(num);
});
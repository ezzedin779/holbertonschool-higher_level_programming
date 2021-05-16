#!/usr/bin/node
const f = require('fs');
const req = require('request');
req.get(process.argv[2]).pipe(f.createWriteStream(process.argv[3]));

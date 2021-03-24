#!/usr/bin/node
if (process.argv.length >= 4) {
  const argument = process.argv.slice(2);
  argument.sort((x, y) => y - x);
  console.log(argument[1]);
} else {
  console.log('0');
}

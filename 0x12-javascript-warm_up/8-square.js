#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size) {
  let i;
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}

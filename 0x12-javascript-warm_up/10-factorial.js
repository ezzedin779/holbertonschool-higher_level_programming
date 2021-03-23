#!/usr/bin/node
function factorial (a) {
  const x = parseInt(a);
  if (x === 0) {
    return 1;
  } else if (x) {
    return a * factorial(x - 1);
  } else {
    return 1;
  }
}
console.log(factorial(process.argv[2]));

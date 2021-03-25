#!/usr/bin/node
exports.logMe = (function (item) {
  let c = -1;
  return function (item) { c += 1; console.log(c + ':' + item); };
})();

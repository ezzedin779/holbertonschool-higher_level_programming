#!/usr/bin/node
exports.moby = function (x, theFunction) {
  let i;
  for (i = 0; i < x; i++) {
    theFunction();
  }
};

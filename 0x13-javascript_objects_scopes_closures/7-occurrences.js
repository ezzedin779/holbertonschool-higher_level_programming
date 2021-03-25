#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let oc = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      oc++;
    }
  }
  return oc;
};

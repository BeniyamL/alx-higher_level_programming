#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (const num of list) {
    if (num === searchElement) {
      n += 1;
    }
  }
  return (n);
};

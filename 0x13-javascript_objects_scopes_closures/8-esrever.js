#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const arr = new Array(len);
  for (let i = 0; list[i]; i++) {
    arr[i] = list[len - 1 - i];
  }
  return (arr);
};

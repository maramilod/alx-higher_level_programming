#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length;
  let arr = new Array(len);;
  for (let i = 0; list[i]; i++) {
    arr[i] = list[len - 1 - i];
  }
  return (arr);
};

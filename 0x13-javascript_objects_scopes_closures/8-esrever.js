#!/usr/bin/node
exports.esrever = function (list) {
  const retList = [];
  let i = 1;
  for (let index = 0; index < list.length; index++) {
    retList[index] = list[list.length - i];
    i++;
  }
  return retList;
};

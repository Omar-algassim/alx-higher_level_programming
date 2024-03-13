#!/usr/bin/node
const array = process.argv;
if (array[2] === undefined || array.length < 4) {
  console.log(0);
} else {
  let max = array[2];
  let secondMax = array[3];
  for (let index = 2; index < array.length; index++) {
    if (max < array[index]) {
      secondMax = max;
      max = array[index];
    } else if (secondMax < array[index] && max > array[index]) {
      secondMax = array[index];
    }
  }
  console.log(secondMax);
}

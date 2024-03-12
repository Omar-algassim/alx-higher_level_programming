#!/usr/bin/node
let i = 0;
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (i < size) {
    let print = '';
    for (let j = 0; j < size; j++) {
      print += 'X';
    }
    console.log(print);
    i++;
  }
}

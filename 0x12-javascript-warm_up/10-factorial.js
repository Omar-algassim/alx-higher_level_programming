#!/usr/bin/node
function factrial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  }
  return (num * factrial(num - 1));
}
const num = parseInt(process.argv[2]);
const result = factrial(num);
console.log(result);

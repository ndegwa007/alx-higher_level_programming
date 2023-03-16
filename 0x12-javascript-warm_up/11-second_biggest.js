#!/usr/bin/node

const x = process.argv.slice(2);

function compare (a, b) {
  return a - b;
}

if (x.length === 0 || x.length === 1) {
  console.log(0);
} else {
  x.sort(compare);
  console.log(x[x.length - 2]);
}

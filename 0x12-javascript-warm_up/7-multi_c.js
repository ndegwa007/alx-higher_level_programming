#!/usr/bin/node

let x = process.argv[2];

if (!x) {
  console.log('Missing number of occurences');
}

while (x > 0) {
  console.log('C is fun');
  x--;
}

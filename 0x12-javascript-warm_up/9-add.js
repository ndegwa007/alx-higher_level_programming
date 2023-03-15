#!/usr/bin/node

const sum = function add(a, b) {

  if (process.argv.length < 4) {
    return NaN;
  }
  const num1 = parseInt(process.argv[2]);
  const num2 = parseInt(process.argv[3]);

  a = num1;
  b = num2;

  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  const s = a + b;
  return s;
}

console.log(sum());

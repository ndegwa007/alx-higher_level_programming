#!/usr/bin/node

const f = function factorial (n) {
  n = parseInt(process.argv[3])
  if (isNaN(n)) {
    return 1
  } else {
    return n * factorial(n - 1)
  }
}

console.log(f())

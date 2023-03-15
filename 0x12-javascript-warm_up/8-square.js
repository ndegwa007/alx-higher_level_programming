#!/usr/bin/node
const ex = 'X'
const x = process.argv[2]
parseInt(x)
if (!parseInt(x)) {
  console.log('Missing size')
}

for (let i = 0; i < x; i++) {
  console.log(ex.repeat(x))
}

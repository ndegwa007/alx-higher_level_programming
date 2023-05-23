#!/usr/bin/node
// script reads and prints contents of a file
import { readFile } from 'node:fs';

const file = process.argv[2];
readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

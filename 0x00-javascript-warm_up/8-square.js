#!/usr/bin/node
const block = 'X';
if (process.argv[2]) {
  const iterations = parseInt(process.argv[2]);
  for (let step = 0; step < iterations; step++) {
    console.log(block.repeat(iterations));
  }
} else {
  console.log('Missing size');
}

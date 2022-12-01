#!/usr/bin/node
const block = 'X';
const iterations = parseInt(process.argv[2]);
for (let step = 0; step < iterations; step++) {
  console.log(block.repeat(iterations));
}

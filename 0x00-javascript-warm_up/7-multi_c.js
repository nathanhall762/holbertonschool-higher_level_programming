#!/usr/bin/node
const message = 'C is fun';

for (let step = 0; step < process.argv[2]; step++) {
  // Runs 5 times, with values of step 0 through 4.
  console.log(message);
}

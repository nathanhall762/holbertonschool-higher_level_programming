#!/usr/bin/node
const message = 'C is fun';

for (let step = 0; step < process.argv[2]; step++) {
  console.log(message);
}

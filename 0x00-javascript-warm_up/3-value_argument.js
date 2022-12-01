#!/usr/bin/node
let argCount = 0;
process.argv.forEach((val, index) => {
  argCount++;
});
if (argCount === 2) {
  console.log('No argument');
} else if (argCount > 2) {
  process.argv.forEach((val, index) => {
    if (index > 1) {
      console.log(val);
    }
  });
}

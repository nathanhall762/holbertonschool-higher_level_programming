#!/usr/bin/node
let argCount = 0;
process.argv.forEach((val, index) => {
  argCount++;
});
const realCount = argCount;
if (argCount < 3) {
  console.log('No argument');
} else if (realCount === 3) {
  console.log('Argument found');
} else if (argCount > 3) {
  console.log('Arguments found');
}

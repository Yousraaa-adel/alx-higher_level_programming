#!/usr/bin/node
const args = process.args;

if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log(parseInt(args[2]));
}

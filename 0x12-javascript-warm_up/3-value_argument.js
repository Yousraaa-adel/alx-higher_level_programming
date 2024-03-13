#!/usr/bin/node
const argsLength = process.argv;

if (argsLength[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argsLength[2]);
}

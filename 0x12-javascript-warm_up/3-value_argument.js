#!/usr/bin/node
const argsLength = process.argv.length;

if (argsLength === 2) {
  console.log('No argument');
} else {
  console.log(argsLength[2]);
}

#!/usr/bin/node
const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

if (isNaN(num1) || isNaN(num2) || !num1 || !num2) {
  console.log('NaN');
}

function add (num1, num2) {
  return num1 + num2;
}

console.log(add(num1, num2));

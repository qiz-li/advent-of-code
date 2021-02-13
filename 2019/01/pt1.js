/*
My first JS program!
Find this puzzle at:
https://adventofcode.com/2019/day/1
*/

const fs = require('fs');

const problemInput = fs.readFileSync('./input.txt').toString().split('\n');
let sum = 0;

problemInput.forEach((line) => {
  sum += Math.floor(line / 3) - 2;
});

console.log(sum);

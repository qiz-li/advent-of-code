/*
My first JS program!
Find this puzzle at:
https://adventofcode.com/2019/day/1
*/

const fs = require("fs");
const problemInput = fs.readFileSync("./input.txt").toString().split("\n");

var sum = 0;

for (var i = 0; i < problemInput.length; i++) {
  sum += Math.floor(problemInput[i] / 3) - 2;
}

console.log(sum);

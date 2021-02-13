/*
Find this puzzle at:
https://adventofcode.com/2019/day/1
*/

const fs = require("fs");
const problemInput = fs.readFileSync("./input.txt").toString().split("\n");

var total_fuel = 0;

for (var i = 0; i < problemInput.length; i++) {
  let fuel = 0;
  let additional = Math.floor(problemInput[i] / 3) - 2;
  // Adding all additional fuels until reaching 0 or negative
  while (additional > 0) {
    fuel += additional;
    additional = Math.floor(additional / 3) - 2;
  }
  total_fuel += fuel;
}

console.log(total_fuel);

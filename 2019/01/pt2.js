/*
Find this puzzle at:
https://adventofcode.com/2019/day/1
*/

const fs = require('fs');

const problemInput = fs.readFileSync('./input.txt').toString().split('\n');
let totalFuel = 0;

problemInput.forEach((line) => {
  let fuel = 0;
  // Adding all additional fuels until reaching 0 or negative
  for (
    let additional = Math.floor(line / 3) - 2;
    additional > 0;
    additional = Math.floor(additional / 3) - 2
  ) {
    fuel += additional;
  }
  totalFuel += fuel;
});

console.log(totalFuel);

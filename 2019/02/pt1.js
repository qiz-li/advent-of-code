/*
Find this puzzle at:
https://adventofcode.com/2019/day/2
*/

const fs = require('fs');

const problemInput = fs
  .readFileSync('./input.txt')
  .toString()
  .split(',')
  .map(Number);

// Return to the "1202 program alarm"
problemInput[1] = 12;
problemInput[2] = 2;

for (let idx = 0; problemInput[idx] !== 99; idx += 4) {
  let sum;
  if (problemInput[idx] === 1) {
    sum = problemInput[problemInput[idx + 1]] + problemInput[problemInput[idx + 2]];
  } else if (problemInput[idx] === 2) {
    sum = problemInput[problemInput[idx + 1]] * problemInput[problemInput[idx + 2]];
  }
  problemInput[problemInput[idx + 3]] = sum;
}
console.log(problemInput[0]);

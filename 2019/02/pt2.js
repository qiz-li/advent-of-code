/*
Find this puzzle at:
https://adventofcode.com/2019/day/2
Reassigning list completely messed me up on this one!
*/

const fs = require('fs');

const problemInput = fs
  .readFileSync('./input.txt')
  .toString()
  .split(',')
  .map(Number);

function runProgram(input, noun, verb) {
  // Program from pt1.js
  const newInput = [...input];
  newInput[1] = noun;
  newInput[2] = verb;
  for (let idx = 0; newInput[idx] !== 99; idx += 4) {
    let sum;
    if (newInput[idx] === 1) {
      sum = newInput[newInput[idx + 1]] + newInput[newInput[idx + 2]];
    } else if (newInput[idx] === 2) {
      sum = newInput[newInput[idx + 1]] * newInput[newInput[idx + 2]];
    }
    newInput[newInput[idx + 3]] = sum;
  }
  return newInput[0];
}

function main() {
  // Likely to be a faster way, but this works...
  for (let noun = 0; noun <= 99; noun += 1) {
    for (let verb = 0; verb <= 99; verb += 1) {
      if (runProgram([...problemInput], noun, verb) === 19690720) {
        return 100 * noun + verb;
      }
    }
  }
  return false;
}

console.log(main());

const fs = require('fs');
const moves = fs.readFileSync('2017/input/day-16.input').toString();

const actions = {
  s: (input, a) => {
    const rest = input.splice(input.length - a);
    input = [...rest, ...input];
    return input;
  },
  x: (input, a, b) => {
    const temp = input[a];
    input[a] = input[b]
    input[b] = temp;
    return input;
  },
  p: (input, a, b) => {
    return actions.x(input, input.indexOf(a), input.indexOf(b));
  }
};

const getInput = () => 'abcdefghijklmnop'.split('');

const performMove = (input, move) => {
  const action = move[0];
  const params = move.substring(1).split('/');
  return actions[action](input, params[0], params[1]);
}
const movesOrder = moves.split(',');
let oneDance = getInput();
movesOrder.forEach(move => 
  oneDance = performMove(oneDance, move));
console.log(`part1: ${oneDance.join('')}`);

let searchInput = getInput();
let cache = {}; // finding the loop
let loopIndex = -1;
for(let i=0; i<1000000000; i++) {
  movesOrder.forEach(move => 
    searchInput = performMove(searchInput, move));
  if (cache[searchInput]) {
    loopIndex = i;
    break;
  } else {
    cache[searchInput] = true;
  }
}

let input = getInput();
const start = Math.floor(1000000000/loopIndex)*loopIndex;
for(let i=start; i<1000000000; i++) {
  movesOrder.forEach(move => 
    input = performMove(input, move));
}
console.log(`part2: ${input.join('')}`);



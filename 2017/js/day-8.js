const fs = require('fs');
const input = fs.readFileSync('2017/input/day-8.input').toString();

const instructions = input.split('\n');
let map = {};
const equalities = {
  '>': (a, b) => a > b,
  '>=': (a, b) => a >= b,
  '<': (a, b) => a < b,
  '<=': (a, b) => a <= b,
  '!=': (a, b) => a != b,
  '==': (a, b) => a == b,
};

const oprs = {
  'inc': (a, v) => a + v,
  'dec': (a, v) => a - v,
};

let max = 0;
instructions.forEach(entry => {
  const parts = entry.split(' ');
  if (equalities[parts[5]](map[parts[4]] || 0, parts[6])) {
    const value = map[parts[0]] || 0;
    max = Math.max(max, value);
    map[parts[0]] = oprs[parts[1]](value, +parts[2]);
  }
});

const result = Math.max(...Object.keys(map).map(key => map[key]));
console.log(result);
console.log(max);

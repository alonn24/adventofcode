const fs = require('fs');
const input = fs.readFileSync('2017/input/day-10.input').toString();

const steps = input.split(',');
let map = {
  'n': ([n, s, e, w]) => ([n + 2, s - 2, e, w]),
  'ne': ([n, s, e, w]) => ([n + 1, s - 1, e + 1, w - 1]),
  'se': ([n, s, e, w]) => ([n - 1, s + 1, e + 1, w - 1]),
  's': ([n, s, e, w]) => ([n - 2, s + 2, e, w]),
  'sw': ([n, s, e, w]) => ([n - 1, s + 1, e - 1, w + 1]),
  'nw': ([n, s, e, w]) => ([n + 1, s - 1, e - 1, w + 1])
};
let pos = [0, 0, 0, 0];

const getDistance = pos => {
  const n = Math.abs(pos[0]);
  const w = Math.abs(pos[2]);
  return w + (n - w) / 2;
};
let max = 0;
steps.forEach(step => {
  pos = map[step](pos);
  max = Math.max(max, getDistance(pos));
});

console.log('part1', getDistance(pos));
console.log('part2', max);


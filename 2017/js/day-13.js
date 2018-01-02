const fs = require('fs');
const input = fs.readFileSync('2017/input/day-13.input').toString();

const map = input.split('\n').reduce((map, e) => {
  const values = e.split(': ');
  map[values[0]] = +values[1];
  return map;
}, {});

const layers = Math.max(...Object.keys(map).map(x => +x));

function isCoughtOnLayer(layer, step) {
  const depth = layer;
  if (layer !== void 0) {
    const devider = depth + depth - 2;
    return step % devider === 0;
  }
  return false;
}

const coughts = [];
for(let step=0; step<=layers; step++) {
  if (isCoughtOnLayer(map[step], step)) {
    coughts.push(step);
  }
}
const sev = coughts.reduce((res, x) => res + x * map[x], 0);
console.log('part1', sev);

function willGetCought(delay) {
  for(let step=0; step<=layers; step++) {
    if (isCoughtOnLayer(map[step], step + delay)) {
      return true;
    }
  }
  return false;
}

let delay = -1;
let pass = false;
while (!pass && delay <= 10000000) {
  delay++;
  pass = !willGetCought(delay);
}
console.log('part2', delay);
let input = '0: 3\n' +
  '1: 2\n' +
  '2: 4\n' +
  '4: 6\n' +
  '6: 5\n' +
  '8: 8\n' +
  '10: 6\n' +
  '12: 4\n' +
  '14: 8\n' +
  '16: 6\n' +
  '18: 8\n' +
  '20: 8\n' +
  '22: 6\n' +
  '24: 8\n' +
  '26: 9\n' +
  '28: 12\n' +
  '30: 8\n' +
  '32: 14\n' +
  '34: 10\n' +
  '36: 12\n' +
  '38: 12\n' +
  '40: 10\n' +
  '42: 12\n' +
  '44: 12\n' +
  '46: 12\n' +
  '48: 12\n' +
  '50: 14\n' +
  '52: 12\n' +
  '54: 14\n' +
  '56: 12\n' +
  '60: 14\n' +
  '62: 12\n' +
  '64: 14\n' +
  '66: 14\n' +
  '68: 14\n' +
  '70: 14\n' +
  '72: 14\n' +
  '74: 14\n' +
  '78: 26\n' +
  '80: 18\n' +
  '82: 17\n' +
  '86: 18\n' +
  '88: 14\n' +
  '96: 18';

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
console.log('part2 delay');
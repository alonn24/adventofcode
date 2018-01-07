let inputA = 289;
let inputB = 629;
let factorA = 16807;
let factorB = 48271;
const bit32 = 2147483647;
const next = (num, fac, crit) => {
  let val = (num*fac) % bit32;
  while(!crit(val)) {
    val = (val*fac) % bit32;
  }
  return val;
};

let nextA = inputA;
let nextB = inputB;
let count = 0;
for(let i=0; i<40000000; i++) {
  nextA = val = (nextA*factorA) % bit32;
  nextB = val = (nextB*factorB) % bit32;
  if ((nextA & 0xffff) === (nextB & 0xffff)) {
    count++;
  }
}
console.log('part1', count);

nextA = inputA;
nextB = inputB;
let total = 0;
for(let i=0; i<5000000; i++) {
  nextA = next(nextA, factorA, res => res % 4 === 0);
  nextB = next(nextB, factorB, res => res % 8 === 0);
  if ((nextA & 0xffff) === (nextB & 0xffff)) {
    total++;
  }
}
console.log('part2', total);


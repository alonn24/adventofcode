let inputA = 289;
let inputB = 629;
let factorA = 16807;
let factorB = 48271;
const bit32 = 2147483647;
const bit16 = 65535;
const next = (num, fac, crit) => {
  let val = (num*fac) % bit32;
  while(!crit(val)) {
    val = (val*fac) % bit32;
  }
  return val;
};

let nextA = inputA;
let nextB = inputB;
let total = 0;
let count = 0;
while(count < 40000000) {
  count++;
  nextA = next(nextA, factorA, res => res % 4 === 0);
  nextB = next(nextB, factorB, res => res % 8 === 0);
  if ((nextA & bit16) === (nextB & bit16)) {
    total++;
  }
}
console.log(total);


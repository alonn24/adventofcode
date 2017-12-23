let input =
  'set b 84\n' +
  'set c b\n' +
  'jnz a 2\n' +
  'jnz 1 5\n' +
  'mul b 100\n' +
  'sub b -100000\n' +
  'set c b\n' +
  'sub c -17000\n' +
  'set f 1\n' +
  'set d 2\n' +
  'set e 2\n' +
  'set g d\n' +
  'mul g e\n' +
  'sub g b\n' +
  'jnz g 2\n' +
  'set f 0\n' +
  'sub e -1\n' +
  'set g e\n' +
  'sub g b\n' +
  'jnz g -8\n' +
  'sub d -1\n' +
  'set g d\n' +
  'sub g b\n' +
  'jnz g -13\n' +
  'jnz f 2\n' +
  'sub h -1\n' +
  'set g b\n' +
  'sub g c\n' +
  'jnz g 2\n' +
  'jnz 1 3\n' +
  'sub b -17\n' +
  'jnz 1 -23' +
  '';

const instructions = input.split('\n').map(entry => {
  const values = entry.split(' ');
  return {
    cmd: values[0],
    reg: values[1],
    val: values[2]
  };
});
let regValues = {};

function setValue(reg, val) {
  const res = parseInt(val);
  if (isNaN(res)) {
    return setValue(reg, regValues[val] || 0);
  } else {
    regValues[reg] = res;
  }
}

function value(val) {
  const res = parseInt(val);
  if (isNaN(res)) {
    return regValues[val] ? value(regValues[val]) : 0;
  } else {
    return res;
  }
}

function execute(entry) {
  switch (entry.cmd) {
    case 'set':
      setValue(entry.reg, entry.val);
      break;
    case 'sub':
      setValue(entry.reg, value(entry.reg) - value(entry.val));
      break;
    case 'mul':
      setValue(entry.reg, value(entry.reg) * value(entry.val));
      break;
  }
}

function run() {
  let i = 0;
  let count = 0;
  while (i < instructions.length) {
    const inst = instructions[i];

    if (inst.cmd === 'jnz' && value(inst.reg) !== 0) {
      i += value(inst.val)
    } else {
      i++;
      execute(inst);
      if (inst.cmd === 'mul') {
        count++;
      }
    }

  }
  console.log(count); 
}

// part 1
run();

// part 2
let a = 1;
let b = 84;
let c = b;
let d = 0;
let e = 0;
let f = 0;
let g = 0;
let h = 0;

// original
if (a) {
  b = (b * 100) + 100000;
  c = b + 17000
}

// do {
//   f = 1;
//   d = 2;
//   do {
//     e = 2;
//     do {
//       g = d * e - b;
//       if (!g) {
//         f = 0
//       }
//       e++;
//       g = e - b
//     } while (g);
//     d++;
//     g = d - b
//   } while (g);
//   if (!f) {
//     h++;
//   }
//   g = b - c;
//   if (g) {
//     b += 17
//   }
// } while (g);

// optimized
function isPrime() {
  let res = true;
  for (let i = 2; i < b; i++) {
    if (b % i === 0) {
      f = 0;
      res = false;
      break;
    }
  }
  return res;
}

do {
  if (!isPrime(b)) h++;
  g = b - c;
  b += 17
} while (g !== 0);

console.log(h);

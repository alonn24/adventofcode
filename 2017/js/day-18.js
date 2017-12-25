let input = 'set i 31\n' +
  'set a 1\n' +
  'mul p 17\n' +
  'jgz p p\n' +
  'mul a 2\n' +
  'add i -1\n' +
  'jgz i -2\n' +
  'add a -1\n' +
  'set i 127\n' +
  'set p 735\n' +
  'mul p 8505\n' +
  'mod p a\n' +
  'mul p 129749\n' +
  'add p 12345\n' +
  'mod p a\n' +
  'set b p\n' +
  'mod b 10000\n' +
  'snd b\n' +
  'add i -1\n' +
  'jgz i -9\n' +
  'jgz a 3\n' +
  'rcv b\n' +
  'jgz b -1\n' +
  'set f 0\n' +
  'set i 126\n' +
  'rcv a\n' +
  'rcv b\n' +
  'set p a\n' +
  'mul p -1\n' +
  'add p b\n' +
  'jgz p 4\n' +
  'snd a\n' +
  'set a b\n' +
  'jgz 1 3\n' +
  'snd b\n' +
  'set f 1\n' +
  'add i -1\n' +
  'jgz i -11\n' +
  'snd a\n' +
  'jgz f -16\n' +
  'jgz a -19';
// input = 'snd 1\n' +
//   'snd 2\n' +
//   'snd p\n' +
//   'rcv a\n' +
//   'rcv b\n' +
//   'rcv c\n' +
//   'rcv d';

const instructions = input.split('\n').map(entry => {
  const values = entry.split(' ');
  return {
    cmd: values[0],
    reg: values[1],
    val: values[2]
  };
});

const firstQ = [];
const secondQ = [];
const prog1 = program(0, firstQ, secondQ);
const prog2 = program(1, secondQ, firstQ);
let count = 0;
while (!prog1.waiting() || !prog2.waiting()) {
  count++;
  if (!prog1.waiting()) {
    prog1.run();
  }
  if (!prog2.waiting()) {
    prog2.run();
  }
}

console.log('done', prog1.waiting(), prog2.waiting(), prog1.send(), prog2.send());

function program(id, myQ, otherQ) {
  let regValues = {p: id};

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
      case 'add':
        setValue(entry.reg, value(entry.reg) + value(entry.val));
        break;
      case 'mul':
        setValue(entry.reg, value(entry.reg) * value(entry.val));
        break;
      case 'mod':
        setValue(entry.reg, value(entry.reg) % value(entry.val));
        break;
    }
  }

  let i = 0;
  let send = 0;
  return {
    waiting: () => instructions[i].cmd === 'rcv' && otherQ.length === 0,
    send: () => send,
    run: function () {
      if (instructions[i].cmd === 'snd') {
        console.log(id, i, instructions[i], value(instructions[i].reg));
        myQ.unshift(value(instructions[i].reg));
        send++;
        i++;
      } else if (instructions[i].cmd === 'rcv' && otherQ.length > 0) {
        console.log(id, i, instructions[i], value(instructions[i].reg));
        let val = otherQ.pop();
        setValue(instructions[i].reg, val);
        i++;
      }
      else if (instructions[i].cmd === 'jgz') {
        if (value(instructions[i].reg) > 0) {
          i += value(instructions[i].val);
        } else {
          i++;
        }
      } else {
        execute(instructions[i]);
        i++;
      }
    }
  }
}

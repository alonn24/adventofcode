let times = 12368930;
let input = 'In state A:\n' +
  '  If the current value is 0:\n' +
  '    - Write the value 1.\n' +
  '    - Move one slot to the right.\n' +
  '    - Continue with state B.\n' +
  '  If the current value is 1:\n' +
  '    - Write the value 0.\n' +
  '    - Move one slot to the right.\n' +
  '    - Continue with state C.\n' +
  '\n' +
  'In state B:\n' +
  '  If the current value is 0:\n' +
  '    - Write the value 0.\n' +
  '    - Move one slot to the left.\n' +
  '    - Continue with state A.\n' +
  '  If the current value is 1:\n' +
  '    - Write the value 0.\n' +
  '    - Move one slot to the right.\n' +
  '    - Continue with state D.\n' +
  '\n' +
  'In state C:\n' +
  '  If the current value is 0:\n' +
  '    - Write the value 1.\n' +
  '    - Move one slot to the right.\n' +
  '    - Continue with state D.\n' +
  '  If the current value is 1:\n' +
  '    - Write the value 1.\n' +
  '    - Move one slot to the right.\n' +
  '    - Continue with state A.\n' +
  '\n' +
  'In state D:\n' +
  '  If the current value is 0:\n' +
  '    - Write the value 1.\n' +
  '    - Move one slot to the left.\n' +
  '    - Continue with state E.\n' +
  '  If the current value is 1:\n' +
  '    - Write the value 0.\n' +
  '    - Move one slot to the left.\n' +
  '    - Continue with state D.\n' +
  '\n' +
  'In state E:\n' +
  '  If the current value is 0:\n' +
  '    - Write the value 1.\n' +
  '    - Move one slot to the right.\n' +
  '    - Continue with state F.\n' +
  '  If the current value is 1:\n' +
  '    - Write the value 1.\n' +
  '    - Move one slot to the left.\n' +
  '    - Continue with state B.\n' +
  '\n' +
  'In state F:\n' +
  '  If the current value is 0:\n' +
  '    - Write the value 1.\n' +
  '    - Move one slot to the right.\n' +
  '    - Continue with state A.\n' +
  '  If the current value is 1:\n' +
  '    - Write the value 1.\n' +
  '    - Move one slot to the right.\n' +
  '    - Continue with state E.';

// times = 6;
// input = 'In state A:\n' +
//   '  If the current value is 0:\n' +
//   '    - Write the value 1.\n' +
//   '    - Move one slot to the right.\n' +
//   '    - Continue with state B.\n' +
//   '  If the current value is 1:\n' +
//   '    - Write the value 0.\n' +
//   '    - Move one slot to the left.\n' +
//   '    - Continue with state B.\n' +
//   '\n' +
//   'In state B:\n' +
//   '  If the current value is 0:\n' +
//   '    - Write the value 1.\n' +
//   '    - Move one slot to the left.\n' +
//   '    - Continue with state A.\n' +
//   '  If the current value is 1:\n' +
//   '    - Write the value 1.\n' +
//   '    - Move one slot to the right.\n' +
//   '    - Continue with state A.';
let conf = {};
input
  .split('\n\n').forEach(bulk => {
  const rows = bulk.split('\n');
  const state = rows[0].match(/([A-F]):$/)[1];
  conf[state] = conf[state] || {};
  let i = 1;
  while (i < rows.length) {
    const val = rows[i].match(/([0,1]):$/)[1]
    conf[state][val] = {
      write: +rows[i + 1].match(/([0,1]).$/)[1],
      move: rows[i + 2].match(/the\s(.*)\.$/)[1] === 'right'? 1 : -1,
      con: rows[i + 3].match(/([A-F]).$/)[1]
    }
    i += 4;
  }

});
let state = 'A';
let tape = {};
let loc = 0;
for(let i=0; i<times; i++) {
  const val = tape[loc] || 0;
  tape[loc] = conf[state][val].write
  loc += conf[state][val].move
  state = conf[state][val].con
}
console.log(Object.keys(tape).filter(key => tape[key] === 1).length);

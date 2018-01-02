const fs = require('fs');
const input = fs.readFileSync('2017/input/day-9.input').toString();

let count = 0;
let ignore = false;
let garbage = false;
let num = 0;
const result = input.split('').reduce((res, c) => {
  if (ignore) {
    ignore = false;
  } else if (garbage) {

    ignore = c === '!';
    garbage = !(c === '>');
    num = (!ignore && garbage)? num+1 : num;
  } else {
    switch (c) {
      case '{':
        count++;
        break;
      case '}':
        res += count;
        count--;
        break;
      case '<':
        garbage = true;
        break;
      case '!':
        ignore = true;
        break;
    }
  }
  return res;
}, 0);

console.log(result);
console.log(num);

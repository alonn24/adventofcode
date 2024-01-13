const fs = require("fs");
const input = fs.readFileSync("2022/input/day-10.input.txt").toString();

const instructions = input
  .split("\n")
  .map((x) => [x.split(" ")[0], Number(x.split(" ")[1])]);

let x = 1;
const values = instructions.flatMap(([inst, n]) => {
  if (inst === "noop") {
    return [x];
  }

  let temp = x;
  x = temp + n;
  return [temp, temp];
});
const result = [20, 60, 100, 140, 180, 220].reduce(
  (res, x) => res + x * values[x - 1],
  0
);
console.log(result);

// Now we can just loop over the cycles
const drawing = Array.from({ length: 6 }).map(() => Array.from({ length: 40 }));
let i = 0;
let j = 0;
values.forEach((value) => {
	console.log(value)
	const intersect = [value - 1, value, value + 1].includes(j);
  drawing[i][j] = intersect ? "#" : ".";
  if (j === 39) {
    i++;
    j=0;
  } else {
    j++;
  }
});
console.log(drawing.map(x => x.join('')));
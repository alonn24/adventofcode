const fs = require("fs");
const input = fs.readFileSync("2022/input/day-6.input.txt").toString();

const characters = input.split("");

for (let i = 3; i < characters.length; i++) {
  const group = characters.slice(i - 3, i + 1);
  const duplicate = group.find((x, i) => group.indexOf(x) !== i);
  if (!duplicate) {
    console.log(i + 1); // zero based indices
    break;
  }
}

for (let i = 13; i < characters.length; i++) {
  const group = characters.slice(i - 13, i + 1);
  const duplicate = group.find((x, i) => group.indexOf(x) !== i);
  if (!duplicate) {
    console.log(i + 1); // zero based indices
    break;
  }
}
const fs = require("fs");
const input = fs.readFileSync("2022/input/day-13.input.txt").toString();

const lists = input
  .split("\n\n")
  .map((x) => x.split("\n").map((x) => JSON.parse(x)));
const results = lists.map(([left, right]) => checkList(left, right));
const sumTruesIndices = results.reduce((res, x, i) => {
  return x ? res + i + 1 : res;
}, 0);
console.log(sumTruesIndices);

const dividerPackages = [[[2]], [[6]]];

const allPackages = lists.flatMap((x) => x).concat(dividerPackages);
const sorted = allPackages.sort((a, b) => (checkList(a, b) ? -1 : 1));
const dividerPackagesIndices = dividerPackages.map((dp) =>
  sorted.findIndex((x) => JSON.stringify(x) === JSON.stringify(dp))
);
console.log((dividerPackagesIndices[0] + 1) * (dividerPackagesIndices[1] + 1));

function checkList(left, right) {
  let decision;
  const smallerLength = Math.min(left.length, right.length);
  for (let i = 0; i < smallerLength; i++) {
    const leftValue = left[i];
    const rightValue = right[i];
    if (!Array.isArray(leftValue) && !Array.isArray(rightValue)) {
      if (leftValue < rightValue) return true; // left is lower
      if (leftValue > rightValue) return false; // right is lower
    } else {
      decision = checkList(toArray(leftValue), toArray(rightValue));
      if (decision === true || decision === false) {
        return decision;
      }
    }
  }
  if (left.length < right.length) {
    return true;
  } else if (left.length > right.length) {
    return false;
  }
  return decision;
}

function toArray(value) {
  return Array.isArray(value) ? value : [value];
}

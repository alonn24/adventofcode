const fs = require("fs");
const input = fs.readFileSync("2022/input/day-15.input.txt").toString();
const sensors = input.split("\n").map((x) => x.match(/[-0-9]+/g).map(Number));

function getTargetIndices(targetY) {
  const indicesSet = new Set();
  sensors.forEach(([x, y, bx, by]) => {
    const yDisToB = Math.abs(y - by);
    const yDisToT = Math.abs(y - targetY);
    const xDisToB = Math.abs(x - bx);

    // Current row size
    const rowSize = xDisToB * 2 + 1 + yDisToB * 2;

		// Target row size
    const tRowSize = rowSize - yDisToT * 2;

		// Add indices to the set of uniq indices
    const start = x - (tRowSize - 1) / 2;
    const end = x + (tRowSize - 1) / 2;
    for (let i = start; i <= end; i++) {
      indicesSet.add(i);
    }
  });
  sensors.forEach(([x, y, bx, by]) => {
    if (by === targetY) {
      indicesSet.delete(bx);
    }
  });
  return { indices: Array.from(indicesSet.keys()) };
}
const { indices } = getTargetIndices(2000000);

console.log(indices.length);

const fs = require("fs");
const input = fs.readFileSync("2022/input/day-8.input.txt").toString();

const grid = input.split("\n").map((x) => x.split("").map(Number));
const visibleMap = {};

const rows = grid.length;
const columns = grid[0].length;

// Left to right
for (let i = 0; i < rows; i++) {
  let max = -1;
  for (let j = 0; j < columns; j++) {
    const value = grid[i][j];
    if (value > max) {
      max = value;
      visibleMap[`${i}-${j}`] = true;
    }
  }
}

// right to left
for (let i = rows - 1; i >= 0; i--) {
  let max = -1;
  for (let j = columns - 1; j >= 0; j--) {
    const value = grid[i][j];
    if (value > max) {
      max = value;
      visibleMap[`${i}-${j}`] = true;
    }
  }
}

// top to bottom
for (let j = 0; j < columns; j++) {
  let max = -1;
  for (let i = 0; i < rows; i++) {
    const value = grid[i][j];
    if (value > max) {
      max = value;
      visibleMap[`${i}-${j}`] = true;
    }
  }
}

// bottom to top
for (let j = columns - 1; j >= 0; j--) {
  let max = -1;
  for (let i = rows - 1; i >= 0; i--) {
    const value = grid[i][j];
    if (value > max) {
      max = value;
      visibleMap[`${i}-${j}`] = true;
    }
  }
}
console.log(Object.keys(visibleMap).length);

let maxScenicScore = 0;
for (let i = 0; i < rows; i++) {
  for (let j = 0; j < columns; j++) {
    const scenicScore = getScenicScore(i, j, grid);
    if (scenicScore > maxScenicScore) {
      maxScenicScore = scenicScore;
    }
  }
}
// NOT 240
// NOT 168
console.log(maxScenicScore);

//    0 1 2 3 4
// 0 [3 0 3 7 3]
// 1 [2 5 5 1 2]
// 2 [6 5 3 3 2]
// 3 [3 3 5 4 9]
// 4 [3 5 3 9 0]
// stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration
function getScenicScore(i, j, grid) {
	const treeHeight = grid[i][j];
  let up = i === 0 ? i : i - 1;
  while (up > 0 && grid[up][j] < treeHeight) {
    up--;
  }

  let down = i === rows - 1 ? i : i + 1;
  while (down < rows - 1 && grid[down][j] < treeHeight) {
    down++;
  }

  let left = j === 0 ? j : j - 1;
  while (left > 0 && grid[i][left] < treeHeight) {
    left--;
  }

  let right = j === columns - 1 ? j : j + 1;
  while (right < columns - 1 && grid[i][right] < treeHeight) {
    right++;
  }

  return (i - up) * (down - i) * (j - left) * (right - j);
}

const fs = require("fs");
const input = fs.readFileSync("2022/input/day-12.input.txt").toString();

const map = input.split("\n").map((x) => x.split(""));
const directions = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

const start = map.reduce((res, x, i) => {
  const j = x.findIndex((p) => p === "S");
  return j >= 0 ? [i, j] : res;
}, null);

const end = map.reduce((res, x, i) => {
  const j = x.findIndex((p) => p === "E");
  return j >= 0 ? [i, j] : res;
}, null);

const shortestPathsMap = getShortestPathTo(map, end);
console.log(shortestPathsMap[`${start[0]}-${start[1]}`].length); // 490

let min = Infinity;
map.forEach((row, i) =>
  row.forEach((col, j) => {
    if (col === "a" && shortestPathsMap[`${i}-${j}`]) {
      const value = shortestPathsMap[`${i}-${j}`].length;
      if (min > value) {
        min = value;
      }
    }
  })
);
console.log(min);

function getShortestPathTo(map, end) {
  const shortestPathsMap = {};
  const nextMoves = [];
  let nextMove = {
    pos: end,
    path: [],
  };
  do {
    const { pos, path } = nextMove;
    const key = `${pos[0]}-${pos[1]}`;

    const shortestPaths = shortestPathsMap[key];
    if (shortestPaths && shortestPaths.length <= path.length) {
      // already got to this point from a shorter path
      nextMove = nextMoves.pop();
      continue;
    }
    shortestPathsMap[key] = path;
    const nextPoses = getNextPos(map, pos);
    nextMoves.push(
      ...nextPoses.map((newPos) => ({
        pos: newPos,
        path: [...path, pos],
      }))
    );
    nextMove = nextMoves.pop();
  } while (nextMove);
  return shortestPathsMap;
}

function getNextPos(map, pos) {
  const nextDirections = directions
    .map(([x, y]) => [pos[0] + x, pos[1] + y])
    .filter(([x, y]) => {
      // Out of bounds
      if (x < 0 || x >= map.length || y < 0 || y >= map[0].length) {
        return false;
      }
      const curChar = map[pos[0]][pos[1]];
      const nextChar = map[x][y];
      // from b to a
      // from a to a
      // from a to z
      // not from z to a
      return getChatCode(curChar) - 1 <= getChatCode(nextChar);
    });
  return nextDirections;
}

function getChatCode(char) {
  if (char === "S") {
    return "a".charCodeAt();
  }
  if (char === "E") {
    return "z".charCodeAt();
  }
  return char.charCodeAt();
}

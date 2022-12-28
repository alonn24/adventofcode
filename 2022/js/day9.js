const fs = require("fs");
const input = fs.readFileSync("2022/input/day-9.input.txt").toString();

const moves = input.split("\n").map((x) => x.split(" "));

const visited = { "0-0": true };
let headPos = [0, 0];
let tailPos = [0, 0];

moves.forEach((move) => {
  const d = move[0];
  const n = Number(move[1]);
  Array.from({ length: n }).forEach(() => {
    headPos = moveHead(d, headPos);
    tailPos = moveTail(tailPos, headPos);
    visited[`${tailPos[0]}-${tailPos[1]}`] = true;
  });
});
console.log(Object.keys(visited).length);

const newVisited = { "0-0": true };
const rope = Array.from({ length: 10 }).map(() => [0, 0]);
moves.forEach((move) => {
  const d = move[0];
  const n = Number(move[1]);
  Array.from({ length: n }).forEach(() => {
    rope[0] = moveHead(d, rope[0]);
    rope.forEach((_, i) => {
      if (i > 0) {
        rope[i] = moveTail(rope[i], rope[i - 1]);
      }
    });
    newVisited[`${rope[9][0]}-${rope[9][1]}`] = true;
  });
});
// NOT 2565
console.log(Object.keys(newVisited).length);

function moveHead(d, pos) {
  if (d === "U") {
    return [pos[0] - 1, pos[1]];
  }
  if (d === "D") {
    return [pos[0] + 1, pos[1]];
  }
  if (d === "L") {
    return [pos[0], pos[1] - 1];
  }
  if (d === "R") {
    return [pos[0], pos[1] + 1];
  }
}

// 0 1 2
// x x x
// H x T
// x x x
function moveTail(tailPos, headPos) {
  const dx = headPos[0] - tailPos[0];
  const dy = headPos[1] - tailPos[1];

  if (Math.abs(dx) <= 1 && Math.abs(dy) <= 1) {
    return tailPos;
  }
  const move = [0, 0];
  if (dx > 0) {
    move[0] += 1;
  } else if (dx < 0) {
    move[0] -= 1;
  }

  if (dy > 0) {
    move[1] += 1;
  } else if (dy < 0) {
    move[1] -= 1;
  }
  return [tailPos[0] + move[0], tailPos[1] + move[1]];
}

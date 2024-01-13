const fs = require("fs");
const input = fs.readFileSync("2022/input/day-14.input.txt").toString();

const paths = input
  .split("\n")
  .map((x) => x.split(" -> ").map((y) => y.split(",").map(Number)));

const ROCK = "#";
const SAND = "o";

const startPoint = [500, 0];
class Cave {
  // column -> row -> value
  _cave = {};

  addToCave([x, y], s) {
    this._cave[x] = this._cave[x] ?? {};
    this._cave[x][y] = s;
  }

  addRocks(from, to) {
    const [x, y] = from;
    const [x2, y2] = to;
    const colSteps = Math.abs(x - x2);
    const colDir = x < x2 ? 1 : -1;
    for (let i = 0; i <= colSteps; i++) {
      this.addToCave([x + i * colDir, y], ROCK);
    }

    const rowSteps = Math.abs(y - y2);
    const rowDir = y < y2 ? 1 : -1;
    for (let i = 0; i <= rowSteps; i++) {
      this.addToCave([x, y + i * rowDir], ROCK);
    }
  }

  dropSandAt([x, y]) {
    let currentPoint = [x, y];
    if (!this._cave[x] || !this._cave[x - 1] || !this._cave[x + 1]) {
      return Infinity;
    }
    const nextPoint =
      (!this._cave[x][y + 1] && [x, y + 1]) ||
      (!this._cave[x - 1][y + 1] && [x - 1, y + 1]) ||
      (!this._cave[x + 1][y + 1] && [x + 1, y + 1]);
    if (!nextPoint) {
      return currentPoint;
    }
    return this.dropSandAt(nextPoint);
  }

  dropSandAtWithFloor([x, y], floor) {
    this._cave[x] = this._cave[x] || {};
    this._cave[x + 1] = this._cave[x + 1] || {};
    this._cave[x - 1] = this._cave[x - 1] || {};

    if (y >= floor) {
      return [x, y];
    }

    const nextPoint =
      (y >= floor && [x, y]) ||
      (!this._cave[x][y + 1] && [x, y + 1]) ||
      (!this._cave[x - 1][y + 1] && [x - 1, y + 1]) ||
      (!this._cave[x + 1][y + 1] && [x + 1, y + 1]);
    if (!nextPoint) {
      return [x, y];
    }
    return this.dropSandAtWithFloor(nextPoint, floor);
  }

  toJSON() {
    return this._cave;
  }

  toString() {
    const all = [];
    for (let i = 0; i <= 13; i++) {
      const res = [];
      for (let j = 485; j <= 513; j++) {
        res.push(this._cave[j]?.[i] || ".");
      }
      all.push(res.join(""));
    }
    return all.join("\n");
  }
}

// fill the rocks
const cave = new Cave();
paths.forEach((path) => {
  path.forEach((p, i) => {
    const next = path[i + 1];
    if (!next) return;
    cave.addRocks(p, next);
  });
});

// Start dropping without a floor
let sandCount = 0;
for (
  let droppedPosition = cave.dropSandAt(startPoint);
  droppedPosition !== Infinity;

) {
  cave.addToCave(droppedPosition, SAND);
  droppedPosition = cave.dropSandAt(startPoint);
  sandCount++;
}
console.log(sandCount);

// part 2
const cave2 = new Cave();
paths.forEach((path) => {
  path.forEach((p, i) => {
    const next = path[i + 1];
    if (!next) return;
    cave2.addRocks(p, next);
  });
});

const floor = Math.max(...paths.flatMap((x) => x.map((p) => p[1]))) + 1;
let droppedPosition;
let sandCount2 = 0;
do {
  droppedPosition = cave2.dropSandAtWithFloor(startPoint, floor);
  cave2.addToCave(droppedPosition, SAND);
  sandCount2++;
} while (
  droppedPosition[0] !== startPoint[0] ||
  droppedPosition[1] !== startPoint[1]
);

console.log(sandCount2);

const fs = require('fs');
const input = fs.readFileSync('2017/input/day-12.input').toString();

const villages = input.split('\n');
const graph = villages.reduce((res, v) => {
  const [num, connected] = v.split(' <-> ');
  const negh = connected.replace(/\s/g, '').split(',');
  res[num] = res[num] || [];
  res[num].push(...negh);
  return res;
}, {});

let visited = [];
let i = 0;
let count = 0;
const entryPoints = Object.keys(graph);
console.log('part1', Object.keys(findGroup(graph, '0')).length)

while (i < entryPoints.length && i >= 0) {
  count++;
  const group = findGroup(graph, entryPoints[i]);
  visited = visited.concat(Object.keys(group));
  i = findNextI(entryPoints, visited);
}
console.log('part2', count);
function findNextI(all, visited) {
  let res = -1;
  for (let j = 0; j < all.length; j++) {
    if (visited.indexOf(all[j]) < 0) {
      res = j;
    }
  }
  return res;
}

function findGroup(graph, curr, found = {}) {
  if (!found[curr]) {
    found[curr] = true;
    graph[curr].forEach(c => findGroup(graph, c, found));
  }
  return found;
}





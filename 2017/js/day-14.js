let input = 'uugsqrei';

let rows = [];
for (let i = 0; i < 128; i++) {
  const current = input + '-' + i;
  const knotHashVal = knotHash(current);
  rows[i] = knotHashVal.split('').reduce((res, x) => res + parseInt(x, 16).toString(2).padStart(4, 0), '').split('');
}
let map = {};
let total = 0;
rows.forEach((row, i) => {
  row.forEach((v, j) => {
    if (v === '1') {
      if (!map[`${i}-${j}`]) {
        total++;
      }
      color(rows, i, j);
    }
  });
});
console.log('part1', Object.keys(map).length)
console.log('part2', total);

function color(m, i, j) {
  if (m[i] && m[i][j] === '1' && !map[`${i}-${j}`]) {
    map[`${i}-${j}`] = true;
    [[i-1, j], [i+1, j], [i, j-1], [i, j+1]].forEach(e => color(m, e[0], e[1]));
  }
}

function sparseHash(nums, times, listLength) {
  let list = [];
  for (let i = 0; i < listLength; i++) list.push(i);
  list = [...list.slice(0, listLength), ...list.slice(0, listLength)];

  let pos = 0;
  let skip = 0;
  for (let i = 0; i < times; i++) {
    nums.forEach(n => {
      let part = list.slice(pos, pos + n);
      part = part.reduce((res, n) => {
        res.unshift(n);
        return res;
      }, []);
      part.forEach((n, i) => list[(pos + i) % listLength] = n);
      list = [...list.slice(0, listLength), ...list.slice(0, listLength)];
      pos = (pos + n + skip) % listLength;
      skip++;
    });
  }
  return list.slice(0, listLength);
}

function denseHash(nums) {
  let result = [];
  for (let i = 0; i < 16; i++) {
    const start = i * 16;
    result.push(nums.slice(start, start + 16).reduce((res, n) => res ^ n, 0));
  }
  return result;
}

function knotHash(input) {
  let listLength = 256;
  const sparseHashVal = sparseHash(input.replace(/\s/g, '').split('').map(x => x.charCodeAt(0)).concat([17, 31, 73, 47, 23]), 64, listLength);
  const denseHashVal = denseHash(sparseHashVal);
  const knotHash = denseHashVal.reduce((res, n) => {
    const hex = n.toString(16);
    return res + (hex.length === 1 ? `0${hex}` : hex);
  }, '');
  return knotHash;
}



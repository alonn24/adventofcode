function reverse(arr) {
  return arr.reduce((res, n) => {
    res.unshift(n);
    return res;
  }, []);
}

function sparseHasStep(listLength, [list, pos, skip], n) {
  const part = reverse(list.slice(pos, pos + n));
  const loopI = part.length - Math.max(pos + n - listLength, 0);
  const partToStart = part.slice(loopI);
  let half = partToStart
    .concat(list.slice(partToStart.length, pos))
    .concat(part.slice(0, loopI))
    .concat(list.slice(pos + n));
  const newList = [...half.slice(0, listLength), ...half.slice(0, listLength)];
  return [newList, (pos + n + skip) % listLength, skip + 1];
}

function sparseHash(nums, times, listLength) {
  let list = [];
  for (let i = 0; i < listLength; i++) list.push(i);
  list = [...list.slice(0, listLength), ...list.slice(0, listLength)];

  let pos = 0;
  let skip = 0;
  for (let i = 0; i < times; i++) {
    [list, pos, skip] = nums.reduce(([list, pos, skip], n) =>
      sparseHasStep(listLength, [list, pos, skip], n),
      [list, pos, skip]);
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

let input = '227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144';
const nums = input.replace(/\s/g, '').split('').map(x => x.charCodeAt(0)).concat([17, 31, 73, 47, 23]);
const sparseHashVal = sparseHash(nums, 64, 256);
const denseHashVal = denseHash(sparseHashVal);
const knotHash = denseHashVal.reduce((res, n) => {
  const hex = n.toString(16);
  return res + (hex.length === 1 ? `0${hex}` : hex);
}, '');
console.log(knotHash);

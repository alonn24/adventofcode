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

let input = '227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144';
let input2 = '3, 4, 1, 5';
// input += ',17, 31, 73, 47, 23';
let listLength = 256;
const sparseHashVal = sparseHash(input.replace(/\s/g, '').split('').map(x => x.charCodeAt(0)).concat([17, 31, 73, 47, 23]), 64, listLength);
const denseHashVal = denseHash(sparseHashVal);
const knotHash = denseHashVal.reduce((res, n) => {
  const hex = n.toString(16);
  return res + (hex.length === 1 ? `0${hex}`: hex);
}, '');
console.log(knotHash);

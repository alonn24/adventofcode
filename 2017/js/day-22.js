let input = '.###.#.#####.##.#...#....\n' +
  '..####.##.##.#..#.....#..\n' +
  '.#####.........#####..###\n' +
  '#.#..##..#.###.###.#.####\n' +
  '.##.##..#.###.###...#...#\n' +
  '#.####..#.#.##.##...##.##\n' +
  '..#......#...#...#.#....#\n' +
  '###.#.#.##.#.##.######..#\n' +
  '###..##....#...##....#...\n' +
  '###......#..#..###.#...#.\n' +
  '#.##..####.##..####...##.\n' +
  '###.#.#....######.#.###..\n' +
  '.#.##.##...##.#.#..#...##\n' +
  '######....##..##.######..\n' +
  '##..##.#.####.##.###.#.##\n' +
  '#.###.#.##....#.##..####.\n' +
  '#.#......##..####.###.#..\n' +
  '#..###.###...#..#.#.##...\n' +
  '#######..#.....#######..#\n' +
  '##..##..#..#.####..###.#.\n' +
  '..#......##...#..##.###.#\n' +
  '....##..#.#.##....#..#.#.\n' +
  '..#...#.##....###...###.#\n' +
  '#.#.#.#..##..##..#..#.##.\n' +
  '#.####.#......#####.####.';
// input = '..#\n' +
//   '#..\n' +
//   '...';
const toKey = ({i, j}) => `${i}/${j}`;
let map = {};
input.split('\n').forEach((row, i) =>
  row.split('').forEach((column, j) => {
    map[toKey({i, j})] = column;
  }));

// const [e, n, w, s]
const dirValues = [({i, j}) => ({i, j: j - 1}),
  ({i, j}) => ({i: i - 1, j}),
  ({i, j}) => ({i, j: j + 1}),
  ({i, j}) => ({i: i + 1, j})];

const middle = Math.floor(input.split('\n').length / 2);
let loc = {i: middle, j: middle};
let dirI = 1;

function part1() {
  function turn(i, mapValue) {
    const next = mapValue === '#' ? 1 : -1;
    return (i + next + 4) % 4;
  }

  let count = 0;
  for (let i = 0; i < 10000; i++) {
    const key = toKey(loc);
    dirI = turn(dirI, map[key])
    map[key] = map[key] === '#' ? '.' : '#';
    if (map[key] === '#') {
      count++;
    }
    loc = dirValues[dirI](loc);
  }

  console.log(count);
}

// part1()
function part2() {
  const symbols = ['.', 'W', '#', 'F'];

  function nextSymbol(s) {
    if (!s) {
      return 'W';
    }
    return symbols[(symbols.indexOf(s) + 1 + 4) % 4];
  }

  function turn(dirI, mapValue) {
    const next = (!mapValue || mapValue === '.') ? -1 : mapValue === '#' ? 1 : mapValue === 'F' ? 2 : 0;
    return (dirI + next + 4) % 4;
  }

  let count = 0;
  for (let i = 0; i < 10000000; i++) {
    const key = toKey(loc);
    dirI = turn(dirI, map[key])
    map[key] = nextSymbol(map[key])
    if (map[key] === '#') {
      count++;
    }
    loc = dirValues[dirI](loc);
  }

  console.log(count);
}

part2()

const fs = require("fs");
const input = fs.readFileSync("2022/input/day-7.input.txt").toString();

const [FILE, DIR] = ["file", "dir"];
function getType(str) {
  return str.indexOf("dir") === 0 ? DIR : FILE;
}
class SystemObject {
  children = [];
  size = 0;

  constructor(name, type, parent) {
    this.name = name;
    this.type = type;
    this.parent = parent;
  }

  getSize() {
    return this.size + this.children.reduce((res, x) => res + x.getSize(), 0);
  }

  findChild(name) {
    return this.children.find((x) => x.name === name);
  }

  addChild(child) {
    const existing = this.children.find((x) => x.name === child.name);
    if (!existing) {
      this.children.push(child);
    }
  }
}

const root = new SystemObject("/", DIR);

// Fill structure
let currentItem = root;
const instructions = input.split("\n");
for (ins of instructions) {
  const parts = ins.split(" ");
  if (parts[0] === "$") {
    if (parts[1] === "cd") {
      if (parts[2] === "..") {
        currentItem = currentItem.parent;
      } else if (parts[2] === "/") {
        currentItem = root;
      } else {
        currentItem = currentItem.findChild(parts[2]);
      }
    }
  } else {
    const type = parts[0] === "dir" ? DIR : FILE;
    const child = new SystemObject(parts[1], type, currentItem);
    if (type === FILE) {
      child.size = Number(parts[0]);
    }
    currentItem.addChild(child);
  }
}

const MAX = 100000;
// Find max directories
function flattenDirectories(item) {
  return [
    ...item.children.filter((x) => x.type === DIR),
    ...item.children.flatMap(flattenDirectories),
  ];
}
const directories = flattenDirectories(root);
const result = directories.filter((x) => x.getSize() <= MAX);
console.log(result.reduce((res, x) => res + x.getSize(), 0));

const DISK_SPACE = 70000000;
const NEED_SPACE = 30000000;
const needToFree = NEED_SPACE - (DISK_SPACE - root.getSize());

const sortedDirectories = directories.sort((a, b) =>
  a.getSize() > b.getSize() ? 1 : -1
);
const directoryToDel = sortedDirectories.find(x => x.getSize() >= needToFree);
console.log(directoryToDel.name, directoryToDel.getSize());

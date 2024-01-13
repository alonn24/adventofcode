const fs = require("fs");
const input = fs.readFileSync("2022/input/day-11.input.txt").toString();

const monkeys = input.split("\n\n").map((x) => {
  const [, strItems, strOpr, strTest, strIfTrue, strIfFalse] = x.split("\n");
  const items = strItems.split(":")[1].split(",").map(Number);
  const strTestValues = strTest.split(" ");
  // check values
  const test = Number(strTestValues[5]);
  const ifTrue = Number(strIfTrue.split("throw to monkey")[1]);
  const ifFalse = Number(strIfFalse.split("throw to monkey")[1]);
  const strOprValues = strOpr.split(" ");
  const action = strOprValues[6];
  const oprValue = strOprValues[7];

  return {
    items,
    test,
    performAction: (n) => {
      let value = oprValue === "old" ? n : Number(oprValue);
      value = typeof n === "bigint" ? BigInt(value) : value;
      if (action === "+") {
        return n + value;
      }
      if (action === "*") {
        return n * value;
      }
    },
    getMonkeyToThrow: (x) => {
      if (typeof x === "bigint") {
        const check = x % BigInt(test) === BigInt(0);
        return check ? ifTrue : ifFalse;
      }
      return x % test === 0 ? ifTrue : ifFalse;
    },
  };
});

function getPerformAction(strOpr) {
  const strOprValues = strOpr.split(" ");
  const action = strOprValues[6];
  const oprValue = strOprValues[7];
  return (n) => {
    let value = oprValue === "old" ? n : Number(oprValue);
    value = typeof n === "bigint" ? BigInt(value) : value;
    if (action === "+") {
      return n + value;
    }
    if (action === "*") {
      return n * value;
    }
  };
}

const monkeyBusinessCount = monkeys.map(() => 0);
const monkeysItems = monkeys.map((x) => x.items.map((x) => x));
Array.from({ length: 20 }).forEach(() => {
  monkeys.forEach((monkey, i) => {
    const items = monkeysItems[i];
    items.forEach((item) => {
      const worryLevel = Math.floor(monkey.performAction(item) / 3);
      const toThrow = monkey.getMonkeyToThrow(worryLevel);
      monkeysItems[toThrow].push(worryLevel);
    });

    // Update business level
    monkeyBusinessCount[i] += items.length;
    monkeysItems[i] = [];
  });
});

const sorted = monkeyBusinessCount.sort((x, y) => (x < y ? 1 : -1));
console.log(sorted[0] * sorted[1]);

const bigDivider = monkeys.reduce((res, m) => res * BigInt(m.test), BigInt(1));

// part 2
const monkeyBusinessCount2 = monkeys.map(() => 0);
const monkeysItems2 = monkeys.map((x) => x.items.map(BigInt));
Array.from({ length: 10000 }).forEach((_, r) => {
  monkeys.forEach((monkey, i) => {
    const items = monkeysItems2[i];
    items.forEach((item) => {
      const worryLevel = monkey.performAction(item) % bigDivider;
      const toThrow = monkey.getMonkeyToThrow(worryLevel);
      monkeysItems2[toThrow].push(worryLevel);
    });

    // Update business level
    monkeyBusinessCount2[i] += items.length;
    monkeysItems2[i] = [];
  });
});

// NOT 14481715519
const sorted2 = monkeyBusinessCount2.sort((x, y) => (x < y ? 1 : -1));
console.log(sorted2[0] * sorted2[1]);

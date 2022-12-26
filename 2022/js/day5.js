const fs = require('fs');
const input = fs.readFileSync('2022/input/day-5.input.txt').toString();

const [strCranes, strProcedure] = input.split('\n\n');
const procedure = strProcedure.split('\n').map(x => x.split(' '));

const strCranesStacks = strCranes.split('\n');
const strCranesNumbers = strCranesStacks.pop();
const cranesNumbers = strCranesNumbers.split(' ').filter(Boolean).map(Number);

function getInitialCranes() {
	const cranes = Array.from(new Array(cranesNumbers.length)).map(() => new Array());

	// Fill cranes
	// [V] [H] [B] [F] [H] [M] [B] [H] [B]
	//  1   5   9   13  17
	// 3 spaces between each item
	// first type is 1 (letter)
	// 2nd type is 2 (letter) + 1 (space) * 3 = 5
	// while x is crane index - type is (x+1)+x*3
	strCranesStacks.forEach(strCrane => {
		cranes.forEach((c,i) => {
			const typeIndex = i+1+i*3;
			if(strCrane[typeIndex] && strCrane[typeIndex] !== ' ') {
				c.unshift(strCrane[typeIndex]);
			}
		})
	});
	return cranes;
}

const cranes = getInitialCranes();
procedure.forEach((opr) => {
	const [n, from, to] = [opr[1], opr[3], opr[5]].map(Number);
	for(let i = 0; i < n; i++) {
		const value = cranes[from-1].pop();
		cranes[to-1].push(value)
	}
});
console.log(cranes.map(x => x[x.length-1]).join(''));

const cranes2 = getInitialCranes();
procedure.forEach((opr) => {
	const [n, from, to] = [opr[1], opr[3], opr[5]].map(Number);
	const values = cranes2[from-1].splice(cranes2[from-1].length - n);
	cranes2[to-1] = [...cranes2[to-1], ...values];
});
// not NRNMMTBPG
console.log(cranes2.map(x => x[x.length-1]).join(''));
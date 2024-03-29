const fs = require('fs');
const { chunk } = require('lodash/fp');
const input = fs.readFileSync('2022/input/day-3.input.txt').toString();

const rucksacks = input.split('\n').map(row => [row.slice(0, row.length/2), row.slice(row.length/2, row.length)])
const matching = rucksacks.map(rucksack => {
	const firstMap = new Set(rucksack[0]);
	return rucksack[1].split('').find(x => firstMap.has(x));
});

const aCode = 'a'.charCodeAt(0)
const ACode = 'A'.charCodeAt(0)
function getPriority(char) {
	const code = char.charCodeAt(0);
	if(code < aCode) return code-ACode+1+26;
	return code-aCode+1;
}

console.log(matching.reduce((res, x) => {
	return res + getPriority(x);
}, 0))

const groups = chunk(3, input.split('\n'));
const commonItemTypes = groups.map(([a,b,c]) => {
	const aMap = new Set(a);
	const bMap = new Set(b);
	return c.split('').find(x => aMap.has(x) && bMap.has(x));
});
console.log(commonItemTypes.reduce((res, x) => {
	return res + getPriority(x);
}, 0))

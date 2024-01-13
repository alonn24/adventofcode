const fs = require('fs');
const input = fs.readFileSync('2022/input/day-4.input.txt').toString();

const pairs = input.split('\n').map(x => x.split(',').map(x => x.split('-').map(Number)));
const numberOfContainedPairs = pairs.reduce((res, x) => {
	const isContainedBy = checkContainedBy(x[0], x[1]) || checkContainedBy(x[1], x[0]);
	return res + (isContainedBy ? 1 : 0);
}, 0);
console.log(numberOfContainedPairs)

const numberOfOverlappingPairs = pairs.reduce((res, x) => {
	const isOverlap = checkOverlap(x[0], x[1]);
	return res + (isOverlap ? 1 : 0);
}, 0);
console.log(numberOfOverlappingPairs)

function checkContainedBy(first, second) {
	return first[0]>=second[0] && first[1] <= second[1];
}

function checkOverlap(first, second) {
	return (first[0] >= second[0] && first[0] <= second[1]) ||
		(second[0] >= first[0] && second[0] <= first[1]);
}
const fs = require('fs');
const input = fs.readFileSync('2022/input/day-1.input.txt').toString();

function sumAll(arr) {
	return arr.reduce((sum, x) => sum+x, 0);
}

const elvesInventory = input.split('\n\n').map(x => x.split('\n').map(Number))
const elvesTotals = elvesInventory.map(sumAll);

const maxCaloriesForElv = Math.max(...elvesTotals);
console.log(`max calories carried by the max elv is ${maxCaloriesForElv}`)


elvesTotals.sort((x,y) => x>y? -1:1);
console.log(`Top 3 carries ${elvesTotals[0]+elvesTotals[1]+elvesTotals[2]}`)

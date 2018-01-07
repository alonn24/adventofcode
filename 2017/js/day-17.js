const input = 316;
let circularBuffer = [0];
let pos = 0;

for(let i=1; i <= 2018; i++) {
  pos = ((pos + input) % circularBuffer.length) + 1;
  circularBuffer.splice(pos+1, 0, i);
}
const index2017 = circularBuffer.indexOf(2017);
console.log(`part1: ${circularBuffer[index2017+1]}`)

pos = 0;
let length = 1;
let val = 0;
for (let i = 1; i < 50000000; i++) {
  pos = ((pos + input) % length) + 1;
  if (pos === 1) {
    val = i;
  }
  length++;
}

console.log(val);

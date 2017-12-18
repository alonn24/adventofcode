const input = 316;
const circularBuffer = [0];
let pos = 0;

for (let i = 1; i < 50000000; i++) {
  if (pos <= 1) {
    circularBuffer.splice(pos + 1, 0, i);
  }
  pos = (pos + input + 1) % circularBuffer.length;
}

console.log(circularBuffer[1]);

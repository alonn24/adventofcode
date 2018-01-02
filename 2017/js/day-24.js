const fs = require('fs');
const input = fs.readFileSync('2017/input/day-24.input').toString();

const ports = input.split('\n').map(x => x.split('/').map(x => +x));

function getBridges(prev, ports) {
  const lastPort = prev[prev.length - 1];
  const candidates = ports.filter(port => lastPort[1] === port[0] || lastPort[1] === port[1]);
  if (candidates.length === 0) {
    return [prev];
  } else {
    let res = [];
    candidates.forEach(port => {
      const portIndex = ports.indexOf(port);
      const nextPorts = [...ports.slice(0, portIndex), ...ports.slice(portIndex + 1)];
      const adjustedPort = lastPort[1] === port[0] ? port : [port[1], port[0]];
      const nextPrev = [...prev, adjustedPort];
      res.push(...getBridges(nextPrev, nextPorts));
    });
    return res;
  }
}

const bridges = getBridges([[0, 0]], ports);
let max = 0;
let maxBridge = [];
bridges.forEach(bridge => {
  const sum = bridge.reduce((sum, x) => sum + x[0] + x[1], 0);
  if (bridge.length > maxBridge.length ||
    (bridge.length === maxBridge.length && sum > max)) {
    max = sum;
    maxBridge = bridge;
  }
});
console.log(max);

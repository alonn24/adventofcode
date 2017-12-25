let input = '42/37\n' +
  '28/28\n' +
  '29/25\n' +
  '45/8\n' +
  '35/23\n' +
  '49/20\n' +
  '44/4\n' +
  '15/33\n' +
  '14/19\n' +
  '31/44\n' +
  '39/14\n' +
  '25/17\n' +
  '34/34\n' +
  '38/42\n' +
  '8/42\n' +
  '15/28\n' +
  '0/7\n' +
  '49/12\n' +
  '18/36\n' +
  '45/45\n' +
  '28/7\n' +
  '30/43\n' +
  '23/41\n' +
  '0/35\n' +
  '18/9\n' +
  '3/31\n' +
  '20/31\n' +
  '10/40\n' +
  '0/22\n' +
  '1/23\n' +
  '20/47\n' +
  '38/36\n' +
  '15/8\n' +
  '34/32\n' +
  '30/30\n' +
  '30/44\n' +
  '19/28\n' +
  '46/15\n' +
  '34/50\n' +
  '40/20\n' +
  '27/39\n' +
  '3/14\n' +
  '43/45\n' +
  '50/42\n' +
  '1/33\n' +
  '6/39\n' +
  '46/44\n' +
  '22/35\n' +
  '15/20\n' +
  '43/31\n' +
  '23/23\n' +
  '19/27\n' +
  '47/15\n' +
  '43/43\n' +
  '25/36\n' +
  '26/38\n' +
  '1/10';
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

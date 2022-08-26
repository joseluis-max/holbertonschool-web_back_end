import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('error', function (error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

subscriber.on('connect', function (error) {
  console.error('Redis client connected to the server');
});

const CHANNEL = 'holberton school channel';
const KILL_SERVER = 'KILL_SERVER';

subscriber.subscribe(CHANNEL);

subscriber.on('message', (channel, message) => {
  if (channel === CHANNEL) {
    console.log(message);
  }

  if (message === KILL_SERVER) {
    subscriber.unsubscribe(CHANNEL);
    subscriber.quit();
  }
});

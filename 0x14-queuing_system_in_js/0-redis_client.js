import { createClient } from 'redis';

const client = createClient();
 
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

client.on('connect', (err) => {
  console.error('Redis client connected to the server');
});

#!/usr/bin/node
/**
 * Connect to redis server via redis client
 */
import redis from 'redis';

const client = redis.createClient();


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
redisClient.subscribe('holberton school channel');

redisclient.on('message', (channel, message) => {
  console.log(message);

  if (message === 'KILL_SERVER'){
    client.unsubscribe(channel);
    client.quit();
  }
})

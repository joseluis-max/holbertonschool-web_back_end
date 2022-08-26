import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on("error", (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

client.on("connect", (err) => {
  console.error("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const asyncGet = promisify(client.get).bind(client);
  const value = await asyncGet(schoolName);
  console.log(value);
}

displaySchoolValue("Holberton").catch((err) =>  console.err(err));
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco").catch((err) =>  console.err(err));

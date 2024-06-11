import { createClient, print } from "redis";
import { promisify } from "util";
const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on("error", (er) =>{
    console.log('Redis client not connected to the server:', er);
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
}

const as = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
    console.log(await as(schoolName));
}

client.on("connect", async() => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
});

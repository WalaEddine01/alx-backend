import { createClient } from "redis";

const client = createClient();

client.on("error", (er) =>{
    console.log(er);
});

try {
    client.connect;
    console.log('Redis client connected to the server');
} catch (error) {
    console.log('Redis client not connected to the server:', error);
}

import { createClient, print } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on("error", (er) =>{
    console.log('Redis client not connected to the server:', er);
});

let a = 1
client.subscribe('holberton school channel');
client.on('message', (channel, message) => {

    if (message === 'KILL_SERVER') {
        a = 0;
        client.unsubscribe('holberton school channel', () => {
            console.log(`${message}`);
            client.quit();
        });
    }
    if (a != 0){
        console.log(`${message}`);
    }
});

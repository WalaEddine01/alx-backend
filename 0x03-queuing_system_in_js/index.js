import { createClient } from "redis";

const client = createClient();

client.on("error", (er) =>{
    console.log('error =>');
});

async function testRedis() {
    await client.connect();
    console.log('YESSSSSSSSSSSSS');

    await client.set("key", "value");
    console.log("KEY VALUE SETTTTTTT");

    const va = await client.get("key");
    console.log("the value of key is : ", va);

    await client.quit();
}

testRedis()
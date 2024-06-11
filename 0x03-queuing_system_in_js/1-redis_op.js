import { createClient, print } from "redis";

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

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, rep) => {
        if (err){
            console.log(err);
        }
        else {
            console.log(rep);
        }
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
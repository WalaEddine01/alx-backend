import { createQueue } from "kue";

const Queue = createQueue();

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

Queue.process("push_notification_code", (job) => {
    sendNotification(job.data.phoneNumber, job.data.message);
})

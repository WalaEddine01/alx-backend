import { Job, createQueue } from "kue";

const Queue = createQueue();

const blackListPhones = [
    "4153518780", "4153518781"
]


const sendNotification = (phoneNumber, message, job, done) => {

    job.progress(0, 100);

    if (blackListPhones.includes(phoneNumber)) {
      const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
      done(error);
      return;
    }

    job.progress(50, 100);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
      job.progress(100, 100);
      done();
    }, 2000);
  };

Queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

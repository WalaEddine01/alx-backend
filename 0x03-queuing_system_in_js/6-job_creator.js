import { createQueue } from "kue";

const Queue = createQueue();

const createJobObj = (phoneNumber, message) => {
    return {
        phoneNumber: phoneNumber,
        message: message
    };
    
};

const job = Queue.create('push_notification_code', createJobObj("333", "DDD")).save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.log('Error creating job:', err);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', (err) => {
  console.log('Notification job failed:', err);
}).on('progress', (progress) => {
  console.log(`Notification job ${job.id} ${progress}% complete`);
});


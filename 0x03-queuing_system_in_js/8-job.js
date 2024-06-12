import { createQueue } from "kue";

const Queue = createQueue();

const createPushNotificationsJobs = (jobs, queue) => {
    if(!Array.isArray(jobs)){
        throw Error('Jobs is not an array');
    }
    for(const j of jobs){
        const job = Queue.create("push_notification_code_3", j).save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`);
        } else {
          console.log('Error creating job:', err);
    }});
    job.on('complete', () => {
        console.log('Notification job completed');
      }).on('failed', (err) => {
        console.log('Notification job failed:', err);
      }).on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
}};

export default createPushNotificationsJobs;


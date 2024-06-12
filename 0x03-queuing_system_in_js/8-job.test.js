import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    console.log(`Notification job created: ${queue.testMode.jobs[0].id}`);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
    console.log(`Notification job created: ${queue.testMode.jobs[1].id}`);

    done();
  });
});

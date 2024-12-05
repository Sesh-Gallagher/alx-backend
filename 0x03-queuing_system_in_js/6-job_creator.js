#!/usr/bin/node
/**
 * Create a job
 */
import { createQueue } from 'kue';

const queue = createQueue();
const notifications = { 
    'phoneNumber': '+271346985',
    'message': 'This code is for  your identification' 
}

const job = queue.create('push_notification_code', notifications).save(function (error) {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', function() {
    console.log('Notification job completed');
}).on('failed', function() {
    console.log('Notification job failed');
});

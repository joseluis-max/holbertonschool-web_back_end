import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const client = redis.createClient();

const queue = kue.createQueue();

const clientGetAsync = promisify(client.get).bind(client);

const strAvailableSeats = 'available_seats';
const jobQueueName = 'reserve_seat';

let reservationEnabled = true;

function reserveSeat(number) {
  client.set(strAvailableSeats, number);
}

async function getCurrentAvailableSeats() {
  return await clientGetAsync(strAvailableSeats);
}

reserveSeat(50);

// Express API
const express = require('express');

const app = express();

app.listen(1245);

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  const msgReservationBlocked = { "status": "Reservation are blocked" };
  const msgReservationInProcess = { "status": "Reservation in process" };
  const msgReservationFailed = { "status": "Reservation failed" };

  if (!reservationEnabled) {
    res.json(msgReservationBlocked);
    return;
  }

  const job = queue.create(jobQueueName).save((err) => {
    if (err) {
      res.json(msgReservationFailed);
      return;
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });

  res.json(msgReservationInProcess);
  return;
});

app.get('/process', (req, res) => {
  const msgQueueProcessing = { "status": "Queue processing" };

  res.json(msgQueueProcessing);

  // Jobs processor
  queue.process(jobQueueName, async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();

    if (availableSeats == 1) reservationEnabled = false;

    if (availableSeats == 0) {
      done(new Error('Not enough seats available'));
      return;
    }

    reserveSeat(availableSeats - 1);
    done();
  });
});

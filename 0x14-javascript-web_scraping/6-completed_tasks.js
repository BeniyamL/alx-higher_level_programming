#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const TaskCompletedUser = {};

request(url, function (_err, response, body) {
  if (_err) {
    console.log(_err);
  } else {
    body = JSON.parse(body);
    for (let i = 0; i < body.length; i++) {
      const userId = body[i].userId;
      const cmplted = body[i].completed;
      if (cmplted && TaskCompletedUser[userId] === undefined) {
        TaskCompletedUser[userId] = 1;
      } else if (cmplted && TaskCompletedUser[userId]) {
        TaskCompletedUser[userId] += 1;
      }
    }
    console.log(TaskCompletedUser);
  }
});

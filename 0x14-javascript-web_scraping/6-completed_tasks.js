#!/usr/bin/node
// Script computes the tasks completed by UserId

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasks[userId] = (completedTasks[userId] || 0) + 1;
      }
    }

    console.log(completedTasks);
  }
});

#!/usr/bin/node
const { argv } = process;
const request = require('request');

request(argv[2], function (err, res, data) {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const todos = JSON.parse(data);
    const completedTasks = todos.reduce((compTasks, currTask) => {
      const uid = currTask.userId;

      if (isNaN(compTasks[uid]) && currTask.completed) {
        compTasks[uid] = 0;
      }
      currTask.completed && compTasks[uid]++;
      return compTasks;
    }, {});

    console.log(completedTasks);
  } catch (e) {
    console.error(e);
  }
});

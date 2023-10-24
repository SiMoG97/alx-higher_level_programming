#!/usr/bin/node
const { argv } = process;
const request = require('request');

// if (process.argv.length < 3) {
//   console.error('Usage: node 6-completed_tasks.js <URL>');
//   process.exit(1);
// }

request(argv[2], function (err, res, data) {
  if (err) {
    console.error(err);
    return;
  }
  try {
    let todos = JSON.parse(data);
    todos = Array.isArray(todos) ? todos : [];
    const completedTasks = todos.reduce((compTasks, currTask) => {
      const uid = currTask.userId;

      if (isNaN(compTasks[uid])) {
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

#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    try {
        const todos = JSON.parse(body);
        const completedTasks = {};

        todos.forEach(todo => {
            if (todo.completed) {
                if (completedTasks[todo.userId]) {
                    completedTasks[todo.userId]++;
                } else {
                    completedTasks[todo.userId] = 1;
                }
            }
        });

        // Remove users with no completed tasks
        for (const userId in completedTasks) {
            if (completedTasks[userId] === 0) {
                delete completedTasks[userId];
            }
        }

        console.log(completedTasks);
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});
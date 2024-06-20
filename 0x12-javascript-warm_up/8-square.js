#!/usr/bin/node
const process = require('process');

const args = process.argv.slice(2).join(' ');

if (args.length === 0 || isNaN(parseInt(args))) {
    console.log('Missing size');
} else {
    const word = 'X';
    let count = 0;
    const argssplit = args.split(' ');
    let output = '';
    while (argssplit[count] !== undefined) {
        const number = parseInt(argssplit[count]);
        for (let i = 0; i < number; i++) {
            for (let j = 0; j < number; j++) {
                output = output + word;
            }
            console.log(output);
            output = '';
        }
        count++;
    }
}

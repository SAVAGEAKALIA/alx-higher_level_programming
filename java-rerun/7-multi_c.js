#!/usr/bin/env node

const args = process.argv.slice(2);
let count;
let word = 'C is fun';


if (!isNaN(args[0])) {
    count = parseInt(args[0]);
    for (let i = 0; i < count; i++) {
        console.log(word);
    }
} else {
    console.log('Missing number of occurrences')
}
#!/usr/bin/env node

const args = process.argv.slice(2);
let size;
let word = 'X';
let output = '';

if (!isNaN(args[0])) {
    size = parseInt(args[0]);
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            output = output + word
        }
        console.log(output)
        output = '';
    }
} else {
    console.log('Missing size')
}
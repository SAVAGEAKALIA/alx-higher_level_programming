#!/usr/bin/env node

const args = process.argv.slice(2);

let arg1 = parseInt(args[0]);

if (!isNaN(arg1)) {
    console.log(`My number: ${arg1}`)
} else {
    console.log('Not a number')
}
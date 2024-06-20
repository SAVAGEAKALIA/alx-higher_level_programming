#!/usr/bin/env node

const args = process.argv.slice(2);

let arg1 = args[0];
let arg2 = args[1];

if (args.length === 1 || args.length > 1) {
    console.log(`${arg1} is ${arg2}`)
} else {
    console.log(`${arg1} is ${arg2}`)
}
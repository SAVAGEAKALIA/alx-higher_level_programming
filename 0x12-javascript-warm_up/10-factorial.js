#!/usr/bin/env node

const process = require('process');

const args = process.argv.slice(2).join(' ');

function factorial(a) {
    let result = 1;
    let n = a;
    for (let i = 1; i < a; i++) {
        result *= n;
        n = n - i;
    }
    return result;
}

if (args.length === 0 || isNaN(parseInt(args))) {
    console.log(1);
} else {
    const argssplit = args.split(' ');
    for (let i = 0; i < argssplit[i]; i++) {
        const a = parseInt(argssplit[i]);
        const result = factorial(a);
        console.log(result);
    }
}

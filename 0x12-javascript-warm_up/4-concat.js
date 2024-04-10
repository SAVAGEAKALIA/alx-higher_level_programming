#!/usr/bin/env node

const process = require('process');

const args = process.argv.slice(2).join(' ');

let output = '';
let output2 = '';
let i = 0;
const j = 'is';
let addis = false;
if (!args) {
    output += undefined + ' ' + j + ' ' + undefined;
    console.log(output);
} else if (args.includes(' ')) {
    const argssplit = args.split(' ');
    while (argssplit[i]) {
        output = '';
        output += argssplit[i];

        if (addis) {
            output2 += ' ' + j + ' ' + output;
        } else {
            output2 += output;
        }
        i++;
        addis = true;
    }

    console.log(output2);
} else {
    output += args + ' ' + j + ' ' + undefined;
    console.log(output);
}

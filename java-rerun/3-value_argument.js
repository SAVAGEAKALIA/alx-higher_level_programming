#!/usr/bin/env node

const arg = process.argv.slice(2);
// print process.argv


if (arg.length === 1) {
    console.log(arg[0]);
} else if (arg.length > 1) {
    arg.forEach((val, index) => {
        console.log(arg[index]);
    });
} else {
    console.log("No argument");
}

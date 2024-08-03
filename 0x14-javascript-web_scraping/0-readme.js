#!/usr/bin/node
const fs = require('fs')
const process = require('process')
ar = process.argv.slice(2)[0]

if (!ar) {
    console.error('Please provide a file path as an argument');
    process.exit(1);
}
fs.readFile(ar, "utf-8", (err, data) => {
    if (!err) {
        console.log(data);
    } else {
        console.log(err);
    }
})
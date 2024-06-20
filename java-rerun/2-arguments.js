#!/usr/bin/env node

const arg = process.argv.slice(2);
// print process.argv

if (arg.length === 1) {
    console.log("Argument found");
} else if (arg.length > 1) {
    console.log("Arguments Found")
} else {
    console.log("No argument");
}
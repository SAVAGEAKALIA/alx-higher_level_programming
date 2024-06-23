#!/usr/bin/env node

const args = process.argv.slice(2);
let a = args[0];
let b = args[1];
a = Number(a);
b = Number(b);

if (!isNaN(a) && !isNaN(b)) {
    // Convert string arguments to numbers

    // Define the add function
    function add(a, b) {
        return a + b;
    }

    // Call the add function and print the result
    const result = add(a, b);
    console.log(`The sum of ${a} and ${b} is ${result}`);
} else {
    if (!a) {
        console.log(`${b}`);
    } else {
        console.log(`${a}`);
    }
}

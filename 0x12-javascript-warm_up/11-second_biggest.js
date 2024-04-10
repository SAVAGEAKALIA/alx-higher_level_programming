#!/usr/bin/env node

const process = require('process');

const args = process.argv.slice(2).join(' ');

if (args.length === 0 || !args) { // Check for empty input
    console.log(0);
} else {
    const argssplit = args.split(' ');
    let result = -Infinity; // Initialize result to negative infinity
    let secondLargest = -Infinity; // Initialize secondLargest to negative infinity

    for (let i = 0; i < argssplit.length; i++) {
        const currentNumber = parseInt(argssplit[i]); // Parse current element to number

        if (!isNaN(currentNumber) && currentNumber > result) { // Check for valid number and larger than current result
            secondLargest = result;
            result = currentNumber;
        } else if (!isNaN(currentNumber) && currentNumber > secondLargest && currentNumber !== result) {
            secondLargest = currentNumber;
        }
    }

    if (secondLargest === -Infinity) { // Handle case where there are no valid numbers or less than 2 numbers
        console.log('No valid numbers provided or less than 2 numbers provided');
    } else {
        console.log(secondLargest);
    }
}

#!/usr/bin/node

function addAndCall(number, theFunction) {
    const updatedNumber = number + 1; // Increment the number using const for immutability

    // Call the function with the incremented value
    theFunction(updatedNumber);
}

module.exports = addAndCall;

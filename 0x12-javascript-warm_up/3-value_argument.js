#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2).join(' ');
let isadd = false;

if (!args) {
  console.log('No argument');
} else if (args.includes(' ')) {
  const argssplit = args.split(' ');
  let i = 0;
  let output2 = '';
  while (argssplit[i]) {
    let output = '';
    output += argssplit[i];

    if (isadd) {
      output2 += ' ' + output;
    } else {
      output2 += output;
    }
    i++;
    isadd = true;
  }
  console.log(output2);
} else {
  console.log(args);
}

#!/usr/bin/node

const fs = require('fs');

// Get the paths of the source files and the destination file from command line arguments
const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destFilePath = process.argv[4];

// Read the contents of the source files
fs.readFile(sourceFilePath1, 'utf8', (err, data1) => {
  if (err) throw err;

  fs.readFile(sourceFilePath2, 'utf8', (err, data2) => {
    if (err) throw err;

    // Concatenate the contents of the source files
    const result = data1 + '\n' + data2;

    // Write the result to the destination file
    fs.writeFile(destFilePath, result, 'utf8', err => {
      if (err) throw err;
      console.log('Files concatenated successfully.');
    });
  });
});

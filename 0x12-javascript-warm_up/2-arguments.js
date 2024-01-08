#!/usr/bin/node

const arg = process.argv[2];
const arg2 = process.argv[3];
if (arg) {
	if (arg2) {
		console.log('Arguments found');
	} else {
		console.log('Argument found');
	}
} else {
	console.log('No argument');
}

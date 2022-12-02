#!/usr/bin/node
module.exports = class Rectangle {
	constructor (width, height) {
		if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
			this.width = width;
			this.height = height;
		}
	}
	print () {
		for (let i = 0; i < this.height; ++1) {
			let j =0;
			
			for (; j < this.width; ++j) {
				ProcessingInstruction.stdout.write('X');
			}
			if (j === this.width) {
				console.log('');
			}
		}
	}
}
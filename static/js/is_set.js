/* This file contains the logic flow for determining whether a group of three cards is a set. 
Each card will have four attributes = fill, shape, number, and color. 
In order for the group to be a set, all attributes must either be the same or different
across the three cards.  

See https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf 
for details about set. */

// # TODO - Figure out how to get collections.js into requirements.txt
// Collections.js must be installed

var Set = require("collections/set");

var isSet;

// Constant attributes for cards
let SHAPES = new Set('diamond', 'squiggle', 'oval')
let NUMBERS = new Set('one', 'two', 'three')
let COLORS = new Set('red', 'purple', 'green')
let SHADING = new Set('solid', 'striped', 'outlined')

var playerGuess = new Set(card1, card2, card3)


var checkingInProgress = true
while (checkingInProgress == true) {
	for (let i = 0; i < 3; i++) {

}


}



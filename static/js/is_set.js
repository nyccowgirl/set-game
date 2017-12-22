/* This file contains the logic flow for determining whether a group of three cards is a set. 
Each card will have four attributes = fill, shape, number, and color. 
In order for the group to be a set, all attributes must either be the same or different
across the three cards.  

See https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf 
for details about set. */

// # TODO - Figure out how to get collections.js into requirements.txt
// Collections.js must be installed

let Set = require("collections/set");

// Constant attributes for cards
const SHAPES = new Set('diamond', 'squiggle', 'oval')
const NUMBERS = new Set('one', 'two', 'three')
const COLORS = new Set('red', 'purple', 'green')
const SHADING = new Set('solid', 'striped', 'outlined')

let playerGuess = [card1, card2, card3]


function checkIfSet(listOfCards) {
  let isSet = true;

}
while (checkingInProgress == true) {
	for (let i = 0; i < 3; i++) {
	}  if card

}

Event listener on click of card. click pushes card into array. 
once array length is three, check for set, act accordingly


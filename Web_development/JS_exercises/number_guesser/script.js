let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

/*
* My personal code is below
*/

// This function will be called at the beginning of each round and returns the number that user has to guess
const generateTarget = () => Math.floor(Math.random() * 10);
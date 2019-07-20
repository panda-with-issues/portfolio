let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

/*
* My personal code is below
*/

// This function will be called at the beginning of each round and returns the number that user has to guess
const generateTarget = () => Math.floor(Math.random() * 10);

function compareGuesses(userGuess, computerGuess, target) {
    // this will state whose guess is closer to target. The closest one wins the round. In case of tie, user wins and the function returns true
    if (userGuess < 0 || userGuess > 9) {
        // validate user input
        alert('You must enter an integer number between 0 and 9');
        return;
    };
    const deltaUser = Math.abs(target - userGuess);
    const deltaComputer = Math.abs(target - computerGuess);
    return deltaUser <= deltaComputer;
};

const updateScore = winner => winner === "human" ? humanScore++ : computerScore++;

const advanceRound = () => currentRoundNumber++;
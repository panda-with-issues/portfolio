// The purpose of this exercise is to build and test fluency with JS functions

const getUserChoice = userInput => {
    // sanitize and validate userInput
    userInput = userInput.toLowerCase();
    if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb') { // bomb is a cheat
        return userInput;
    };
    console.log('Invalid input. Choose between rock, paper or scissors.');
};

function getComputerChoice() {
    const random = Math.floor(Math.random() * 3);
    switch (random) {
        case 0:
            return 'rock';
        case 1:
            return 'paper';
        case 2:
            return 'scissors';
    }
};

function getWinner(userChoice, computerChoice) {
    console.log(`You played ${userChoice}, computer played ${computerChoice}`);
    // bomb always win
    if (userChoice === 'bomb') {
        return 'You win';
    };
    if (userChoice === computerChoice) {
        return "It's a tie!";
    };
    if ((userChoice === 'rock' && computerChoice === 'scissors') || (userChoice === 'paper' && computerChoice === 'rock') || (userChoice === 'scissors' && computerChoice === 'paper')) {
         return 'You win';
    } else {
        return 'You lose';
    }
};

console.log(getWinner(getUserChoice('paper'), getComputerChoice()));
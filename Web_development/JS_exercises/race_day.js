// The purpose of this program is to practice with workflow in JS.
let raceNumber = Math.floor(Math.random() * 1000);
// tell if the runner is registered in the first or the second phase
const isEarlyRegistered = true;
const runnerAge = 18;
// adult registered in the first phase are assigned a number above 1000
if (runnerAge > 18 && isEarlyRegistered) {
    raceNumber += 1000;
}
if (runnerAge > 18) {
    isEarlyRegistered ? console.log(`Your number is ${raceNumber}. You will run at 9:30 am.`) : console.log(`Your number is ${raceNumber}. You will run at 11:00 am.`);
} else if (runnerAge === 18) {
    console.log('Please see the registration desk.');
}
else {
    console.log(`Your number is ${raceNumber}. You will run at 12:30 am.`);
}
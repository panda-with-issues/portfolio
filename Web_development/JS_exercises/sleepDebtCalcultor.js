// Another exercise on JS functions

function getSleepHours(day) {
    switch (day) {
        case 'monday':
            return 6;
        case 'tuesday':
            return 8;
        case 'wednesday':
            return 7;
        case 'thursday':
            return 8;
        case 'friday':
            return 3;
        case 'saturday':
            return 4;
        case 'sunday':
            return 7;
        default:
            return 'not a valid weekday';
    }
};

const getActualSleepHours = () => getSleepHours('monday') + getSleepHours('tuesday') + getSleepHours('wednesday') + getSleepHours('thursday') + getSleepHours('friday') + getSleepHours('saturday') + getSleepHours('sunday');

const getIdealSleepHours = () => {
    const idealSleepHours = 7;
    return idealSleepHours * 7;
};

function getSleepDebt() {
    const actualSleepHours = getActualSleepHours();
    const idealSleepHours = getIdealSleepHours();
    const delta = actualSleepHours - idealSleepHours;
    if (actualSleepHours < idealSleepHours) {
        console.log(`You should sleep ${-delta} hours more`);
    } else if (actualSleepHours === idealSleepHours) {
        console.log('You sleep the perfect amount of hours!');
    } else {
        console.log(`You slept ${delta} hours more than needed`);
    }
};

getSleepDebt();

// I think this script is overly horrible, but the exercise wanted it like that...
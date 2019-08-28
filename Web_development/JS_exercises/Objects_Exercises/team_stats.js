/*
* This project is provided by codecademy.com
* We want to create and extract information about your favorite sports team. Basketball, soccer, tennis, or water polo, you pick it. It’’s your job to create data using the JavaScript data structures at your disposal: arrays, objects, etc.
* Once created, you can manipulate these data structures as well as gain insights from them. For example, you might want to get the total number of games your team has played, or the average score of all of their games.
*/
/*
* Task 1:
* We want a data structure to store the information about our team. Create an empty team object.
*/
const team = {
  /*
  * Task 2:
  * Our team has players, and the team plays games. We want to represent both of these. Add two properties to your team object. A _players property and a _games property that are both initialized to empty arrays.
  * Populate the empty array that corresponds to the _players key in your team object with three actual players. They should be in the following format:
  * {
  *   firstName: 'Pablo',
  *   lastName: 'Sanchez',
  *   age: 11
  * }
  * Populate the empty array that corresponds to the _games key in your object with three actual games. They should be in the following format:
  * {
  *   opponent: 'Broncos',
  *   teamPoints: 42,
  *   opponentPoints: 27
  * }
  */
  _players: [
    {
      firstName: 'Alan',
      lastName: 'Turing',
      age: 37
    },
    {
      firstName: 'Albert',
      lastName: 'Einstein',
      age: 55
    },
    {
      firstName: 'Arthur',
      lastName: 'Rimbaud',
      age: 17
    }
  ],
  _games: [
    {
      opponent: 'Greek Philosophers',
      teamPoints: 68,
      opponentPoints: 14
    },
    {
      opponent: 'Arab Mathematicians',
      teamPoints: 46,
      opponentPoints: 40
    },
    {
      opponent: 'Religions',
      teamPoints: 27,
      opponentPoints: 145
    }
  ],
  /*
  * Task 3:
  * Create getter methods for your _players and _games keys. You do not need to create setter methods, because we don’t want anyone to change the values saved to these keys.
  */
  get players () {
    return this._players
  },
  get games () {
    return this._games
  },
  /*
  * Task 4:
  * We want to add a new player to your team. Add a method addPlayer to your team object. This method should take in three parameters: firstName, lastName, and age. It should create a player object, and add them to the team‘s players array.
  */
  addPlayer (firstName, lastName, age) {
    const player = {
      firstName,
      lastName,
      age
    }
    this.players.push(player)
  },
  /*
  * Task 6:
  * The scorekeeper has some new information for us! Add a similar method for recording game results called addGame that:
  * takes in an opponent’s name,
  * your team’s points,
  * the opponent’s points,
  * creates a game object,
  * adds the game object to your team‘s games array.
  */
  addGame (opponent, teamPoints, opponentPoints) {
    const game = {
      opponent,
      teamPoints,
      opponentPoints
    }
    this.games.push(game)
  }
}
/*
* Task 5:
* Below your team object, invoke your addPlayer method on the following players: Steph Curry Age 28,Lisa Leslie Age 44, and Bugs Bunny Age 76.
* Print out the team‘s players to check they were all properly added.
*/
team.addPlayer('Steph', 'Curry', 28)
team.addPlayer('Lisa', 'Leslie', 44)
team.addPlayer('Bugs', 'Bunny', 76)
console.log(team.players)
/*
* Task 7:
* Invoke your addGame method on three games and print the team‘s updated games array.
*/
team.addGame('bimbi', 15, 55)
team.addGame('a caso', 56, 31)
team.addGame('universo', 45, 44)
console.log(team.games)

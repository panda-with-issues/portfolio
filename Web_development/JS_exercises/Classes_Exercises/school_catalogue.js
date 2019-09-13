/*
* This project is provided by codecademy.com
* Let’s put your knowledge of classes to the test by creating a digital school catalog for the New York City Department of Education. The Department of Education wants the catalog to hold quick reference material for each school in the city.
* We need to create classes for primary, middle, and high schools. Because these classes share properties and methods, each will inherit from a parent School class. Our parent and three child classes have the following properties, getters, setters, and methods:
*
* School
*
*   Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (number)
*   Getters: all properties have getters
*   Setters: the numberOfStudents property has a setter
*   Methods: .quickFacts() and .pickSubstituteTeacher() (this is a static method)
*
* Primary
*
*   Includes everything in the School class, plus one additional property
*   Properties: pickupPolicy (string)
*
* Middle
*
*   Does not include any additional properties or methods
*
* High
*
*   Includes everything in the School class, plus one additional property
*   Properties: sportsTeams (array of strings)
*/

class School {
  constructor (name, level, numberOfStudents) {
    this._name = name
    this._level = level
    this._numberOfStudents = numberOfStudents
  }

  get name () {
    return this._name
  }

  get level () {
    return this._level
  }

  get numberOfStudents () {
    return this._numberOfStudents
  }

  set numberOfStudents (number) {
    if (typeof number === 'number') {
      this._numberOfStudents = number
    } else {
      console.log('Invalid input: numberOfStudents must be set to a Number.')
    }
  }

  quickFacts () {
    console.log(`${this._name} educates ${this._numberOfStudents} students at the ${this._level} school level.`)
  }

  static pickSubstituteTeacher (substituteTeachers) { // substituteTeachers is an array of strings (teachers' name)
    return substituteTeachers[Math.floor(Math.random() * substituteTeachers.length)]
  }
}

class Primary extends School {
  constructor (name, numberOfStudents, pickupPolicy) {
    super(name, 'primary', numberOfStudents)
    this._pickupPolicy = pickupPolicy
  }

  get pickupPolicy () {
    return this._pickupPolicy
  }
}

class Middle extends School {
  constructor (name, numberOfStudents) {
    super(name, 'middle', numberOfStudents)
  }
}

class High extends School {
  constructor (name, numberOfStudents, sportsTeams) {
    super(name, 'high', numberOfStudents)
    this._sportsTeams = sportsTeams
  }

  get sportsTeams () {
    this._sportsTeams.forEach(sport => console.log(sport))
  }
}

/*
* Create a PrimarySchool instance with the following properties:
*
*   Name: 'Lorraine Hansbury'
*   Number of Students: 514
*   Pickup Policy: 'Students must be picked up by a parent, guardian, or a family member over the age of 13.'
*
* Save the instance to a constant variable named lorraineHansbury.
*/

const lorraineHansbury = new Primary('Lorraine Hansbury', 514, 'Students must be picked up by parent, guardian, or a family member over the age of 13.')

/*
* Call .quickFacts() on the lorraineHansbury instance.
*/

lorraineHansbury.quickFacts() // log 'Lorraine Hansbury educates 514 students at the primary school level.'

/*
* The principal of Lorraine Hansbury needs a substitute teacher for the day.
* Call .pickSubstituteTeacher() on School, and pass the following array as an argument:
*/

const arr = ['Jamal Crawford', 'Lou Williams', 'J. R. Smith', 'James Harden', 'Jason Terry', 'Manu Ginobli']

Primary.pickSubstituteTeacher(arr) // return a random teacher as expected

/*
* Create a HighSchool instance with the following properties:
*
*   Name: 'Al E. Smith'
*   Number of Students: 415
*   Sports Teams: ['Baseball', 'Basketball', 'Volleyball', 'Track and Field']
*
* Save the instance to a constant variable named alSmith.
*/

const alSmith = new High('Al E. Smith', 415, ['Baseball', 'Basketball', 'Volleyball', 'Track and Field'])

/*
* Get the value saved to the sportsTeams property in alSmith.
*/

alSmith.sportsTeams // log each element of the array, as intended

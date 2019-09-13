/*
* This project is provided by codecdemy.com
*
* Congratulations, you’ve passed the grueling rigmarole of librarian school and have become head librarian at your local Books-‘N-Stuff.
* Books-‘N-Stuff carries three different types of media: books, CDs, and movies. In this project you will create a parent class named Media with three subclasses: Book, Movie, and CD. These three subclasses have the following properties and methods:
*
* Book
*   Properties: author (string), title (string), pages (number), isCheckedOut (boolean, initially false), and ratings (array, initially empty).
*   Getters: all properties have a getter
*   Methods: .getAverageRating(), .toggleCheckOutStatus(), and .addRating()
*
* Movie
*
*   Properties: director (string), title (string), runTime (number), isCheckedOut (boolean, initially false), and ratings (array, initially empty)
*   Getters: all properties have a getter
*   Methods: .getAverageRating(), .toggleCheckOutStatus(), and .addRating()
*
* CD
*
*   Properties: artist (string), title (string), isCheckedOut (boolean, initially false), and ratings (array, initially empty), songs (array of strings)
*   Getters: all properties have a getter
*   Methods: .getAverageRating(), .toggleCheckOutStatus(), and .addRating()
*/

class Media {
  constructor (title) {
    this._title = title
    this._isCheckedOut = false
    this._ratings = []
  }

  get title () {
    return this._title
  }

  get isCheckedOut () {
    return this._isCheckedOut
  }

  get ratings () {
    return this._ratings
  }

  getAverageRating () {
    const sum = this._ratings.reduce((accumulator, currentValue) => accumulator + currentValue)
    return (sum / this._ratings.length).toFixed(1)
  }

  toggleCheckOutStatus () {
    this._isCheckedOut = !this._isCheckedOut
  }

  addRating (rating) {
    this._ratings.push(rating)
  }
}

class Book extends Media {
  constructor (title, author, pages) {
    super(title)
    this._author = author
    this._pages = pages
  }

  get author () {
    return this._author
  }

  get pages () {
    return this._pages
  }
}

class Movie extends Media {
  constructor (title, director, runTime) {
    super(title)
    this._director = director
    this._runTime = runTime
  }

  get director () {
    return this._director
  }

  get runTime () {
    return this._runTime
  }
}

class CD extends Media {
  constructor (title, artist, songs) {
    super(title)
    this._artist = artist
    this._songs = songs
  }

  get artist () {
    return this._artist
  }

  get songs () {
    return this._songs
  }
}

/*
* Create a Book instance with the following properties:
*
*   Author: 'Bill Bryson'
*   Title: 'A Short History of Nearly Everything'
*   pages: 544
*
* Save the instance to a constant variable named historyOfEverything.
*/

const historyOfEverything = new Book('A Short History of Nearly Everything', 'Bill Bryson', 544)

/*
* Call .toggleCheckOutStatus() on the historyOfEverything instance.
* Log the value saved to the isCheckedOut property in the historyOfEverything instance.
*/

historyOfEverything.toggleCheckOutStatus()
console.log(historyOfEverything.isCheckedOut) // returns true

/*
* Call .addRating() three times on historyOfEverything with inputs of 4, 5, and 5.
* Call .getAverageRating() on historyOfEverything. Log the result to the console.
*/

historyOfEverything.addRating(4)
historyOfEverything.addRating(5)
historyOfEverything.addRating(5)
console.log(historyOfEverything.getAverageRating())

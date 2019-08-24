/*
* This project is provided by codecademy.com
*
* As a frequent diner, you love trying out new restaurants and experimenting with different foods. However, having to figure out what you want to order can be a time-consuming ordeal if the menu is big, and you want an easier way to be able to figure out what you are going to eat.
* In this project, you’ll use JavaScript to randomly create a three-course meal based on what is available on a menu. We’ll keep running it until we’re satisfied with the generated meal!
*/




* Task 4:
* Inside the menu object, we are going to create a method called .addDishToCourse() which will be used to add a new dish to the specified course on the menu.
* The method should take in three parameters: the courseName, the dishName , and the dishPrice.
* The .addDishToCourse() method should create an object called dish which has a name and price which it gets from the parameters.
* The method should then push this dish object into the appropriate array in your menu‘s _courses object based on what courseName was passed in.
*
* Task 5:
* Now, we’re going to need another function which will allow us to get a random dish from a course on the menu, which will be necessary for generating a random meal.

Create a method inside the menu object called .getRandomDishFromCourse(). It will take in one parameter which is the courseName.

*/

/*
* Task 1:
* Start by creating a menu object.
* Add a _courses property to your menu object. This property will ultimately contain a mapping between each course and the dishes available to order in that course.
* Create three properties inside the _courses object called appetizers, mains, and desserts. Each one of these should initialize to an empty array.
*/
const menu = {
  _courses: {
    appetizers: [],
    mains: [],
    desserts: []
  },
  /*
  * Task 2:
  * Create getter and setter methods for the appetizers, mains, and desserts properties.
  */
  get appetizers () {
    return this._courses.appetizers
  },
  get mains () {
    return this._courses.mains
  },
  get desserts () {
    return this._courses.desserts
  },
  set appetizers (appetizer) {
    this._courses.appetizers = appetizer
  },
  set mains (main) {
    this._courses.mains = main
  },
  set desserts (dessert) {
    this._courses.desserts = dessert
  },
  /*
  * Task 3:
  * Inside your menu object, create a getter method for the _courses property. Inside the courses getter method, return an object that contains key/value pairs for appetizers, mains, and desserts.
  */
  get courses () {
    return this._courses
  },
  // task 4
  addDishToCourse (courseName, dishName, dishPrice) {
    let dish = {
      dishName,
      dishPrice
    }
    this[courseName].push(dish)
  }
}

console.log(menu.courses)

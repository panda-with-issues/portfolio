/*
* This project is provided by codecademy.com
*
* As a frequent diner, you love trying out new restaurants and experimenting with different foods. However, having to figure out what you want to order can be a time-consuming ordeal if the menu is big, and you want an easier way to be able to figure out what you are going to eat.
* In this project, you’ll use JavaScript to randomly create a three-course meal based on what is available on a menu. We’ll keep running it until we’re satisfied with the generated meal!
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
  /*
  * Task 4:
  * Inside the menu object, we are going to create a method called .addDishToCourse() which will be used to add a new dish to the specified course on the menu.
  * The method should take in three parameters: the courseName, the dishName , and the dishPrice.
  * The .addDishToCourse() method should create an object called dish which has a name and price which it gets from the parameters.
  * The method should then push this dish object into the appropriate array in your menu‘s _courses object based on what courseName was passed in.
  */
  addDishToCourse (courseName, dishName, dishPrice) {
    const dish = {
      dishName,
      dishPrice
    }
    this[courseName].push(dish)
  },
  /*
  * Task 5:
  * Now, we’re going to need another function which will allow us to get a random dish from a course on the menu, which will be necessary for generating a random meal.
  * Create a method inside the menu object called .getRandomDishFromCourse(). It will take in one parameter which is the courseName.
  */
  getRandomDishFromCourse (courseName) {
    // Retrieve the array of the given course’s dishes from the menu‘s _courses object and store in a variable called dishes.
    const dishes = menu.courses[courseName]
    // Generate a random index by multiplying Math.random() by the length of the dishes array
    const randIdx = Math.floor(Math.random() * dishes.length)
    // Return the dish located at that index in dishes.
    return dishes[randIdx]
  },
  /*
  * Task 6:
  * Now that we have a way to get a random dish from a course, we can create a .generateRandomMeal() function which will automatically generate a three-course meal for us. The function doesn’t need to take any parameters.
  */
  generateRandomMeal () {
    // The function should create an appetizer variable which should be the result of calling the .getRandomDishFromCourse() method when we pass in an appetizers string to it.
    const appetizer = menu.getRandomDishFromCourse('appetizers')
    // Create a main variable and dessert variable the same way you created the appetizer variable, but make sure to pass in the right course type.
    const main = menu.getRandomDishFromCourse('mains')
    const dessert = menu.getRandomDishFromCourse('desserts')
    // Calculates the total price and returns a string that contains the name of each of the dishes and the total price of the meal, formatted as you like.
    const bill = appetizer.dishPrice + main.dishPrice + dessert.dishPrice
    return `I've chosen this menu for you: ${appetizer.dishName}, ${main.dishName}, and ${dessert.dishName}. You'll pay ${bill} €.`
  }
}

/*
* Task 7:
* Now that we’ve finished our menu, object, let’s use it to create a menu by adding some appetizers, mains, and desserts with the .addDishToCourse() function. Add at least 3 dishes to each course (or more if you like!).
*/

menu.addDishToCourse('appetizers', 'Chinese Bread', 1.5)
menu.addDishToCourse('appetizers', 'Harumaki roll', 1.5)
menu.addDishToCourse('appetizers', 'Curry triangles', 1.5)
menu.addDishToCourse('mains', 'Soya spaghetti with shrimps', 3.4)
menu.addDishToCourse('mains', 'Beef with onions', 5)
menu.addDishToCourse('mains', 'Spicy ribs with salt and pepper', 4.8)
menu.addDishToCourse('desserts', 'Fried fruits', 2.6)
menu.addDishToCourse('desserts', 'Fried ice cream', 3)
menu.addDishToCourse('desserts', 'Candy fruits', 2.8)

/*
* Once your menu has items inside it, generate a meal by using the .generateRandomMeal() function on your menu, and save it to a variable called meal. Lastly, print out your meal variable to see what meal was generated for you.
*/

const meal = menu.generateRandomMeal()
console.log(meal)

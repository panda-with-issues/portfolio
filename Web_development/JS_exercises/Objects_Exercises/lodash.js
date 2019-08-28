/*
* This project is provided by codecademy.com
* In this project, you will be implementing some of the most exciting functionality from the widely-popular lodash.js library. You will be implementing ten methods that add new functionality for numbers, strings, objects, and arrays.
*/
/*
* Task 1:
* Before we get started implementing our new methods, we need to create an object to contain them. This object will represent our library containing all the functionality we add to it.
* Create a new variable called _ that is initialized to an empty object.
*/
const _ = {
  /* Task 2:
  * The first method we will implement is .clamp(). It takes three arguments: a number, a lower bound, and an upper bound. .clamp() modifies the provided number to be within the two provided bounds:
  * If the provided number is smaller than the lower bound, it will return the lower bound as the final number
  * If the number is larger than the upper bound, it will return the upper bound as the final number
  * If the number is already within the two bounds, it will return the number as the final number
  */
  clamp (n, lower, upper) {
    const clampDown = Math.max(n, lower)
    return Math.min(clampDown, upper)
  },
  /*
  * Task 3:
  * The next number method we will implement is .inRange(). Here is a summary of the method: .inRange() takes three arguments: a number, a start value, and an end value and checks to see if the provided number falls within the range specified by the start and end values.
  * If the provided number is smaller than the start value, .inRange() will return false
  * If the provided number is larger than or equal to the end value, .inRange() will return false
  * If the provided number is within the start and end values, .inRange() will return true
  * If no end value is provided to the method, the start value will be 0 and the end value will be the provided start value
  * If the provided start value is larger than the provided end value, the two values should be swapped
  */
  inRange (n, start, end) {
    if (typeof end === 'undefined') {
      end = start
      start = 0
    }
    if (start > end) {
      const temp = start
      start = end
      end = temp
    }
    return n >= start && n < end
  }
}

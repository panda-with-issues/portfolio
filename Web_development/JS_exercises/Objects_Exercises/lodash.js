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
  },
  /*
  * Task 4:
  * The next string method we will implement is .pad(). .pad() takes three arguments: a string, a length and a str of characters to pad with.
  * .pad() adds spaces evenly to both sides of the string to make it reach the desired length
  * Extra padding is added to the end of the string if an odd amount of padding is required to reach the specified length
  */
  pad (str, length, char) {
    if (typeof char === 'undefined') {
      char = ' '
    }
    if (str.length < length) {
      const padLength = length - str.length
      let pad = ''
      for (let i = 0; i < Math.floor(padLength / 2); i++) {
        const charToPush = char[i % char.length]
        pad += charToPush
      }
      if (padLength % 2 === 1) {
        const padL = pad + char[pad.length % char.length]
        return pad + str + padL
      }
      return pad + str + pad
    }
    return str
  },
  /*
  * Task 5:
  * Let’s begin implementing some new object methods! The first object method we will implement is .has(). It takes two arguments: an object and a path. .has() checks to see if the provided object contains a value at the specified key.
  * .has() will return true if the object contains a value at the key and will return false if not
  */
  has (obj, path) {
    if (typeof path === 'string') {
      path = path.split(/[.[\]']/) // match . [ ] '
      // clean from empty substrings
      for (let i = path.length - 1; i >= 0; i--) {
        if (path[i] === '') {
          path.splice(i, 1)
        }
      }
    }
    // base case
    if (path.length === 1) {
      return Object.keys(obj).includes(path[0])
    }
    // inductive step
    const nextProperty = path.shift()
    obj = obj[nextProperty]
    return this.has(obj, path)
  },
  /*
  * Task 6:
  * The next object method we will implement is .invert(). It takes one argument -- an object --, iterates through each key / value pair in the provided object and swaps the key and value
  */
  invert (obj) {
    const result = {}
    for (const prop in obj) {
      result[obj[prop]] = prop
    }
    return result
  },
  /*
  * Task 7:
  * The final object method we will implement is .findKey(). It takes two arguments: an object and a predicate function — a function that returns a boolean value.
  * .findKey() iterates through each key / value pair in the provided object and calls the predicate function with the value
  * .findKey() returns the first key that has a value that returns a truthy value from the predicate function
  * .findKey() returns undefined if no values return truthy values from the predicate function
  */
  findKey (obj, predicate) {
    for (const key in obj) {
      if (predicate(obj[key])) {
        return key
      }
    }
  },
  /*
  * Task 8:
  * It’s time to start implementing methods for our final data type: arrays! The first array method we will implement is .drop(). It takes two arguments: an array and a number representing the number of items to drop from the beginning of the array
  * .drop() returns a new array which contains the elements from the original array, excluding the specified number of elements from the beginning of the array
  * If the number of elements to drop is unspecified, your method should drop one element
  */
  drop (arr, n) {
    if (typeof n === 'undefined') {
      n = 1
    }
    return arr.slice(n)
  },
  /*
  * Task 9:
  * The next array method we will implement is .dropWhile(). It takes two arguments: an array and a predicate function
  * The supplied predicate function takes three arguments: the current element, the current element index, and the whole array
  * .dropWhile() creates a new copy of the supplied array, dropping elements from the beginning of the array until an element causes the predicate function to return a falsy value
  */
  dropWhile (arr, func) {
    const arrCopy = arr.slice()
    const n = arrCopy.findIndex((val, idx) => !func(val, idx, arrCopy))
    return arrCopy.slice(n)
  },
  /*
  * Task 9
  * The last array method we will implement is .chunk(). It takes two arguments: an array and a size
  * .chunk() breaks up the supplied array into arrays of the specified size
  * .chunk() returns an array containing all of the previously-created array chunks in the order of the original array
  * If the array can’t be broken up evenly, the last chunk will be smaller than the specified size
  * If no size is supplied to the method, the size is set to 1
  */
  chunk (arr, length) {
    if (typeof length === 'undefined') length = 1
    const result = []
    while (arr.length) {
      result.push(arr.splice(0, length))
    }
    return result
  }
}
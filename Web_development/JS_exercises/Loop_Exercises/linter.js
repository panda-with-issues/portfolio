/*
* This program wants to mock a linter in order to do some operation on a given text
* This project is provided by codecademy.com and all of its tasks must be resolved only using array iteration methods
*/

// begin of code provided by codecademy.com

let story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.';

let overusedWords = ['really', 'very', 'basically'];

let unnecessaryWords = ['extremely', 'literally', 'actually' ];

// end of code provided by codecademy.com

/*
* First task
* We want to gather some information about the individual words and sentences in the string. Let’s split the string into individual words and save them in a new array called storyWords.
*/

const storyWords = story.split(' ')

/*
* Second task
* Log how many words there are in this story to the console.
*/

console.log(storyWords.length) // 188

/*
* Third task
* There is an array of words that are unnecessary. Iterate over your array to filter out these words. Save the remaining words in an array called betterWords.
*/

const betterWords = storyWords.filter(word => {
  return !unnecessaryWords.includes(word)
})

// follow several test functions

function isEqual (arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false
  };
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false
    }
  }
  return true
}

console.log(isEqual(storyWords, betterWords)) // false

function getDiffIds (arr1, arr2) {
  const ids = []
  if (arr1.length < arr2.length) {
    return 'swap arrays'
  };
  let i = 0
  let j = 0
  while (j < arr2.length) {
    if (arr1[i] !== arr2[j]) {
      ids.push(i)
      i++
    };
    i++
    j++
  }
  return ids
};

function ExcludedWords (arr, ids) {
  const excludedWords = []
  ids.forEach(id => excludedWords.push(arr[id]))
  return excludedWords
};

const wordsToExclude = storyWords.filter(word => {
  return unnecessaryWords.includes(word)
})

console.log(isEqual(wordsToExclude, ExcludedWords(storyWords, getDiffIds(storyWords, betterWords))))
// return true
// task seems completed succesfully




// function countOverusedWords(arr1, words) {
//   const array
  
// }
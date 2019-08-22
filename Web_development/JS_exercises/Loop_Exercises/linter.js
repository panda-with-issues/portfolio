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

console.log(isEqual(storyWords, betterWords))
// false

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
// returns true
// task seems completed successfully

/*
* There is an array of words called overusedWords. These are words overused in this story. You want to let the user of your program know how many times they have used these overused words.
*/

function countOverusedWords(arr, words) {
  // create an array of array in which every type of overused words will be stored, e.g. [[really], [very, very, very], []]
  const result = []
  words.forEach(word => result.push([]))
  // loop through text to fill nested arrays based on word's index in overusedWords
  arr.forEach(word => {
    if (overusedWords.includes(word)) {
      let idx = overusedWords.indexOf(word)
      result[idx].push(word)
    }
  })
  // pair every word to its count and log to console
  result.forEach(arr => {
    idx = result.indexOf(arr)
    console.log(`"${overusedWords[idx]}" has been used ${arr.length} times.`);
  })
};

countOverusedWords(betterWords, overusedWords)
// returns really: 2, very: 5, basically: 1

//follow several tests
const really = betterWords.filter(word => word === 'really')
const very = betterWords.filter(word => word === 'very')
const basically = betterWords.filter(word => word === 'basically')
console.log(really.length, very.length, basically.length)
// returns 2, 5, 1
// task seems to be completed successfully

/*
* Now, count how many sentences are in the paragraph.
*/

function getSentenceCount (arr) {
  let count = 0
  betterWords.forEach(word => {
    if (word[word.length - 1] === '.' || word[word.length - 1] === '!' || word[word.length - 1] === '?') {
      count++
    }
  })
  return count
}

console.log(getSentenceCount(betterWords))
// returns 12

//test function
function getPunctuation (str) {
  const characters = str.split('')
  const punctuation = characters.filter(char => {
    return char === '.' || char === '!' || char === '?'
  })
  return punctuation.length
}

console.log(getPunctuation(story));
// returns 12
//task seems completed successfully

/*
* Log these items to the console:
*
* - The word count
* - The sentence count
* - The number of times each overused word appears
*/

function logInfos () {
  console.log('Words used: ' + betterWords.length)
  console.log('Sentence number: ', getSentenceCount(betterWords))
  countOverusedWords(betterWords, overusedWords)  
};

logInfos()
// task completed

/*
* Now, log the betterWords array to the console as a single string.
*/

console.log(betterWords.join(' '))

/*
* Challenge task: write a function that finds the word that appears the greatest number of times.
*/

function getMostUsedWord (arr) {
  let mostUsedWord
  let max = 0
  const checked = []
  arr.forEach(word => {
    if (!checked.includes(word)) {
      checked.push(word)
      let count = 0
      for (let i = 0; i < arr.length; i++) {
        if (word === arr[i]) {
          count++
        }
      }
      if (count > max) {
        max = count
        mostUsedWord = word
      }
    }
  })
  return mostUsedWord
}

console.log('Most used word is "' + getMostUsedWord(betterWords) + '"')
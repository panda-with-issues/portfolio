/*
* This project is provided by codecademy.com
*/

const MessageMixer = {
  countCharacter (inputString, inputCharacter) {
    let count = 0
    const string = inputString.toLowerCase()
    const character = inputCharacter.toLowerCase()
    for (let i = 0; i < string.length; i++) {
      if (string[i] === character) {
        count++
      }
    }
    return count
  },
  capitalizeFirstCharacterOfWords (string) {
    const arr = string.split(' ')
    for (let i = 0; i < arr.length; i++) {
      const word = arr[i]
      arr[i] = word[0].toUpperCase() + word.substring(1)
    }
    return arr.join(' ')
  },
  reverseWord (word) {
    return word.split('').reverse().join('')
  },
  reverseAllWords (sentence) {
    const words = sentence.split(' ')
    for (let i = 0; i < words.length; i++) {
      words[i] = this.reverseWord(words[i])
    }
    return words.join(' ')
  },
  replaceFirstOccurence (string, toBeReplaced, replaceWith) {
    return string.replace(toBeReplaced, replaceWith)
  },
  replaceAllOccurrences (string, toBeReplaced, replaceWith) {
    return string.split(toBeReplaced).join(replaceWith)
  },
  encode (string) {
    const replacementObject = { a: '@', s: '$', i: '!', o: '0' }
    for (const key in replacementObject) {
      string = this.replaceAllOccurrences(string, key, replacementObject[key])
    }
    return string
  },
  palindrome (str) {
    const palindrome = str + ' ' + this.reverseWord(str)
    return palindrome
  },
  pigLatin (sentence, character) {
    sentence += ' '
    return sentence.split(' ').join(character + ' ')
  }
}

module.exports = MessageMixer

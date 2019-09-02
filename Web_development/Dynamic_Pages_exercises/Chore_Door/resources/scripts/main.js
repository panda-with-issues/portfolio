// global variables
const door1 = document.getElementById('door1')
const door2 = document.getElementById('door2')
const door3 = document.getElementById('door3')
const startButton = document.getElementById('start')
const botPath = 'resources/imgs/bot.svg'
const beachPath = 'resources/imgs/beach.svg'
const spacePath = 'resources/imgs/space.svg'
const closedPath = '../imgs/closed_door.svg'

let numClosedDoors = 3
let openDoor1
let openDoor2
let openDoor3
let currentlyPlaying = true

const isClicked = door => {
  if (door.src === closedPath) {
    console.log('false')
    return false
  }
  console.log('true')
  return true
}
const isBot = door => {
  if (door.src === botPath) {
    return true
  }
  return false
}

function gameOver (status) {
  if (status === 'win') {
    startButton.innerHTML = 'You win! Play again?'
  } else {
    startButton.innerHTML = 'Game Over! Play again?'
  }
  currentlyPlaying = false
}
function playDoor (door) {
  numClosedDoors--
  if (numClosedDoors === 0) {
    gameOver('win')
  } else if (isBot(door)) {
    gameOver()
  }
}
function randomChoreDoorGenerator () {
  const choreDoor = Math.floor(Math.random() * numClosedDoors)
  switch (choreDoor) {
    case 0:
      openDoor1 = botPath
      openDoor2 = spacePath
      openDoor3 = beachPath
      break
    case 1:
      openDoor1 = beachPath
      openDoor2 = botPath
      openDoor3 = spacePath
      break
    case 2:
      openDoor1 = spacePath
      openDoor2 = beachPath
      openDoor3 = botPath
  }
}
function startRound () {
  door1.src = closedPath
  door2.src = closedPath
  door3.src = closedPath
  startButton.innerHTML = 'Good luck!'
  currentlyPlaying = true
  randomChoreDoorGenerator()
}

// animate doors
door1.onclick = () => {
  if (currentlyPlaying && !isClicked(door1)) {
    door1.src = openDoor1
    playDoor(door1)
  }
}
door2.onclick = () => {
  if (currentlyPlaying && !isClicked(door2)) {
    door2.src = openDoor2
    playDoor(door2)
  }
}
door3.onclick = () => {
  if (currentlyPlaying && !isClicked(door3)) {
    door3.src = openDoor3
    playDoor(door3)
  }
}

// reset game
startButton.onclick = () => {
  if (!currentlyPlaying) {
    startRound()
  }
}

startRound()
console.log(isClicked(door1))

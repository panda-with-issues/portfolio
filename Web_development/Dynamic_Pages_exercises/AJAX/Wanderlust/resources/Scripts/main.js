import keys from './api_keys.js'
import cities from '../database/city_list.js'

// Intanciate new errors
const RequestFailedE = new Error('Request failed') // this will be thrown if an API request is rejected

// get page information
const submitButton = document.getElementById('submit-button')
const inputField = document.getElementById('destination-field')

// Handlebars.js context
const context = {
  locations: [],
  days: []
}

// helper functions

function getDestination () {
  // sanitize user input
  const input = inputField.value.trim()
  const sanitizedInput = input[0].toUpperCase() + input.slice(1)
  return sanitizedInput
}

function formatTime (dateStr) {
  // takes the time infos by the string date given by OpenWeather JSON response and format it in user friendly layout
  const time = parseInt(dateStr.split(' ')[1].slice(0, 2), 10)
  const timeFormatted = `${time}:00 - ${time + 3}:00`
  return timeFormatted
}

function formatDate (dateStr) {
  // takes the date by the string date given by OpenWeather JSON response and format it in user friendly layout
  const date = dateStr.split(' ')[0].split('-').reverse()
  switch (date[1]) {
    case '01':
      date.splice(1, 1, 'January')
      break
    case '02':
      date.splice(1, 1, 'February')
      break
    case '03':
      date.splice(1, 1, 'March')
      break
    case '04':
      date.splice(1, 1, 'April')
      break
    case '05':
      date.splice(1, 1, 'May')
      break
    case '06':
      date.splice(1, 1, 'June')
      break
    case '07':
      date.splice(1, 1, 'July')
      break
    case '08':
      date.splice(1, 1, 'August')
      break
    case '09':
      date.splice(1, 1, 'September')
      break
    case '10':
      date.splice(1, 1, 'October')
      break
    case '11':
      date.splice(1, 1, 'November')
      break
    case '12':
      date.splice(1, 1, 'December')
      break
  }
  const dateFormatted = date.join(' ')
  return dateFormatted
}

function renderData () {
  // boiler plate code for handlebars.js
  const source = document.getElementById('handlebars').innerHTML
  const template = Handlebars.compile(source)
  const compiledHtml = template(context)
  document.getElementById('hb-container').innerHTML = compiledHtml
}

// AJAX
async function getVenues () {
  // make a GET request to Foursquare API to obtain interesting place near the destination variable
  // Foursquare informations
  const endpoint = 'https://api.foursquare.com/v2/venues/explore' // this API lets you find interesting places near a given place
  const version = '&v=20190911' // required param to resolve the request. It points to the API version utilised. Format is YYYYMMDD. See Foursquare documentation under Versioning
  const queryKey = '&near='
  const limit = '&limit=5' // return up to five venues
  const grayBG = 'bg_' // sets the icon backgrond color to gray. Must be set before FSIconSize
  const iconSize = '64'
  const destination = getDestination()
  const url = endpoint + keys.FSClientId + keys.FSSecret + version + queryKey + destination + limit
  // fetch data
  try {
    const response = await fetch(url)
    if (response.ok) {
      const jsonResponse = await response.json()
      const venues = jsonResponse.response.groups[0].items.map(element => element.venue)
      // populate context with fetched data
      context.destination = destination
      venues.forEach(venue => {
        const venueObj = {}
        venueObj.name = venue.name
        venueObj.address = venue.location.address
        const icon = venue.categories[0].icon
        venueObj.icon = icon.prefix + grayBG + iconSize + icon.suffix
        context.locations.push(venueObj)
      })
    } else {
      throw RequestFailedE
    }
  } catch (e) {
    console.log(e)
  }
}

async function getWeather () {
  // make a GET request to obtain current weather at the given destination
  // OpenWeather informations
  const endpoint = 'https://api.openweathermap.org/data/2.5/forecast' // this API lets you see what'll the weather be like in that location in next five days
  const queryKey = '&q='
  const celsius = '&units=metric' // set results in celsius degrees
  const destination = getDestination()
  // retrieve country code
  let queryString
  for (let i = 0; i < cities.length; i++) {
    if (cities[i].name === destination) {
      const countryKey = cities[i].country
      queryString = queryKey + destination + ',' + countryKey
      break
    }
  }
  const url = endpoint + keys.OWAppId + queryString + celsius
  // fetch data
  try {
    const response = await fetch(url)
    if (response.ok) {
      const jsonResponse = await response.json()
      const days = jsonResponse.list.filter(element => jsonResponse.list.indexOf(element) % 8 === 0)
      console.log(days)
      // populate context with fetched data
      days.forEach(day => {
        const dayObj = {}
        dayObj.date = formatDate(day.dt_txt)
        dayObj.time = formatTime(day.dt_txt)
        dayObj.temperature = Math.round(day.main.temp)
        dayObj.humidity = day.main.humidity
        const weather = day.weather[0]
        dayObj.weather = weather.description
        dayObj.icon = weather.icon
        context.days.push(dayObj)
      })
    } else {
      throw RequestFailedE
    }
  } catch (e) {
    console.log(e)
  }
}

// execute functions
function search () {
  // reset context in case of second search
  if (context.locations.length || context.days.length) {
    context.locations = []
    context.days = []
  }
  Promise.all([getVenues(), getWeather()]).then(renderData)
  inputField.value = ''
}

submitButton.onclick = (e) => {
  // this lets the search starts either with a click either with pressing enter
  e.preventDefault()
  search()
}

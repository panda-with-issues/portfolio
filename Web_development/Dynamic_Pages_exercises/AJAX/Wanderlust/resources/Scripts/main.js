import keys from './api_keys.js'

// Intanciate new errors
const RequestFailedE = new Error('Request failed') // this will be thrown if an API request is rejected

// get page information
const submitButton = document.getElementById('submit-button')
const input = document.getElementById('destination-field')

// Handlebars.js context
const context = {
  locations: []
}

// Foursquare informations
const FSEndpoint = 'https://api.foursquare.com/v2/venues/explore' // this API lets you find interesting places near a given place
const version = '&v=20190911' // required param to resolve the request. It points to the API version utilised. Format is YYYYMMDD. See Foursquare documentation under Versioning
const FSQueryKey = '&near='
const limit = '&limit=5' // return up to five venues
const FSGrayBG = 'bg_' // sets the icon backgrond color to gray. Must be set before FSIconSize
const FSIconSize = '64'

// APIXU informations
const APIXUEndpoint = 'http://api.weatherstack.com/current' // this API lets you see what's theweather like in that location
const APIXUQueryKey = '&query='

// AJAX
async function getVenues () {
  // make a GET request to Foursquare API to obtain interesting place near the destination variable
  const destination = input.value
  const url = FSEndpoint + keys.FSClientId + keys.FSSecret + version + FSQueryKey + destination + limit
  try {
    const response = await fetch(url)
    if (response.ok) {
      const jsonResponse = await response.json()
      const venues = jsonResponse.response.groups[0].items.map(element => element.venue)
      // populating context with fetched data
      context.destination = destination
      venues.forEach(venue => {
        const venueObj = {}
        venueObj.name = venue.name
        venueObj.address = venue.location.address
        const icon = venue.categories[0].icon
        venueObj.icon = icon.prefix + FSGrayBG + FSIconSize + icon.suffix
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
  const url = APIXUEndpoint + keys.APIXUKey + APIXUQueryKey + destination
  try {
    const response = await fetch(url)
    if (response.ok) {
      const jsonResponse = await response.json()
      const weather = jsonResponse.current
      return weather
    }
    throw RequestFailedE
  } catch (e) {
    console.log(e)
  }
}

function renderVenues () {
  // boiler plate code for handlebars.js that render location data
  const source = document.getElementById('handlebars').innerHTML
  const template = Handlebars.compile(source)
  const compiledHtml = template(context)
  document.getElementById('hb-container').innerHTML = compiledHtml
}

// execute functions
function search () {
  // reset context in case of second search
  if (context.locations.length) {
    context.locations = []
  }
  getVenues().then(renderVenues)
}

submitButton.onclick = (e) => {
  // this lets the search starts either with a click either with pressing enter
  e.preventDefault()
  search()
}

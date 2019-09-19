import keys from './api_keys.js'

// get page information
const destination = document.getElementById('destination').value
const submitButton = document.getElementById('submit-button')

// Foursquare informations
const FSEndpoint = 'https://api.foursquare.com/v2/venues/explore' // this API lets you find interesting places near a given place
const version = '&v=20190911' // required param to resolve the request. It points to the API version utilised. Format is YYYYMMDD. See Foursquare documentation under Versioning
const FSQueryKey = '&near='
const limit = '&limit=5' // return up to five venues

// APIXU informations
const APIXUEndpoint = 'http://api.weatherstack.com/forecast' // this API lets you see what'll the weather be like in up to 14 days in the future
const APIXUQueryKey = '&query='
const APIXULang = '&language=it' // display results in italian

// AJAX
async function getVenues () {
  // make a GET request to Foursquare API to obtain interesting place near the destination variable
  const url = FSEndpoint + keys.FSClientId + keys.FSSecret + version + FSQueryKey + destination + limit
  try {
    const response = await fetch(url)
    if (response.ok) {
      const JsonResponse = await response.json()
      const venues = JsonResponse.response.groups[0].items.map(element => element.venue)
      return venues
    }
    throw new Error('Request failed')
  } catch (e) {
    console.log(e)
  }
}

// execute functions
submitButton.onclick = getVenues

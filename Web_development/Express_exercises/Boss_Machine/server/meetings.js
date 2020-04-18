const express = require('express')
const db = require('./db')

const meetings = express.Router()

meetings.get('/', (req, res) => {
  const allMeetings = db.getAllFromDatabase('meetings')
  res.send(allMeetings)
})

meetings.post('/', (req, res) => {
  const newMeeting = db.createMeeting()
  db.addToDatabase('meetings', newMeeting)
  res.status(201).send(newMeeting)
})

meetings.delete('/', (req, res) => {
  db.deleteAllFromDatabase('meetings')
  res.status(204).send()
})

module.exports = meetings

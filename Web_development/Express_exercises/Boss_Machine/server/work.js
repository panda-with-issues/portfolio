const express = require('express')
const db = require('./db')

const work = express.Router({ mergeParams: true })

function validateHours (req, res, next) {
  const hours = Number(req.body.hours)
  if (hours > 0) {
    req.hours = hours
    next()
  } else {
    res.status(400).send('Hours must be a positive number')
  }
}

function getMinionWorksById (minionId) {
  const allWorks = db.getAllFromDatabase('work')
  return allWorks.filter(work => work.minionId === minionId)
}

work.get('/', (req, res) => {
  const minionWork = getMinionWorksById(req.minionId)
  res.send(minionWork)
})

work.post('/', validateHours, (req, res, next) => {
  const infos = {
    title: req.body.title,
    description: req.body.description,
    hours: req.hours,
    minionId: req.minionId
  }
  const newWork = db.addToDatabase('work', infos)
  res.status(201).send(newWork)
})

work.param('workId', (req, res, next, id) => {
  const work = db.getFromDatabaseById('work', id)
  if (work) {
    req.work = work
    req.workId = id
    next()
  } else {
    res.status(404).send('Work not found')
  }
})

function validateWork (req, res, next) {
  const minionWorks = getMinionWorksById(req.minionId)
  if (minionWorks.some(work => work.id === req.workId)) {
    next()
  } else {
    res.status(400).send(`Minion ${req.minionId} hasn't got this work`)
  }
}

work.put('/:workId', validateHours, validateWork, (req, res) => {
  const newInfos = {
    id: req.workId,
    title: req.body.title,
    description: req.body.description,
    hours: req.hours,
    minionId: req.minionId
  }
  const updatedWork = db.updateInstanceInDatabase('work', newInfos)
  res.send(updatedWork)
})

work.delete('/:workId', validateWork, (req, res) => {
  db.deleteFromDatabaseById('work', req.workId)
  res.status(204).send()
})

module.exports = work

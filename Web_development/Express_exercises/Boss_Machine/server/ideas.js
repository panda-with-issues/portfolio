const express = require('express')
const db = require('./db')
const checkWorth = require('./checkMillionDollarIdea')
const ideas = express.Router()

function validateNum (numLiteral) {
  const num = Number(numLiteral)
  if (isNaN(num)) {
    return false
  }
  return num
}

function validateInputs (req, res, next) {
  const weeks = validateNum(req.body.numWeeks)
  const revenue = validateNum(req.body.weeklyRevenue)
  if (!weeks) {
    // 0 is not acceptable as well
    const err = new Error('Invalid number of weeks')
    err.status = 400
    next(err)
  } else if (!revenue) {
    const err = new Error('Invalid weekly revenue')
    err.status = 400
    next(err)
  } else {
    req.weeks = weeks
    req.revenue = revenue
    next()
  }
}

ideas.get('/', (req, res) => {
  const allIdeas = db.getAllFromDatabase('ideas')
  res.send(allIdeas)
})

ideas.post('/', validateInputs, checkWorth, (req, res, next) => {
  const infos = {
    name: req.body.name,
    description: req.body.description,
    numWeeks: req.weeks,
    weeklyRevenue: req.revenue
  }
  try {
    const newIdea = db.addToDatabase('ideas', infos)
    res.status(201).send(newIdea)
  } catch (e) {
    next(e)
  }
})

ideas.param('ideaId', (req, res, next, id) => {
  const idea = db.getFromDatabaseById('ideas', id)
  if (idea) {
    req.ideaId = id
    req.idea = idea
    next()
  } else {
    const err = new Error('Invalid ID')
    err.status = 404
    next(err)
  }
})

ideas.get('/:ideaId', (req, res, next) => {
  res.send(req.idea)
})

ideas.put('/:ideaId', validateInputs, checkWorth, (req, res, next) => {
  const newInfos = {
    id: req.ideaId,
    name: req.body.name,
    description: req.body.description,
    numWeeks: req.weeks,
    weeklyRevenue: req.revenue
  }
  try {
    const updatedIdea = db.updateInstanceInDatabase('ideas', newInfos)
    res.send(updatedIdea)
  } catch (e) {
    e.status = 400
    next(e)
  }
})

ideas.delete('/:ideaId', (req, res, next) => {
  db.deleteFromDatabaseById('ideas', req.ideaId)
  res.status(204).send()
})

module.exports = ideas

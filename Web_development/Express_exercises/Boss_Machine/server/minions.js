const express = require('express')
const db = require('./db')
const minions = express.Router()

minions.get('/', (req, res, next) => {
  const allMinions = db.getAllFromDatabase('minions')
  res.send(allMinions)
})

function validateSalary (req, res, next) {
  const stringSalary = req.body.salary
  try {
    const salary = Number(stringSalary)
    if (typeof salary === 'number') {
      req.salary = salary
      next()
    } else {
      const err = new Error('Invalid salary')
      err.status = 400
      next(err)
    }
  } catch (e) {
    next(e)
  }
}

minions.post('/', validateSalary, (req, res, next) => {
  try {
    const infos = {
      name: req.body.name,
      title: req.body.title,
      salary: req.salary,
      weaknesses: req.body.weaknesses
    }
    const minion = db.addToDatabase('minions', infos)
    if (minion) {
      res.status(201).send(minion)
    } else {
      const e = new Error('Bad Request')
      e.status = 400
      next(e)
    }
  } catch (e) {
    next(e)
  }
})

minions.param('id', (req, res, next, id) => {
  const minion = db.getFromDatabaseById('minions', req.params.id)
  if (minion) {
    req.id = id
    req.minion = minion
    next()
  } else {
    const err = new Error('Minion not found')
    err.status = 404
    next(err)
  }
})

minions.get('/:id', (req, res, next) => {
  res.send(req.minion)
})

minions.put('/:id', validateSalary, (req, res, next) => {
  const newInfos = {
    id: req.id,
    name: req.body.name,
    title: req.body.title,
    salary: req.salary,
    weaknesses: req.body.weaknesses
  }
  try {
    const minion = db.updateInstanceInDatabase('minions', newInfos)
    res.send(minion)
  } catch (e) {
    next(e)
  }
})

minions.delete('/:id', (req, res, next) => {
  db.deleteFromDatabaseById('minions', req.id)
  res.status(204).send()
})

module.exports = minions

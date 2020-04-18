const express = require('express');
const minionsRouter = require('./minions')
const ideasRouter = require('./ideas')
const meetingsRouter = require('./meetings')
const workRouter = require('./work')

const apiRouter = express.Router()

apiRouter.use('/minions', minionsRouter)
minionsRouter.use('/:minionId/work', workRouter)
apiRouter.use('/ideas', ideasRouter)
apiRouter.use('/meetings', meetingsRouter)

module.exports = apiRouter

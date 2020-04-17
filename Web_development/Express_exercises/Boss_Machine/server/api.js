const express = require('express');
const minionsRouter = require('./minions')
const apiRouter = express.Router();

apiRouter.use('/minions', minionsRouter)


module.exports = apiRouter;

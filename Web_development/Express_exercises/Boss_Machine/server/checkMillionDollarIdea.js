const checkMillionDollarIdea = (req, res, next) => {
  if (req.weeks * req.revenue < 1000 * 1000) {
    const err = new Error('This idea is not worth 1,000,000 $')
    err.status = 400
    next(err)
  } else {
    next()
  }
};

// Leave this exports assignment so that the function can be used elsewhere
module.exports = checkMillionDollarIdea;

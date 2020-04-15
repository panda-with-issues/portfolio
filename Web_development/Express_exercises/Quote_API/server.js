const express = require('express');
const app = express();

const { quotes } = require('./data');
const { getRandomElement } = require('./utils');

const PORT = process.env.PORT || 4001;

app.use(express.static('public'));

app.get('/api/quotes/random', (req, res) => {
  const el = getRandomElement(quotes)
  res.send({ quote: el })
})

app.get('/api/quotes', (req, res) => {
  const author = req.query.person
  if (author) {
    const responseArr = quotes.filter(quote => quote.person === author)
    res.send({ quotes: responseArr })
  } else {
    res.send({ quotes: quotes })
  }
})

app.post('/api/quotes', (req, res) => {
  const quote = req.query.quote
  const person = req.query.person
  if (quote && person) {
    const newQuote = {
      quote,
      person
    }
    quotes.push(newQuote)
    res.status(201).send({ quote: newQuote })
  }
  res.status(400).send()
})

app.listen(PORT, () => console.log(`Listening on port ${PORT}`))

# fasttext-native

> fastText native bindings for ⬡.js

[![npm](https://img.shields.io/npm/v/fasttext-native.svg?style=flat-square)](https://npm.im/fasttext-native)
[![Travis](https://img.shields.io/travis/tuananh/fasttext-native/develop.svg?label=Linux%20%26%20macOS%20build&style=flat-square)](https://travis-ci.org/tuananh/fasttext-native)
[![David](https://img.shields.io/david/tuananh/fasttext-native.svg?style=flat-square)](https://david-dm.org/tuananh/fasttext-native)

Forked from [pragonauts's fast-text](https://github.com/pragonauts/fast-text)

## Features

- Executing prediction models
- Searching nearest neighbour
- Prebuilt binaries for Linux and macOS (Windows is not supported by fastText)
- Tracking latest fastText upstream version (currently version 0.1.0)

## Usage

### Prediction

There is a simple class for executing prediction models:

```javascript
const path = require('path')
const { Classifier } = require('fasttext-native')

const model = path.resolve(__dirname, './classification.bin')

const classifier = new Classifier(model)

classifier.predict('how it works', 1, (err, res) => {
  if (err) {
    console.error(err)
  } else if (res.length > 0) {
    const tag = res[0].label // __label__someTag
    const score = res[0].valuel // 1.3455345
  } else {
    console.log('No matches')
  }
})
```


### Nearest neighbour

There is a simple class for searching nearest neighbours:

```javascript
const path = require('path')
const { Query } = require('fasttext-native')

const model = path.resolve(__dirname, './skipgram.bin')

const query = new Query(model)

query.nn('word', 10, (err, res) => {
  if (err) {
    console.error(err)
  } else if (res.length > 0) {
    const tag = res[0].label // letter
    const score = res[0].valuel // 0.99992
  } else {
    console.log('No matches')
  }
})
```
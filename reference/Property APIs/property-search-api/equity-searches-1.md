---
title: Equity Searches
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
There are a few different ways to narrow down properties based on different Equity Requirements. 

### Home Equity Value Search:

* estimated\_equity
* equity\_operator

```
//Find properties with less than 250,000 in equity
let request = {
  size: 250,
  city: 'Arlington',
  state: 'VA',
  estimated_equity: 250000,
  equity_operator: 'lt'
}
```

### Home Owner Equity Percent Search:

* equity\_percent
* equity\_percent\_operator

```
//Find properties with greater than 75% equity
let request = {
  size: 250,
  city: 'Arlington',
  state: 'VA',
  equity_percent: 75,
  equity_percent_operator: 'gt'
}
```

### Equity Flags

There are also a couple equity based flags: negative\_equity & high\_equity.

negative\_equity: true is equivalent to estimated\_equity \< 0

high\_equity: true is equivalent to equity\_percent > 70

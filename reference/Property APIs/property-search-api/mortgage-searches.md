---
title: Mortgage Searches
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
### Mortgage Range Search

```
let request = {
 	size: 200,
  city: 'Arlington',
  state: 'VA',
  mortgage_min: 200000,
  mortgage_max: 400000
}
```

### Free & Clear

```
//find properties with no open mortgage balance
let request = {
 size: 100,
 free_clear: true
}
```

### Open Mortgage Balance

```
(coming soon...)
```

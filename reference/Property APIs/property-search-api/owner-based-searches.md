---
title: Owner Based Searches
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
### Absentee Owner Searches

```
let request = {
  size: 100,
  absentee_owner: true
}
```

### In State Owner Searches

```
let request = {
  size: 100,
  in_state_owner: true
	state: 'VA'
}
```

### Out of State Owner Searches

```
let request = {
  size: 100,
  out_of_state_owner: true,
	city: 'Virginia Beach',
  state: 'VA'
}
```

### Years Owned Searches

```
let request = {
 	size: 100,
  years_owned_min: 5,
  years_owned_max: 10
}
```

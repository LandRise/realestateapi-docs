---
title: Search Radius Example
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
There are only a few key components to performing your first Property Search based on Current Location or some other arbitrary geo-point in the US.

You'll need:

* latitude (double/float or string representation thereof)
* longitude (double/float or string representation thereof)
* radius (between 0.1-10 \[in miles])

```
//Find 250 properties within 5 miles of point provided
//that have 2-4 beds, 2-5 baths, and more than 250,000 in homeequity
let request = {
  size: 250,
  latitude: "-86.32762085355883",
  longitude: "35.42300740560803",
  radius: 5,
  beds_min: 2,
  beds_max: 4,
  baths_min: 2,
  baths_max: 5,
  equity: 250000,
  equity_comparison: "lt"
}
```

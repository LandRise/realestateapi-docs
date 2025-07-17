---
title: Building Characteristics Searches
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
You can filter for properties based on the following building characteristics:

* beds
* baths
* building size
* rooms
* stories
* units
* year built

```
//beds - in # of rooms
let request = {
  size: 100,
  beds_min: 2,
  beds_max: 4
}

//baths - in # of rooms
let request = {
  size: 100,
  baths_min: 3,
  baths_max: 5
}


//building size - in sq. ft.
let request = {
  size: 100,
  building_size_min: 1250,
  building_size_max: 2000
}


//rooms
let request = {
  size: 100,
  rooms_min: 6,
  rooms_max: 10
}

//stories
let request = {
  size: 100,
  stories_min: 2,
  stories_max: 4
}


//units 
//can be used in conjunction with MFH search param 'mfh_5plus' to build a range
let request = {
  size: 100,
  units_min: 7,
  units_max: 12
}

//year built
let request = {
 size: 100,
 year_min: 1980,
 year_max: 2000
}







```

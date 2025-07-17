---
title: .schools
excerpt: Find nearby schools for your subject property
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Coverage

* Over 25,000 schools represented nationwide (incl. Public & Charter)
* School info provided for over 30M properties
* ".schools" includes an array of schools across grade levels

## School Location

* each school has its own geo-point (latitude/longitude) with the "location" field for you to plot it's location & distance relative to your property's "propertyInfo.latitude" and "propertyInfo.longitude"
* you'll also receive the street address, city, state, and zip of the school

## School Ratings

* Scale for ratings: 1-10 (1 is the worst, 10 is the best)

## School Grades & Level

* use the ".level" object to see what official classification the school falls under:
  * preschool
  * elementary
  * middle
  * high
* since some places assign different grades to different classifications (e.g. 5th grade in elementary vs. middle), you can use the ".grades" to see the exact range

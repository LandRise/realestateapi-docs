---
title: Daily Jobs for Newly Listed Properties
excerpt: >-
  Find listings based on the date of the initial listing on the MLS. Dates must
  be in YYYY-MM-DD format.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Use Case: Grab all New Listings Nationwide Every Day

Current Date: April 2, 2025

Goal: Update your listing database with the newest listed properties nationwide

Assumptions: You want to add any new listings to your local side so you can keep up with new inventory and set those properties up to be updated later as updates stream in through one of the other daily jobs

```
let input = {
  count: true
  listing_date_min: "2025-04-01",
  listing_date_max: "2025-04-01"
}

// 30,556 RESULTS
// requires 30,556 / 250 (max size) = 123 MLS Search API calls
// ~100ms / api call * 123 MLS Search API calls = 12.3 seconds

{
  size: 250,
  listing_date_min: "2025-04-01",
  listing_date_max: "2025-04-01"
}

{
  size: 250, 
  listing_date_min: "2025-04-01",
  listing_date_max: "2025-04-01",
  resultIndex: 250
}

{
  size: 250, //379 - 250 = 129
  listing_date_min: "2025-04-01",
  listing_date_max: "2025-04-01",
  resultIndex: 500
}


```

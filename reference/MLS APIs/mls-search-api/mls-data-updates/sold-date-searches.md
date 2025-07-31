---
title: Daily Jobs for Sold Listings
excerpt: >-
  Find recently sold (or historical) listings by filtering on the date they were
  reported sold to the MLS
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Use Case: Track Newly Sold Listings

Current Date: April 2, 2025

Goal: Grab all newly sold listings nationwide from yesterday

Assumptions: You are already tracking all status: "Pending" properties to see when they close

```
{
  count: true
  sold_date_min: "2025-04-01",
  sold_date_max: "2025-04-01"
}

// 2,741 RESULTS
// requires 2,741 / 250 (max size) = 11 MLS Search API calls
// ~100ms / api call * 11 = 1.1 seconds for daily job to grab solds

{
  size: 250,
  sold_date_min: "2025-04-01",
  sold_date_max: "2025-04-01"
}

{
  size: 250, 
  sold_date_min: "2025-04-01",
  sold_date_max: "2025-04-01",
  resultIndex: 250
}

{
  size: 250, //379 - 250 = 129
  sold_date_min: "2025-04-01",
  sold_date_max: "2025-04-01",
  resultIndex: 500
}

//....etc

//Update your listing records to "Sold" based on the listing_id's received in the responses from these MLS Search API calls


```

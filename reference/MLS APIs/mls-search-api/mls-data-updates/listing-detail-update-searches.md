---
title: Daily Jobs for Any Listing Updates
excerpt: Detect listings with any changes using the modification timestamp filters
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Use Case: Get All Updated Listings Every Day

Current Date: April 2, 2025

Goal: Pull all of the updated listings from yesterday - April 1, 2025

Assumptions: You have already completed a large initial load job and have the listing\_id's for everything you have pulled/care about. You will compare the records/listing\_id's you pull in this code to what you already have cached and update the relevant records on your side.

```
let input = {
  size: 250,
  modification_timestamp_min: "2025-04-01",
  modification_timestamp_max: "2025-04-02"
}

//-OR-//

//use "city", "mls_board_code", "zip", or other geo filters to prioritize your updates
let input = {
  city: "Richmond",
  state: "VA",
  modification_timestamp_min: "2025-04-01",
  modification_timestamp_max: "2025-04-02"
}



//process results and get all the listing_id's in an array
//compare to each listing ID you already have cached to see which ones need updating
//you may need to perform paging to get all results

//Get count of how many need to be updated
{
  count: true,
  modification_timestamp_min: "2025-04-01",
  modification_timestamp_max: "2025-04-02"
}

// 190,691 RESULTS
// requires 190,691 / 250 (max size) = 763 MLS Search API calls
// ~100ms per request = 76.3 second job time = 1.27 mins

//Pagination Flow of Queries 
{
  size: 250,
  modification_timestamp_min: "2025-04-01",
  modification_timestamp_max: "2025-04-02"
}

{
  size: 250,
  modification_timestamp_min: "2025-04-01",
  modification_timestamp_max: "2025-04-02",
  resultIndex: 250
}

{
  size: 250,
  modification_timestamp_min: "2025-04-01",
  modification_timestamp_max: "2025-04-02",
  resultIndex: 500
}

//....etc

```

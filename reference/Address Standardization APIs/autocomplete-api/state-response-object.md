---
title: ("T") State Completion
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
You can perform an AutoComplete search over an entire state.

You'll get suggestions of the other search types in your results as well as the main state listing with searchType: "T"

Here's an example:

```
{
  "input": {
    "search": "Virginia"
  },
  "data": [
    {
      "state": "VA",
      "stateName": "Virginia",
      "searchType": "T",
      "title": "Virginia, USA"
    },
    {
      "state": "VA",
      "stateId": "51",
      "county": "Virginia Beach City",
      "countyId": "810",
      "searchType": "N",
      "fips": "51810",
      "title": "Virginia Beach City, VA"
    },
    {
      "state": "MN",
      "city": "Virginia",
      "searchType": "C",
      "title": "Virginia, MN"
    },
    {
      "state": "IL",
      "city": "Virginia",
      "searchType": "C",
      "title": "Virginia, IL"
    },
    {
      "state": "NE",
      "city": "Virginia",
      "searchType": "C",
      "title": "Virginia, NE"
    },
    {
      "state": "VA",
      "city": "Virginia Beach",
      "searchType": "C",
      "title": "Virginia Beach, VA"
    },
    {
      "state": "MT",
      "city": "Virginia City",
      "searchType": "C",
      "title": "Virginia City, MT"
    },
    {
      "state": "NV",
      "city": "Virginia City",
      "searchType": "C",
      "title": "Virginia City, NV"
    },
    {
      "state": "CO",
      "city": "Virginia Dale",
      "searchType": "C",
      "title": "Virginia Dale, CO"
    },
    {
      "state": "FL",
      "city": "Virginia Gardens",
      "searchType": "C",
      "title": "Virginia Gardens, FL"
    }
  ],
  "totalResults": 8,
  "returnedResults": 10,
  "statusCode": 200,
  "statusMessage": "Success",
  "credits": 0,
  "live": true,
  "requestExecutionTimeMS": "22ms"
}
```

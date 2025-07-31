---
title: '"Pins" API Response Object'
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
* "data" \[array (of objects)] => contains all of the result pins
  * "id" - the unique property ID for a given pin; can be used as input to the Property Detail lookup for more details
  * "latitude"/"longitude" - will help you plot onto a Google Maps or Mapbox style map
* resultCount => number of result pins matching your query
* recordCount => number of records grabbed in most recent API call

```
{
  "input": {
    "size": 5,
    "city": "Richmond",
    "state": "VA"
  },
  "data": [
    {
      "id": 195701571,
      "latitude": 37.57515085410918,
      "longitude": -77.52410645803138
    },
    {
      "id": 193780115,
      "latitude": 37.58494796874613,
      "longitude": -77.44245515888888
    },
    {
      "id": 193779832,
      "latitude": 37.5559926318486,
      "longitude": -77.34033413202864
    },
    {
      "id": 193014839,
      "latitude": 37.605816086090535,
      "longitude": -77.43727523642104
    },
    {
      "id": 188347998,
      "latitude": 37.49381488798615,
      "longitude": -77.43899894964719
    }
  ],
  "resultCount": 101467,
  "resultIndex": 5,
  "recordCount": 5,
  "statusCode": 200,
  "statusMessage": "Success",
  "credits": 5,
  "requestExecutionTimeMS": "103ms"
}
```

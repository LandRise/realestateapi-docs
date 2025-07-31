---
title: ("G") Neighborhood Completion
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
The primary way of working with neighborhoods is by searching by the name of the neighborhood you are interested in. This is the sample response when using a neighborhood name as the search parameter input.

<Image align="center" src="https://files.readme.io/7a6010c-Screen_Shot_2023-12-01_at_3.43.09_AM.png" />

This can be used with the Property Search using the "neighborhood\_id", "search\_type", and "neighborhood\_name" fields.

```Text JSON
{
  "input": {
    "search": "Cherry Grove"
  },
  "data": [
    {
      "state": "NY",
      "city": "Cherry Grove",
      "searchType": "C",
      "title": "Cherry Grove, NY"
    },
    {
      "state": "SC",
      "city": "Cherry Grove Beach",
      "searchType": "C",
      "title": "Cherry Grove Beach, SC"
    },
    {
      "neighborhoodId": "94091",
      "neighborhoodName": "Cherry Grove",
      "neighborhoodType": "subdivision",
      "city": "Mechanicsville",
      "state": "VA",
      "zip": "23111",
      "title": "Cherry Grove, Mechanicsville, VA",
      "searchType": "G"
    },
    {
      "neighborhoodId": "122517",
      "neighborhoodName": "Cherry Grove",
      "neighborhoodType": "subdivision",
      "city": "Mooresville",
      "state": "NC",
      "zip": "28115",
      "title": "Cherry Grove, Mooresville, NC",
      "searchType": "G"
    },
    {
      "neighborhoodId": "130601",
      "neighborhoodName": "Cherry Grove",
      "neighborhoodType": "subdivision",
      "city": "Hickory",
      "state": "NC",
      "zip": "28602",
      "title": "Cherry Grove, Hickory, NC",
      "searchType": "G"
    },
    {
      "neighborhoodId": "145721",
      "neighborhoodName": "Cherry Grove",
      "neighborhoodType": "subdivision",
      "city": "North Myrtle Beach",
      "state": "SC",
      "zip": "29582",
      "title": "Cherry Grove, North Myrtle Beach, SC",
      "searchType": "G"
    },
    {
      "neighborhoodId": "283489",
      "neighborhoodName": "Cherry Grove",
      "neighborhoodType": "subdivision",
      "city": "Whites Creek",
      "state": "TN",
      "zip": "37189",
      "title": "Cherry Grove, Whites Creek, TN",
      "searchType": "G"
    },
    {
      "neighborhoodId": "302733",
      "neighborhoodName": "Cherry Grove",
      "neighborhoodType": "subdivision",
      "city": "Ecorse",
      "state": "MI",
      "zip": "48229",
      "title": "Cherry Grove, Ecorse, MI",
      "searchType": "G"
    },
    {
      "neighborhoodId": "225609",
      "neighborhoodName": "Cherry Grove",
      "neighborhoodType": "subdivision",
      "city": "Miami",
      "state": "FL",
      "zip": "33176",
      "title": "Cherry Grove, Miami, FL",
      "searchType": "G"
    },
    {
      "neighborhoodId": "283083",
      "neighborhoodName": "Cherry Grove",
      "neighborhoodType": "subdivision",
      "city": "Spring Hill",
      "state": "TN",
      "zip": "37174",
      "title": "Cherry Grove, Spring Hill, TN",
      "searchType": "G"
    }
  ],
  "totalResults": 12,
  "returnedResults": 10,
  "statusCode": 200,
  "statusMessage": "Success",
  "credits": 0,
  "live": true,
  "requestExecutionTimeMS": "20ms"
}
```

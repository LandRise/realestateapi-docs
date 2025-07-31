---
title: Error Handling for Property Detail API
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
# 400 Errors - Bad Request Errors

## General Errors

### No input/empty JSON specified

```
{
  "statusCode": 400,
  "error": "Bad Request",
  "message": "\"PropertyDetailRequest\" must contain at least one of [id, address, house, apn]",
  "validation": {
    "source": "payload",
    "keys": [
      ""
    ]
  }
}
```

<br />

<br />

## Possible Errors on "zip" Input Field

### Search by Address Parts - "Zip Left Off" Error

```
Input: 
{
  "house": "792",
  "street": "Valentines St",
  "city": "Gasburg",
  "state": "VA"
}

Error: 
{
  "statusCode": 400,
  "error": "Bad Request",
  "message": "\"house\" missing required peer \"zip\"",
  "validation": {
    "source": "payload",
    "keys": [
      ""
    ]
  }
}
```

### Search by Address Parts - "Invalid Zip" Error

```
{
  "statusCode": 400,
  "error": "Bad Request",
  "message": "\"zip\" length must be 5 characters long",
  "validation": {
    "source": "payload",
    "keys": [
      "zip"
    ]
  }
}
```

<br />

<br />

## Possible Errors on "state" Input Field

### Search by Address Parts - "State Left Off" Error

```
{
  "statusCode": 400,
  "error": "Bad Request",
  "message": "\"house\" missing required peer \"state\"",
  "validation": {
    "source": "payload",
    "keys": [
      ""
    ]
  }
}
```

<br />

### Search by Address Parts - "State Abbreviation Needed" Error

```
{
  "statusCode": 400,
  "error": "Bad Request",
  "message": "\"state\" length must be 2 characters long",
  "validation": {
    "source": "payload",
    "keys": [
      "state"
    ]
  }
}
```

<br />

<br />

# 404 Errors

### "Not Found"

* when the property address record is not found in our data set
* when the property ID for the lookup doesn't match a corresponding property record with that ID

```
// No result for addres
{
  "input": {
    "comps": false,
    "address": "722 Valentines Street, Gasburg, VA 23857"
  },
  "data": {},
  "statusCode": 404,
  "statusMessage": "Not Found",
  "live": true,
  "requestExecutionTimeMS": "34ms",
  "propertyLookupExecutionTimeMS": null,
  "compsLookupExecutionTimeMS": null
}

// No result for ID
{
  "input": {
    "comps": false,
    "id": 13252346234
  },
  "data": {},
  "statusCode": 404,
  "statusMessage": "Not Found",
  "live": true,
  "requestExecutionTimeMS": "14ms",
  "propertyLookupExecutionTimeMS": null,
  "compsLookupExecutionTimeMS": null
}
```

<br />

### "Street is not similar to found properties"

* from one of the following situations:
  * incorrect house number
  * street name off by >3-4 characters

```
{
  "input": {
    "comps": false,
    "house": "X",
    "street": "Valentines St",
    "city": "Gasburg",
    "state": "VA",
    "zip": "23857"
  },
  "data": {},
  "statusCode": 404,
  "statusMessage": "Not Found",
  "reason": "Street is not similar to found properties",
  "live": true,
  "requestExecutionTimeMS": "31ms",
  "propertyLookupExecutionTimeMS": null,
  "compsLookupExecutionTimeMS": null
}
```

---
title: Lender Grade AVM API Response Object
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
This endpoint returns an AVM range and a statistical confidence score of how reliable our algorithm has found the home valuation to be.

Note: the method of calculation of the Lender Grade AVMs are different than the calculation of the reapiAvm from the v3/PropertyComps endpoints. We find these valuations to be more precise and reliable in 99% of cases. One of the main areas where the Lender Grade AVMs are stronger are in outlier properties.

```text json
{  
  "input": {  
    "address": "17 Topeka Pass, Willingboro NJ 08046",  
    "strict": false  
  },  
  "data": {  
    "id": "700090303849",  
    "apn": "38  01121-0000-00004",  
    "fips": "34005",  
    "avm": "459000",  
    "avmMin": "339660",  
    "avmMax": "578340",  
    "confidence": "74",  
    "address": "17 Topeka Pass",  
    "city": "Willingboro",  
    "state": "NJ",  
    "zip": "8046",  
    "zip4": "4111",  
    "label": "17 Topeka Pass, Willingboro NJ 8046",  
    "lastUpdateDate": "2024-06-15T00:00:00.000Z"  
  },  
  "statusCode": 200,  
  "statusMessage": "Success",  
  "live": true,  
  "requestExecutionTimeMS": "1269ms"  
}
```

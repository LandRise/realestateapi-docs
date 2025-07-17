---
title: '"comps" Object Schema'
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
The v3/PropertyComps endpoint will return a list of comps that match your custom input parameters.

<br />

The schema of total fields available on the Property Comps endpoint is more limited than what is provided by the Property Detail endpoint, but you'll still find good high-level information for each of the comps.

<br />

```
{
      "id": "24721544",
      "distance": 1.95,
      "vacant": false,
      "absenteeOwner": false,
      "corporateOwned": false,
      "outOfStateAbsenteeOwner": false,
      "inStateAbsenteeOwner": false,
      "bedrooms": 4,
      "bathrooms": 2,
      "yearBuilt": "1978",
      "squareFeet": "2016",
      "estimatedValue": "1297000",
      "estimatedEquity": "844067",
      "equityPercent": "65",
      "openMortgageBalance": "480000",
      "estimatedMortgageBalance": "452933",
      "lastSaleDate": "2024-12-03",
      "lastSaleAmount": "0",
      "lotSquareFeet": "9888",
      "latitude": 38.89945020768596,
      "longitude": -77.14562140956144,
      "landUse": "Residential",
      "propertyType": "SFR",
      "owner1FirstName": "Graham M",
      "owner1LastName": "Curtis",
      "owner2FirstName": "Wendy B",
      "owner2LastName": "Curtis",
      "garageAvailable": true,
      "airConditioningAvailable": true,
      "preForeclosure": false,
      "cashBuyer": false,
      "privateLender": false,
      "zoning": "R-8",
      "censusTract": "100200",
      "congressionalDistrict": "08",
      "lenderName": "Ameris Bank",
      "address": {
        "zip": "22207",
        "city": "Arlington",
        "county": "Arlington County",
        "state": "VA",
        "street": "5707 27th Rd N",
        "address": "5707 27th Rd N, Arlington, VA 22207"
      },
      "mailAddress": {
        "zip": "22207",
        "city": "Arlington",
        "county": "Arlington County",
        "state": "VA",
        "street": "5707 27th Rd N",
        "address": "5707 27th Rd N, Arlington, VA 22207"
      },
      "age": 46
    }
```

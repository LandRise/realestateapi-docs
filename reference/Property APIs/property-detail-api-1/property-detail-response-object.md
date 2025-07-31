---
title: Property Detail Response Object
excerpt: >-
  Get a comprehensive look at all of the data points returned from a standard
  Property Detail response.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Root Level Fields

These data points are available directly on the root of the data object of the response from the property detail endpoint without needing to read through the nested objects or arrays of objects.

```
{
  "absenteeOwner": false,
  "auction": false,
  "cashBuyer": true,
  "cashSale": false,
  "corporateOwned": false,
  "death": false,
  "deathTransfer": false,
  "deedInLieu": false,
  "equity": null,
  "equityPercent": 100,
  "estimatedEquity": 697581,
  "estimatedMortgageBalance": "0",
  "estimatedMortgagePayment": "0",
  "estimatedValue": 697581,
  "floodZone": true,
  "floodZoneDescription": "AREA OF MINIMAL FLOOD HAZARD",
  "floodZoneType": "X",
  "freeClear": true,
  "highEquity": true,
  "id": 8195564,
  "inherited": false,
  "inStateAbsenteeOwner": false,
  "investorBuyer": false,
  "judgment": false,
  "lastSaleDate": "2012-10-12",
  "lastSalePrice": "200000",
  "lastUpdateDate": "2023-06-06 00:00:00 UTC",
  "lien": false,
  "MFH2to4": false,
  "MFH5plus": false,
  "mlsActive": false,
  "mlsCancelled": false,
  "mlsFailed": false,
  "mlsHasPhotos": false,
  "mlsPending": false,
  "mlsSold": false,
  "mobileHome": false,
  "openMortgageBalance": 0,
  "outOfStateAbsenteeOwner": false,
  "ownerOccupied": true,
  "preForeclosure": false,
  "priorId": null,
  "privateLender": false,
  "propertyType": "SFR",
  "quitClaim": false,
  "sheriffsDeed": false,
  "spousalDeath": false,
  "taxLien": false,
  "trusteeSale": false,
  "vacant": false,
  "warrantyDeed": false
}
  

```

### Auction Info

Will only be populated when "auction": true

```
 "auctionInfo": {
      "active": false,
      "auctionDate": "2025-01-30T00:00:00.000Z",
      "auctionStreetAddress": null,
      "auctionTime": "10:00X XM",
      "caseNumber": "000251-CV-2024",
      "defaultAmount": null,
      "documentType": "Notice of Foreclosure Sale",
      "estimatedBankValue": "494000",
      "foreclosureId": "23891658",
      "judgmentAmount": "438083",
      "judgmentDate": "2025-01-30T00:00:00.000Z",
      "lenderName": "METROPOLITAN LIFE INSURANCE CO",
      "lenderPhone": null,
      "noticeType": "FOR",
      "openingBid": "438083",
      "originalLoanAmount": "0",
      "recordingDate": "2024-11-15T00:00:00.000Z",
      "seqNo": 1,
      "trusteeAddress": null,
      "trusteeFullName": "MONROE COUNTY SHERIFF",
      "trusteePhone": null,
      "trusteeSaleNumber": null,
      "typeName": null
 },
```

<br />

### Current Mortgages

An array containing current mortgage data such as document date, interest rate, loan amount, loan type and lender information.

```
{
	"currentMortgages": [
		{
			"interestRate": 0,
			"documentDate": "2012-10-30T00:00:00.000Z",
			"amount": 129922,
			"loanType": "Refinance",
			"lenderName": "Citywide Mortgage Co",
			"deedType": "Conventional With Pmi",
			"recordingDate": "2012-10-30T00:00:00.000Z",
			"position": "First",
			"interestRateType": "Unknown",
			"seq": 0
		},
		...
	],
	...
}
```

### Demographics

```
 "demographics": {
      "fmrEfficiency": "1140",
      "fmrFourBedroom": "2120",
      "fmrOneBedroom": "1300",
      "fmrThreeBedroom": "1910",
      "fmrTwoBedroom": "1490",
      "fmrYear": "2023",
      "hudAreaCode": "METRO42140M42140",
      "hudAreaName": "Santa Fe, NM MSA",
      "medianIncome": "71468",
      "suggestedRent": "1910"
 }
```

### Foreclosure Info

An array containing details about foreclosure and pre-foreclosure documents.

```
{
	"foreclosureInfo": [
 		{
        "foreclosureId": "114870306",
        "originalLoanAmount": "41835",
        "estimatedBankValue": "68826",
        "defaultAmount": "0",
        "recordingDate": "2022-10-05",
        "openingBid": "0",
        "auctionDate": "2022-11-03",
        "auctionTime": "11:00 AM",
        "auctionStreetAddress": "Wayne County Courthouse, Detroit",
        "documentType": "Notice of Trustee Sale",
        "trusteeSaleNumber": "22MI00690-1",
        "typeName": "I",
        "active": true
      }
  ],
}
```

### Last Sale

```
"lastSale": {
      "armsLength": false,
      "buyerNames": "Hse Preservation Ptshp L Morey",
      "documentType": "Warranty Deed",
      "documentTypeCode": "DTWD",
      "downPayment": "0",
      "ltv": 0,
      "ownerIndividual": true,
      "priorOwnerIndividual": true,
      "priorOwnerMonthsOwned": "59",
      "purchaseMethod": "Cash Purchase",
      "recordingDate": "2011-03-21",
      "saleAmount": "0",
      "saleDate": "2011-03-08",
      "sellerNames": "Kozely,Peter",
      "seqNo": "0",
      "transactionType": "Transfer"
}
```

### Linked Properties

* visit: [https://developer.realestateapi.com/reference/linked-properties-of-owners](https://developer.realestateapi.com/reference/linked-properties-of-owners) to learn more

```
"linkedProperties": {
      "ids": [
        "219804253",
        "239902035",
        "210587175",
        "239902030",
        "220931651",
        "214930837"
      ],
      "totalEquity": "946758",
      "totalMortgageBalance": "246540",
      "totalOwned": "6",
      "totalValue": "1193298"
}
```

### Lot Info

An object that contains the property’s use description, property class, census tract, subdivision, legal description, lot size, lot number, land use type and APN.

```
"lotInfo": {
      "apn": "011279232",
      "apnUnformatted": "011279232",
      "censusBlock": "2012",
      "censusBlockGroup": "2",
      "censusTract": "10500",
      "landUse": "Residential",
      "legalDescription": "T17N R10E S29 .74 AC LOT 49 BLK 1 ;PM1-056-098-155-506",
      "legalSection": "29",
      "lotAcres": 0,
      "lotNumber": "49",
      "lotSquareFeet": 32234,
      "lotDepthFeet": null,
      "lotWidthFeet": null,
      "propertyClass": "The general use for the property is for residential purposes",
      "propertyUse": "Single Family Residence",
      "subdivision": "A",
      "zoning": null
}
```

### MLS History

An array showing MLS transaction history such as listed, pending and cancelled.

```
{
	"mlsHistory": [
  	{
        "propertyId": "18871883",
        "type": "single_family",
        "price": "525000",
        "beds": 3,
        "baths": 2.5,
        "daysOnMarket": "0",
        "agentName": "Bryan Goldman",
        "agentOffice": "Keller Williams Realty",
        "agentPhone": "3606933336",
        "status": "offmarket",
        "statusDate": "2022-05-13",
        "seqNo": "1"
      },
    	...
  ],
	
}
```

### Mortgage History

An array containing mortgage history for the property with details such as amount, recording date, maturity date, deed type, loan type and lender data.

```
"mortgageHistory": [
      {
        "amount": 920000,
        "deedType": "Warranty Deed",
        "documentDate": "2006-04-06T00:00:00.000Z",
        "granteeName": "Peter Kozely",
        "interestRate": null,
        "interestRateType": "Adjustable Rate",
        "lenderCode": "B",
        "lenderName": "Countrywide Bank",
        "lenderType": "Bank",
        "maturityDate": null,
        "mortgageId": "193432697",
        "open": false,
        "recordingDate": "2006-04-06T00:00:00.000Z",
        "seq": 0,
        "transactionType": "Transfer"
      },
      {
        "amount": 600000,
        "deedType": "Quit Claim Deed",
        "documentDate": "2005-10-12T00:00:00.000Z",
        "granteeName": "Martina Kreidl",
        "interestRate": null,
        "interestRateType": "Adjustable Rate",
        "lenderCode": "F",
        "lenderName": "Fremont Investment & Loan",
        "lenderType": "Funding/Finance Company",
        "maturityDate": null,
        "mortgageId": "167008738",
        "open": false,
        "recordingDate": "2005-10-12T00:00:00.000Z",
        "seq": 1,
        "transactionType": "Mortgage"
      },
      {
        "amount": 150000,
        "deedType": "Deed Of Trust",
        "documentDate": "2005-09-16T00:00:00.000Z",
        "granteeName": "Martina Kreidl",
        "interestRate": null,
        "interestRateType": "Fixed Rate",
        "lenderName": "Rudy F Rodriguez Lp",
        "maturityDate": null,
        "mortgageId": "165025829",
        "open": false,
        "recordingDate": "2005-09-16T00:00:00.000Z",
        "seq": 2,
        "transactionType": "Mortgage"
      },
      {
        "amount": 249000,
        "assumable": false,
        "deedType": "Deed Of Trust",
        "documentDate": "2005-02-23T00:00:00.000Z",
        "granteeName": "Martina Kreidl",
        "interestRate": null,
        "interestRateType": "Adjustable Rate",
        "lenderCode": "B",
        "lenderName": "Wells Fargo Bank",
        "lenderType": "Bank",
        "loanType": "Line Of Credit",
        "loanTypeCode": "LOC",
        "maturityDate": null,
        "mortgageId": "152129395",
        "open": false,
        "recordingDate": "2005-02-23T00:00:00.000Z",
        "seq": 3,
        "transactionType": "Mortgage"
      },
      {
        "amount": 215000,
        "assumable": false,
        "deedType": "Deed Of Trust",
        "documentDate": "2004-05-30T00:00:00.000Z",
        "granteeName": "Tobias J Kreidl, Tobias Martina E Kreidl",
        "interestRate": null,
        "interestRateType": "Adjustable Rate",
        "lenderCode": "B",
        "lenderName": "Wells Fargo Bank",
        "lenderType": "Bank",
        "loanType": "Line Of Credit",
        "loanTypeCode": "LOC",
        "maturityDate": null,
        "mortgageId": "136238744",
        "open": false,
        "recordingDate": "2004-05-30T00:00:00.000Z",
        "seq": 4,
        "transactionType": "Mortgage"
      }
    ],
```

### Neighborhood Data

```
"neighborhood": {
      "id": "263649",
      "name": "Sarapalms",
      "type": "subdivision",
      "center": "POINT(-82.5074394490618 27.4166348074334)"
}
```

### Owner Info

An object that contains the property owner(s) names, mailing addresses, length of ownership and equity.

```
"ownerInfo": {
      "equity": null,
      "mailAddress": {
        "address": "1433 Canyon Rd",
        "addressFormat": "S",
        "carrierRoute": "C024",
        "city": "Santa Fe",
        "county": "Santa Fe",
        "fips": "35049",
        "house": "1433",
        "label": "1433 Canyon Rd, Santa Fe, Nm 87501",
        "state": "NM",
        "street": "Canyon",
        "streetType": "Rd",
        "zip": "87501",
        "zip4": "6133"
      },
      "owner1FirstName": "Caryn",
      "owner1FullName": "Caryn Glickman",
      "owner1LastName": "Glickman",
      "owner1Type": "Individual",
      "ownershipLength": 132
}
```

### Property Comps for Subject Property

An array containing details on comparable properties for the address or property ID provided

```
{
	"comps": [
     {
        id: '41794029',
        priorId: '1842600223',
        vacant: false,
        absenteeOwner: false,
        corporateOwned: false,
        outOfStateAbsenteeOwner: false,
        inStateAbsenteeOwner: false,
        propertyId: '41794029',
        bedrooms: '4',
        bathrooms: '3',
        yearBuilt: '1951',
        squareFeet: '1780',
        estimatedValue: '1025381',
        equityPercent: '24',
        lastSaleDate: '2022-05-11',
        lastSaleAmount: '1300000',
        latitude: '38.889334000',
        longitude: '-77.154853000',
        openMortgageBalance: '780000',
        landUse: 'Residential',
        propertyType: 'SFR',
        owner1FirstName: 'Owner1Name',
        owner1LastName: 'May',
        owner2FirstName: 'Stephanie',
        owner2LastName: 'May',
        preForeclosure: false,
        cashBuyer: false,
        privateLender: false,
        lenderName: 'Guaranteed Rate Inc',
        address: [Object],
        mailAddress: [Object]
      },
    	...
  ],
}
```

### Property Info

An object that contains property info such as latitude and longitude, size in square feet, year built, number of bedrooms and bathrooms, full address parts and amenities.

```
{	
	"propertyInfo": {
      "address": {
        "address": "1433 Canyon Rd",
        "carrierRoute": "C024",
        "city": "Santa Fe",
        "congressionalDistrict": "271",
        "county": "Santa Fe",
        "fips": "35049",
        "house": "1433",
        "jurisdiction": "Santa Fe",
        "label": "1433 Canyon Rd, Santa Fe, Nm 87501",
        "state": "NM",
        "street": "Canyon",
        "streetType": "Rd",
        "zip": "87501",
        "zip4": "6133"
      },
      "airConditioningType": "NONE",
      "basementFinishedPercent": null,
      "basementSquareFeet": 0,
      "basementSquareFeetFinished": null,
      "basementSquareFeetUnFinished": null,
      "basementType": "NO BASEMENT",
      "bathrooms": 2,
      "bedrooms": 3,
      "buildingSquareFeet": 3385,
      "carport": false,
      "construction": "Adobe",
      "deck": false,
      "deckArea": "0",
      "fireplace": false,
      "fireplaces": 0,
      "garageSquareFeet": 483,
      "garageSquareFeetFinished": null,
      "garageSquareFeetUnfinished": null,
      "garageType": "Garage, Attached",
      "heatingType": "RADIANT",
      "latitude": 35.68142,
      "livingSquareFeet": 3385,
      "longitude": -105.906501,
      "lotSquareFeet": 32234,
      "parkingSpaces": 2,
      "partialBathrooms": 1,
      "patio": false,
      "patioArea": "0",
      "plumbingFixturesCount": "0",
      "pool": false,
      "poolArea": "0",
      "porchArea": "0",
      "porchType": "Open Porch",
      "pricePerSquareFoot": 0,
      "propertyUse": "Single Family Residence",
      "propertyUseCode": 385,
      "roofConstruction": "197",
      "roofMaterial": "180",
      "roomsCount": 8,
      "rvParking": false,
      "safetyFireSprinklers": false,
      "stories": 1,
      "unitsCount": "0",
      "utilitiesSewageUsage": null,
      "utilitiesWaterSource": null,
      "yearBuilt": 1950
  }
}
```

### Sale History

An array containing details about sale transactions with details such as sale amount, transaction type, purchase method, ltv and seller and buyer names.

```
"saleHistory": [
  {
    "armsLength": false,
    "buyerNames": "Hse Preservation Ptshp L Morey",
    "documentType": "Warranty Deed",
    "documentTypeCode": "DTWD",
    "downPayment": 0,
    "ltv": 0,
    "ownerIndividual": true,
    "purchaseMethod": "Cash Purchase",
    "recordingDate": "2011-03-21T00:00:00.000Z",
    "saleAmount": 0,
    "saleDate": "2011-03-08T00:00:00.000Z",
    "sellerNames": "Kozely,Peter",
    "seq": 0,
    "seqNo": "0",
    "transactionType": "Transfer"
  },
  {
    "armsLength": true,
    "buyerNames": "Peter Kozely",
    "documentType": "Warranty Deed",
    "documentTypeCode": "DTWD",
    "downPayment": 0,
    "ltv": 0,
    "ownerIndividual": true,
    "purchaseMethod": "Cash Purchase",
    "recordingDate": "2006-04-06T00:00:00.000Z",
    "saleAmount": 0,
    "saleDate": "2006-03-24T00:00:00.000Z",
    "sellerNames": "Kreidl,Martina",
    "seq": 1,
    "seqNo": "1",
    "transactionType": "Transfer"
  }
]
```

### School Data

```
 "schools": [
      {
        "name": "Sara Scott Harllee Middle School",
        "street": "6423 9th Street East",
        "city": "Bradenton",
        "state": "FL",
        "zip": "34203",
        "type": "Public",
        "grades": "6-8",
        "rating": "1",
        "parentRating": "4",
        "enrollment": "452",
        "levels": {
          "middle": true
        },
        "location": "POINT(-82.55284 27.426584)"
      },
      {
        "name": "Southeast High School",
        "street": "1200 37th Avenue East",
        "city": "Bradenton",
        "state": "FL",
        "zip": "34208",
        "type": "Public",
        "grades": "9-12",
        "rating": "3",
        "parentRating": "4",
        "enrollment": "1681",
        "levels": {
          "high": true
        },
        "location": "POINT(-82.551079 27.467558)"
      },
      {
        "name": "Kinnan Elementary School",
        "street": "3415 Tallevast Road",
        "city": "Sarasota",
        "state": "FL",
        "zip": "34243",
        "type": "Public",
        "grades": "PK-5",
        "rating": "3",
        "parentRating": "4",
        "enrollment": "601",
        "levels": {
          "preschool": true,
          "elementary": true
        },
        "location": "POINT(-82.520729 27.404907)"
      }
]
```

### Tax Info

An object containing the property’s estimated value, assessed value, assessed land value, assessed year, market land and property values, home improvements value and tax amount.

```
 "taxInfo": {
      "assessedImprovementValue": "465547",
      "assessedLandValue": 61102,
      "assessedValue": 526649,
      "assessmentYear": 2022,
      "estimatedValue": 1895936.4,
      "marketImprovementValue": 1396640,
      "marketLandValue": 183307,
      "marketValue": 1579947,
      "propertyId": 8195564,
      "taxAmount": "12491.00",
      "year": 2022
}
```

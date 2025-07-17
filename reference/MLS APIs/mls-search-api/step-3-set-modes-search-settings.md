---
title: 'Step 3: Set Modes / Search Settings'
deprecated: false
hidden: false
metadata:
  robots: index
---
## "count" Mode

* returns a count for the number of search results that match your query
* will not pull back the full response objects

<br />

## "listing\_ids\_only" Mode

* returns an array of the unique listingId's from all the search results from MLS Search

<br />

## "ids\_only" Mode

* To be used when wanting to pull the Property Detail API record for each listing
* not all listings in the MLS Search/Detail APIs will have an "id"

<br />

## Exclude

<br />

<br />

## Sort

Use the "sort" field on one of the accepted sort params and get your results back just how you want them without the post-processing

| Field Name for "sort" Input Parm | Field That Sort Gets Applied To    |
| :------------------------------- | :--------------------------------- |
| bathrooms                        | listing.property.bathroomsTotal    |
| bedrooms                         | listing.property.bedroomsTotal     |
| contract\_date                   | listing.listingContractDate        |
| listing\_date                    | listing.leadTypes.mlsListingDate   |
| listing\_price                   | listing.leadTypes.mlsListingPrice  |
| living\_area                     | listing.property.livingArea        |
| lot\_size                        | listing.property.lotSizeSquareFeet |
| modification\_timestamp          | modificationTimestamp              |
| price\_change                    | listing.priceChangeTimestamp       |
| sold\_date                       | listing.soldDate                   |
| year\_built                      | listing.property.yearBuilt         |
| sold\_price                      | ..coming in June 2025              |

Note: these sorts will override the default geo-distance (closest first) order when using "latitude"/"longitude" or "address" and "radius" together.

```
{
  "city": "Richmond",
  "state": "VA",
  "active": true,
  "sort": {
    "listing_price": "asc"
  }
}
```

```
{
  "city": "Richmond",
  "state": "VA",
  "active": true,
  "sort": {
    "modification_timestamp": "desc"
  }
}
```
---
title: Listing Price Change Date Searches
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
```
{
  price_change_timestamp_min: "2024-08-01",
  price_change_timestamp_max: "2024-08-15"
}
```

<br />

## Use Case: Identify Listing Price Drops/Price Hikes in a given zip code

```
let input = {
  size: 250,
  zip: "22205",
  price_change_timestamp_min: "2025-03-01",
  price_change_timestamp_max: "2025-03-31"
}

//perform the pagination steps to get all listings with price changes

//example array of listing_ids: [1243, 58930, 03020, 392030]

for (let id of listing_ids) {
  //compare "listing.leadTypes.mlsListingPrice" of cached record for a given listing_id that has matched from the price_change_timestamp search results to the new "listing.leadTypes.mlsListingPrice"
  
  //if newPrice > oldPrice => price hike
  
  //if newPrice < oldPrice => price drop
}

```

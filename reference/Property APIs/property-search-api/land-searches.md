---
title: Land Searches
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## Land Value Search

```json
let request = {
  size: 100,
  city: 'New Bern',
  state: 'NC',
  assessed_land_value_min: 15000,
  assessed_land_value_max: 75000  
}
```

## Lot Size Search

* lot\_size\_min & lot\_size\_max are measured in square feet
* the corresponding field in the Property Detail response will be "lotInfo.lotSquareFeet"

```json
let request = {
  size: 100,
  city: 'New Bern',
  state: 'NC',
  lot_size_min: 8,
  lot_size_max: 15  
}
```

## Vacant Land Search

```
let request = {
  size: 100,
  city: "Richmond",
  state: "VA",
  property_type: "LAND",
  lot_size_min: 1,
  lot_size_max: 20,
  vacant: true
}
```

## Resolving Land Records

* since a lot of land parcels will not have an address, we can tease out the APN identifier for that property instead by doing the following:

```
// Start with a land query on v2/PropertySearch
let input_propertySearch = {
  size: 100,
  city: "Richmond",
  state: "VA",
  property_type: "LAND",
  lot_size_min: 1,
  lot_size_max: 20,
  vacant: true
}

let results = await axios.post('https://api.realestateapi.com/v2/PropertySearch, input_propertySearch, {headers});
                               

//loop through the property IDs from the Land Search and feed each into Property Detail
for (let result of results.data) {
  let input_propertyDetail = {
    id: result.id
  }
  
  let propertyDetails = await axios.post('https://api.realestateapi.com/v2/PropertyDetail, input_propertyDetail, {headers});
 	
  let apn = propertyDetails.data.lotInfo.apn; //or lotInfo.apnUnformatted                                     
}


```

## Search By APN Directly

* using the AutoComplete API, you can start typing an APN and have the auto-suggest complete your search

```
let input = {
  search: "50420" //more characters after but list of options will begin to appear after 1st few characters
}
```

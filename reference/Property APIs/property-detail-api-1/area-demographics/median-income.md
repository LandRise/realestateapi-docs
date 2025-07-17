---
title: Median Income Analysis
excerpt: Utilize insights into zip code based median income values
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Example Use Case

Since each property in the same zip code will have the same ".demographics.medianIncome" value - a way you could work towards building out a small national database (for analytics, etc.) of median incomes from our data

tl;dr

* get a list of zips
* find a property from each zipcode using Property Search
* enrich that property with Property Detail
* grab the median income value from .demographcs.medianIncome for each

```
//list of zips for city, state, or all of national zips

let medianIncomesByZip = [];

for (let zip of zips) {
  
  
  let input = {
    size: 1,
    zip: zip
  }
  
  let randomPropertiesFromZipCode = await PropertySearch("https://api.realestateapi.com/v2/PropertySearch", input, {headers})
  
  //results of Property Search are an array of properties, even with size: 1 specified
  //grab first element of this array and send it's property "id" to Property Detail
  
  let property_detail_input = {
    id: randomPropertiesFromZipCode[0].id
  }
  
  let recordWithMedianIncomeData = await PropertyDetail("https://api.realestateapi.com/v2/PropertyDetail" ,property_detail_input, {headers})
  
  medianIncomesByZip.push({
    zipcode: zip,
    medianIncome: recordWithMedianIncomeData.demographics.medianIncome
  })
  
 
}


```

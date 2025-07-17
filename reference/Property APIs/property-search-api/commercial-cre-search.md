---
title: Commercial (CRE) Search
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
RealEstateAPI can support multiple types of Commercial searches:

1. Mutli-Family Commercial Properties
   1. "mfh\_5plus" will return multi-family properties with 5 or more units
      1. not all properties marked mfh\_5plus: true are true commercial as deemed on the county level
   2. since definitions of commercial multi-family can vary, you can create your own definition using:
      1. "property\_type": "MFR"
      2. "units\_min" & "units\_max"

<br />

2. Commercial Land
   1. perform initial search for property\_type: "LAND"
   2. inspect the "lotInfo.landUse" for "COMMERCIAL" or "Commercial"

```
//Step 1 - hit /v2/PropertySearch
{
  ids_only: true, //to prevent double spending your credits
  city: "Richmond",
  state: "VA",
  property_type: "LAND"
}

//Step 2  - hit /v2/PropertyDetail to get access to lotInfo.landUse for each record

for (let id of propertySearchResults.data) {
  
  let result = await hitPropertyDetail(id);
  
  console.log('check if commercial: ', result.lotInfo.landUse);
  //if "COMMERCIAL" or "Commercial" it is land designated for commercial use
}
```

<br />

<br />

3. Commercial (General)
   1. most of our commercial coverage falls in property\_type: "OTHER"
   2. if you want to get specific with a certain category, you can provide a Property Use Code or a List of Property Use Codes
   3. for example, if I wanted to search for Office Buildings I could use the following codes:
      1. 136 => COMMERCIAL OFFICE (GENERAL)
      2. 140 => STORE/OFFICE (MIXED USE)
      3. 169 => OFFICE BUILDING
      4. 170 => OFFICE BUILDING (MULTI-STORY)
      5. 171 => COMMERCIAL OFFICE/RESIDENTIAL (MIXED USE)
      6. 184 => SKYSCRAPER/HIGH-RISE (COMMERCIAL OFFICES)

```
{
  state: "VA",
  property_use_code: [136, 140, 169, 170, 171, 184]
}
```

<br />
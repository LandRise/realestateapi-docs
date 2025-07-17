---
title: ids_only Searches for Credit Optimization
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
Property Search can pull up to 250 property records per API call. In order to keep response times far under 1 second, we only return a subset of the whole set of fields we have for each property in the Property Search responses.

Some of you may be wondering: "Well, do I have to spend 2 credits for each property to find it in the Search API and to get its full property details??" - The Answer is No!

In order to retrieve your search results from the Property Search API that match your criteria AND get the full Property Detail enrichment for each property, use our "**ids\_only**" request field.

<br />

The max number of ids that can be returned per each ids\_only: true Property Search API calls is 10,000.

<br />

```
// /v2/PropertySearch
{
  city: "Richmond",
  state: "VA",
  pre_foreclosure: true,
  ids_only: true
}
```

Will return a list of property IDs for all properties matching this query's search criteria.

```
// /v2/PropertyDetail

for (let propertyId of propertySearchResultIds) {
  
  let full_details = await propertyDetail({id: propertyId });
}

```
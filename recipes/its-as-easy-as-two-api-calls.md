---
title: It's as Easy as Two API Calls
description: >-
  Make the most of our property data sets by enriching your Property Search
  results with the Property Bulk Detail API
hidden: false
recipe:
  color: '#579e86'
  icon: 🏘️
---
```javascript JavaScript
(async () => {
  try {
    let filter = { /* Decide on your custom filter set & Geo */ };
    
    let search_results = await runSearch(filter, 100, 0);
    
    let property_ids = search_results.map((property) => property.id));
    
    let bulk_results = await runPropertyDetailBulkAction(property_ids);
    
    console.log('bulk property detail results: ', bulk_results);
    
    
  } catch(e) {
    console.error(e);
  }
})();

function runSearch(filter, page_size, resultIndex) {
  
  let search_options = {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'x-api-key': 'APIKEY'
    },
    data: {
      count: false,
      size: page_size,
      resultIndex: resultIndex,
      ...filter
    }
  };
  
    
  const response = await fetch('https://api.realestateapi.com/v2/PropertySearch', search_options)
  
  const data = await response.json();
  
  return data;
}

function runPropertyBulkDetailAction(property_ids) {
  let search_options = {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': 'APIKEY'
      },
      data: property_ids
  };
  
  const response = await fetch('https://api.realestateapi.com/v2/PropertyDetailBulk', search_options)
    	
  const data = await response.json();
  
  return data;   
}
    


```

# Step 1: Run Your Search

<!-- javascript@3-5 -->

Choose your set of search parameters, including geo and property/owner characteristics filters, and then proceed to hit the Property Search API with this payload.

For the sake of this example, we won't deal with paging and only grab the first 100 records.

# Step 2: Build a List of Property IDs



Once we have our results from the Property Search API, then all we need to get the full Property Profiles for all of them is to use the "id" field for each object as a search parameter.

While Property Detail API only takes a single ID as a string, the Property Bulk Detail API needs an array type. In order to do this easily, we can do a JS array map operation on the property search results and store it in "property_ids" and use it as the array input to the Property Detail Bulk endpoint.

# What's Next?



With the data from both the Property Search API that matched your search criteria and our full property records for them, the only question left is how to serve it to your users.
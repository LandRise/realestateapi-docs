---
title: 'Property Search: Build Your 1st List'
description: Simple code sample showing how the Property Search API works
hidden: false
recipe:
  color: '#75bdb8'
  icon: 🔍
---
```javascript JavaScript
async function runSearch() {
 try {
   
   const options = {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': '<<apiKey>>',
        'x-user-id': ''
      },
      data: {
        count: false, //'false' here will pull back properties instead of just a count
        size: 50,
        city: 'Houston',
        state: 'TX',
        
        //Your choice of filters
        /*
        	See More in our API Docs:
          https://beta.realestateapi.com/reference/property-search-api
          
          negative_equity: true,
          equity: true,
          cash_buyer: true,
          quit_claim: true,
          corporate_owned: true,
          free_clear: true,
          absentee_owner: true,
          reo: true,
          auction: true,
          foreclosure: true,
          pre_foreclosure: true,
          beds_min: 2,
          beds_max: 4
        */
        
        
      }
		};

    let response = await fetch('https://api.realestateapi.com/v2/PropertySearch', options)

    let data = await response.json();
   
   	return data;

 } catch(e) {
 		//200 - successful search
   	//400 - need to reformat the request body (stringified, fits required field models from docs
   	//404 - look at the url and make sure you have the correct endpoint url
   	//429 - you've reached a rate limit, consider adding interval timing to large amounts of calls
 		//500 - contact us in our discord community or at dev@realestateapi.com
 }
}
```

# Step 0: Configure Headers

<!-- javascript@6-11 -->

Use your RealEstateAPI key to make calls to the Property Search API.

You can include an 'x-user-id' field that will allow you separate actions from your app user-by-user

# Step 1: Figure Out Your Target Geo for the Search

<!-- javascript@14-15 -->

Narrow down your search to a certain county or city before adding the next layer of filtering for the types of properties you want to find

# Step 2: Choose Your Combination of Property Filters

<!-- javascript@20-38 -->

You can mix and match the filters however you see fit, but the more you select to be 'true', the less results you are likely to get back.

# Step 3: Perform the Property Search

<!-- javascript@41 -->

Now that we know what Geo we are targeting and what property characteristics to look for in that area, we just need to provide that data to the Property Search API endpoint.

# What's Next?



Once you've learned how to do a basic query, the next step would be to learn how to utilize the Property Detail or Property Detail Bulk API to get even more comprehensive data on your properties returned from the Property Search API.
---
title: 'Property Search: Paging Example'
description: >-
  Using a Property Search Count query in order to page through a list of filter
  results larger than the maximum size of 250
hidden: false
recipe:
  color: '#d3d7d9'
  icon: 🔁
---
```javascript JavaScript
async function runSearchAndGetAllResults(filter, page_size, resultIndex) {
    try {
      
        let body = {
            count: false,
            size: page_size,
            resultIndex: resultIndex,
            ...filter
        }

        let headers = {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': '<Your API Key>'
        }
        
        const data = await axios.post('https://api.realestateapi.com/v2/PropertySearch', body, {headers});

        //only one search needs to be done because result set was smaller than page_size
        if (data.data.resultCount == data.data.recordCount) return data.data.data;
        
        //stash these results, then prepare next paging API Call
        let results = data.data.data;

        body.resultIndex += data.data.recordCount;

        let resultCount = data.data.resultCount;

        console.log('total results to get: ', resultCount);
      
        while (body.resultIndex < resultCount) {
            
            let next_search = await axios.post('https://api.realestateapi.com/v2/PropertySearch', body, {headers});
                        
            //add any records starting at this resultIndex to the results
            next_search.data.data.forEach((obj) => results.push(obj));
            
            body.resultIndex += next_search.data.recordCount;
            
        }

        console.log('total results (end of process): ', results.length);
      
        return results;
      
    } catch(e) {
      console.error(e);
    }
}

(async () => {
    try {
        let filter = {
            city: 'Durham',
            state: 'NC',
            zip: '27703',
						//any property characteristic flags you want to narrow the search
        };

        const page_size = 50;
        let resultIndex = 0;

        await runSearchAndGetAllResults(filter, page_size, resultIndex);
    } catch(e) {
        console.error(e);
    }
})();
```

# Step 1: Select Filter

<!-- javascript@53-58 -->

Choose the set of property flags and the specific geo (county, state, city, or zip) that you would like to perform your search with

# Step 2: Setup a Paging Loop

<!-- javascript@1-44 -->

The reason why we need paging is because the Property Search API will only return a max of 250 properties, even if the 'size' property is set to larger than that. So if you need more than 250 properties or all of them based on the search criteria, then you will need to implement paging.

The sample function provided will get all results, using the resultCount property from the first search and the resultIndex cursor property to make the number of calls necessary to retrieve all records.

# What's Next?



This implementation of the Property Search API is best for serving lists of properties (and associated data) matching specific user filters in an application for example. Once you have this code working in a sandbox environment, you're ready to integrate it into various user flows.
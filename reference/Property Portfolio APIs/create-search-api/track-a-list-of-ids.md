---
title: Track a List of IDs
excerpt: >-
  Does what you need to track property wise not fall cleanly into a specific
  Property Search set of criteria? Commonly if you're building lead types across
  multiple geos or favorited lists by users that could consist of multiple lead
  types from different searches, you might need to update only certain property
  IDs. This guide should help you setup tracking for a list of IDs.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Step 1: Create Saved Search API

```json
{
	search_name: "Lukas_IDsTest_062525",
	list_size: 10, //make sure this matches the .length of the ID list you provide
	search_query: { 
         ids: [
           "335810662",
           "190167848",
           "191455659",
           "194066223",
           "187069145",
           "33726348",
           "35780942",
           "35809525",
           "34483531",
           "40671873"
          ]
	}
}
```

### Example Response from Create Saved Search for List of IDs

```
{
  input: {
    search_name: 'Lukas_IDsTest_062525',
    list_size: 10,
    search_query: { ids: [Array], size: 10, ids_last_update: true }
  },
  data: {
    search: {
      searchId: '910d5054-8c88-4ee2-a139-284d4cxxxxxx',
      accountId: 96,
      xUserId: null,
      searchName: 'Lukas_IDsTest_062525',
      searchQuery: '{"ids":[335810662,190167848,191455659,194066223,187069145,33726348,35780942,35809525,34483531,40671873]}',
      lastReportDate: '2025-06-26T01:15:11.000Z',
      nextReportDate: '2025-06-27T01:15:11.000Z',
      createdAt: '2025-06-26T01:15:11.000Z',
      meta_data: {}
    },
    results: [
      [Object], [Object],
      [Object], [Object],
      [Object], [Object],
      [Object], [Object],
      [Object], [Object]
    ],
    summary: { size: 10, added: 10, deleted: 0, updated: 0, unchanged: 0 }
  },
  statusCode: 200,
  statusMessage: 'Success',
  credits: 0,
  live: true,
  requestExecutionTimeMS: '48ms'
}
```

<br />

<br />

## Step 2: Get Daily Report and Make Updates Accordingly

```json
{
  searchId: '910d5054-8c88-4ee2-a139-284d4cxxxxxx'
}
```

<br />

### Example Response from Retrieve Saved Search for List of IDs

```json
{
    searchId: '910d5054-8c88-4ee2-a139-284d4cxxxxxx',
    accountId: 089080,
    xUserId: null,
    searchName: 'Lukas_IDsTest_062525',
    searchQuery: '{"ids":[335810662,190167848,191455659,194066223,187069145,33726348,35780942,35809525,34483531,40671873]}',
    lastReportDate: '2025-06-26T01:16:12.000Z',
    nextReportDate: '2025-06-27T01:16:12.000Z',
    createdAt: '2025-06-26T01:15:11.000Z',
    meta_data: {}
  },
  results: [
    {
      id: 335810662,
      changeType: 'added',
      lastUpdateDate: '2025-06-11T00:00:00.000Z'
    },
    {
      id: 190167848,
      changeType: 'added',
      lastUpdateDate: '2025-06-18T00:00:00.000Z'
    },
    {
      id: 191455659,
      changeType: 'added',
      lastUpdateDate: '2025-06-18T00:00:00.000Z'
    },
    {
      id: 194066223,
      changeType: 'added',
      lastUpdateDate: '2025-06-18T00:00:00.000Z'
    },
    {
      id: 187069145,
      changeType: 'added',
      lastUpdateDate: '2025-06-11T00:00:00.000Z'
    },
    {
      id: 33726348,
      changeType: 'added',
      lastUpdateDate: '2025-06-19T00:00:00.000Z'
    },
    {
      id: 35780942,
      changeType: 'added',
      lastUpdateDate: '2025-06-18T00:00:00.000Z'
    },
    {
      id: 35809525,
      changeType: 'added',
      lastUpdateDate: '2025-06-18T00:00:00.000Z'
    },
    {
      id: 34483531,
      changeType: 'added',
      lastUpdateDate: '2025-06-11T00:00:00.000Z'
    },
    {
      id: 40671873,
      changeType: 'added',
      lastUpdateDate: '2025-06-18T00:00:00.000Z'
    }
  ],
	summary: { size: 10, added: 10, deleted: 0, updated: 0, unchanged: 0 }
}


```

<br />

<br />

<br />

<br />

# What if I have more than 10,000 IDs to Track?

* Since list\_size max is 10,000, you'll need to break up your "ids" array input into multiple saved search queries
  * in this setup, make sure the "search\_name" you provide for each helps you serialize the results in your daily jobs
  * e.g. "IDs\_List\_Seq\_000", "IDs\_List\_Seq\_001", "IDs\_List\_Seq\_002", etc.
* once you hit enough properties (in the 10M+ range), you may get more benefit of tracking updates from all zip codes for easy size chunks to iterate through and compare to your larger index of IDs you are tracking
  * would be one saved search per zip , and each day's Retrieve for each search\_id could be prioritized where you have the most properties saved
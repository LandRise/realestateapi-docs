---
title: ("C") City Completion
excerpt: Match a partial city & state combination
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
	input: { 
    search: 'Herndon, V',
    search_types: ["C"]
  },
  data: [
    {
      state: 'VA',
      stateId: '51',
      zip: '20170',
      county: 'Fairfax',
      countyId: '059',
      city: 'Herndon',
      street: 'Herndon Pkwy',
      searchType: 'S',
      fips: '51059',
      title: 'Herndon Pkwy, Herndon, VA'
    },
    {
      state: 'VA',
      stateId: '51',
      zip: '20170',
      county: 'Fairfax',
      countyId: '059',
      city: 'Herndon',
      street: 'Herndon Woods Ct',
      searchType: 'S',
      fips: '51059',
      title: 'Herndon Woods Ct, Herndon, VA'
    },
    {
      state: 'VA',
      stateId: '51',
      zip: '20170',
      county: 'Fairfax',
      countyId: '059',
      city: 'Herndon',
      street: 'Herndon Mill Cir',
      searchType: 'S',
      fips: '51059',
      title: 'Herndon Mill Cir, Herndon, VA'
    },
    ...
	],
  totalResults: 10000,
  returnedResults: 10,
  statusCode: 200,
  statusMessage: 'Success',
  credits: 0,
  live: true,
  requestExecutionTimeMS: '64ms'
}
```

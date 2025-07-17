---
title: AutoComplete Params
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
Based on the user input that was provided during the AutoComplete API phase of your application's AutoComplete design, you will call the Property Search with different sets of parameters.

```
//searchType: 'A' returned from AutoComplete - full address
let request = {
  size: 100,
  searchType: 'A',
  id: '196537292',
  apn: '38  01121-0000-00002',
  stateId: '34',
  countyId: '005',
  fips: '34005',
  title: '9 Topeka Pass, Willingboro, NJ, 08046'
}

//searchType: 'Z' returned from AutoComplete  - zip
let request = {
  size: 100,
  searchType: 'Z',
  id: '28831304',
  apn: '13-010-007',
  stateId: '51',
  countyId: '013',
  fips: '51013',
  title: '883 N Kentucky St, Arlington, VA, 22205'
}

//searchType: 'S' returned from AutoComplete - city/state
let request = {
  size: 100,
  searchType: 'S',
  stateId: '51',
  countyId: '059',
  fips: '51059',
  title: 'Herndon Pkwy, Herndon, VA'
}

//searchType: 'C' returned from AutoComplete - county
let request = {
  size: 100,
  searchType: 'C',
  id: '531392',
  apn: '012689 30.4-5-54',
  fips: '36001',
  countyId: '001',
  stateId: '36' 
}

//searchType: 'G' returned from AutoComplete - neighborhood
let request = {
  size: 50,
  searchType: 'G',
  neighborhood_id: '',
  neighborhood_name: '',
  
}

```

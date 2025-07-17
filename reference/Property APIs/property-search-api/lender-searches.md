---
title: Lender Searches
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
We only offer the singular "private\_lender" flag in order to find properties with a lender at scale. However, the power of this flag is most effective when you run all the Property ID's you get back with this search to the Property Detail Bulk endpoint. That response will give you back more detailed information about the Lender that you could have useful business applications.

```
let property_search_request = {
  size: 150,
  private_lender: true,
  city: 'Richmond',
  state: 'VA'  
}

//search response:
//search_result = [{ id: x, ... }, {id: y, ...}, ... ]
 
let property_detail_bulk_request = search_result.map((obj) => obj.id))

//bulk detail response:
//bulk_result: [ {}, {}, {}, {}, ...]



```

---
title: Get All Saved Searches API
excerpt: >-
  Retrieve all your created Saved Searches or filter all your through all
  created Saved Searches using the x-user-id you provided on the Create Saved
  Search step, by the search_id, or by other metadata provided in the Create
  Saved Search step
api:
  file: property-portfolio-apis.json
  operationId: get-all-saved-searches
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Sample Requests

```json
// filter by "search_id", returns a single search

"filter": {
    "search_id": "your-search-id"
}
```

```json
// filter by "x_user_id", returns all searches associated
// with your "x-user-id" header

"filter": {
    "x_user_id": "your-x-user-i"
}
```

```json
// filter by "meta_data", returns all searches matching the 3 meta_data fields
// [key_1, key_2, key_3]

"filter": {
    "meta_data": {
		    "key_1": "foo"
        "key_3": "baz"
    }
}
```
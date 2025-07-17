---
title: Delete Saved Search
excerpt: ''
api:
  file: property-portfolio-apis.json
  operationId: update-saved-search
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Example JSON Input Object

```
POST https://api.realestateapi.com/v1/PropertyPortfolio/SavedSearch/Delete

{
	"search_id": "5a90fb85-37c5-456f-b88f-dec52c0b8911"
}
```

<br />

## Example JSON Output Response Object

```
{
  "input": {
    "search_id": "1280f7b8-7285-4055-915d-f19be4cd7af1"
  },
  "data": {
    "searchId": "1280f7b8-7285-4055-915d-f19be4cd7af1",
    "deleted": true
  },
  "statusCode": 200,
  "statusMessage": "Success",
  "credits": 0,
  "live": true,
  "requestExecutionTimeMS": "214ms"
}
```
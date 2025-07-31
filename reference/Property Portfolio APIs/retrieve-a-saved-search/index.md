---
title: Retrieve a Saved Search
excerpt: ''
api:
  file: property-portfolio-apis.json
  operationId: retrieve-a-saved-search
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Sample Request

```json
{
	"search_id": "3b17feae-0245-45ef-a91b-77b89ced524c"
}
```

<br />

### Sample Response

```json
{
  "input": {
    "search_id": "3b17feae-0245-45ef-a91b-77b89ced524c"
  },
  "data": {
    "search": {
      "searchId": "3b17feae-0245-45ef-a91b-77b89ced524c",
      "accountId": 59,
      "xUserId": null,
      "searchName": "MLS Active In The 918",
      "searchQuery": "{\"city\":\"Tulsa\",\"state\":\"OK\",\"mls_active\":true}",
      "list_size": 10000,
      "lastReportDate": "2024-05-24T03:28:16.000Z",
      "nextReportDate": "2024-05-25T03:28:16.000Z",
      "createdAt": "2024-05-24T03:25:11.000Z",
      "meta_data": {}
    },
    "results": [
      {
        "id": "186925006",
        "changeType": "deleted",
        "lastUpdateDate": "2024-01-09T00:00:00.000Z"
      },
      {
        "id": "385788",
        "changeType": null,
        "lastUpdateDate": "2024-02-23T00:00:00.000Z"
      },
      {
        "id": "197384549",
        "changeType": "updated",
        "lastUpdateDate": "2024-05-02T00:00:00.000Z"
      },
      {
        "id": "194078780",
        "changeType": "added",
        "lastUpdateDate": "2024-01-09T00:00:00.000Z"
      },
      ...
    ],
    "summary": {
      "size": 10000,
      "added": 1,
      "deleted": 1,
      "updated": 11,
      "unchanged": 9987
    }
  },
  "statusCode": 200,
  "statusMessage": "Success",
  "credits": 0,
  "live": true,
  "requestExecutionTimeMS": "249ms"
}
```

## What to do with Response from Retrieve API call

* sort each object in the "results" array by "changeType"
* For additions ('added' changeType), make sure to persist this ID to your DB (along with lastUpdateDate) and make the Property Detail API call for additional info since you this is a new record that hasn't been pulled yet
* For updates ('updated' changeType), make a Property Detail call to refresh the record if the timestamp is within your desired refresh period (more than a week old, more than a month old, etc.)
* For deletions ('deleted' changeType), delete this ID from your DB so that you are no longer checking for updates on this ID for the given saved search

## Example "summary" object after Create API call

* for a given zip code with 3431 properties

```
summary: { size: 3431, added: 3431, deleted: 0, updated: 0 }
```
---
title: Grouping & Performing Updates
excerpt: >-
  Example of how to group by 'changeType' and update your data via the Property
  Detail API
deprecated: false
hidden: false
metadata:
  robots: index
---
* sort each object in the "results" array by "changeType"
* For additions ('added' changeType), make sure to persist this ID to your DB (along with lastUpdateDate) and make the Property Detail API call for additional info since you this is a new record that hasn't been pulled yet
* For updates ('updated' changeType), make a Property Detail call to refresh the record if the timestamp is within your desired refresh period (more than a week old, more than a month old, etc.)
* For deletions ('deleted' changeType), delete this ID from your DB so that you are no longer checking for updates on this ID for the given saved search

```json
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
]
```

<br />

## Handle Additions

* When I see ID: 194078780 ( results\[3] ) - I will do the following:
  * call Property Detail with input \{ id: 194078780 }
  * save to your DB the full Property Detail response and a metadata object with the timestamp "lastUpdateDate" from the Retrieve API call response:
    ```json
    {
      { id: 194078780, lastUpdated: "2024-01-09T00:00:00.000Z", lastChangeType: "added" },
    	{ data: { ... all Property Detail response data }    
    }

    --OR--
    {
      { id: 194078780, changelog: [{ changeType: "added", updateDate:"2024-01-09T00:00:00.000Z" }] },
    	{ data: { ... all Property Detail response data }    
    }

    ```
  * the "changelog" implementation will help you persist a historical lineage for a given property ID since you started tracking it, and could be helpful for auditing purposes

<br />

## Handle Updates

* When I see ID: 197384549 - I will do the following:
  * check for this ID in my DB to make sure that it exists (it should if you handle the Addition cases properly)
  * when I get the matching DB for this ID, check the most recent timestamp and decide if you want to spend the 1 credit against Property Detail to refresh it depending on your Update Policy. Some people refresh weekly, some monthly, some whenever one is available - pick what's best for your team's data refresh strategy.
  * If you have decided to refresh, just simply hit the Property Detail API, upsert/update your DB record with the fresh Property Detail response and update your "lastUpdated" field or insert a new entry to the "changelog" array
    * In this step you may also want to perform a diff of the old Property Detail response and the new Property Detail response to see which fields changed values and persist that somewhere in your DB if you care to
    * find an efficient strategy that prevents you storing the entire payload from Property Detail every refresh but still helps you track what changes were made anytime an update is performed
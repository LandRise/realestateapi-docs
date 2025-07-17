---
title: Create Saved Search API
excerpt: ''
api:
  file: property-portfolio-apis.json
  operationId: create-search-api
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
{
	"search_name": "Oklahoma City MLS Active SFR",
	"search_query": {
		"size": 1000,
		"mls_active": true,
		"property_type": "SFR",
		"city": "Oklahoma City",
		"state": "OK"
	},
	"meta_data": {
		"key_1": "test-metadata-value"
	}
}
```

<br />

## Example JSON Output Response Object

```
{
	"input": {
		"search_name": "Oklahoma City MLS Active SFR",
		"search_query": {
			"size": 1000,
			"mls_active": true,
			"property_type": "SFR",
			"city": "Oklahoma City",
			"state": "OK"
		},
		"meta_data": {
			"key_1": "test-metadata-value"
		}
	},
	"data": {
		"searchId": "5a90fb85-37c5-456f-b88f-dec52c0b8911",
		"searchName": "Oklahoma City MLS Active SFR",
		"xUserId": "x-user-id" 
	},
	"statusCode": 200,
	"statusMessage": "Success",
	"credits": 10
}
```
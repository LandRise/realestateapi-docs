---
title: API Keys
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
## **RealEstateAPI Key Basics**

*Test* —  a test key has Property Detail API and SkipTrace API scope and 100 requests.  

*Prod* — a prod key will be issued to your account upon getting on any form of recurring payment plan, whether it is the monthly data subscriptions or the annual agreements.

To find out more about getting a RealEstateAPI key, you can book with our team here: [RealEstateAPI Discovery Call](https://calendly.com/d/g6f-xkt-dx3/discovery-call)

### Deactivating Keys

If you wish to deactivate a certain RealEstateAPI key for any reason, please contact support at [dev@realestateapi.com](mailto:dev@realestateapi.com)

***

## Using your API Key

Just make sure to include your RealEstateAPI key in the headers of your requests like so.

```
let headers = {
	'x-api-key': "Your-RealEstateAPI-Key" 
}

let { data ] = await axios.post(url, body, { headers } );

...
```

***

## **Accessing Other API Scopes**

### Property Search & CSV Generator

To get access to the Property Search and CSV Generator for Property Search, you'll need to schedule a time to meet with our team to discuss search size limits, paging results, and which filters or fields are most business-critical for you. 

### AutoComplete

The AutoComplete API scope is given to any key that also has Property Search scope or is on any paid tier above the free tier with a test key or the Sandbox Prepaid Bundle.

### Bulk API Scopes

Since your test key only comes with 100 requests, and the Property Detail Bulk and Bulk SkipTrace can each accept up to 1,000 records in a single request, you will not have access to them until you have a prepaid credit balance or monthly/annual data access agreements.

### Special Sub-Scopes and Custom APIs

Some endpoints have sub-scope permissions that limit what fields you can and cannot use. These are typically not the main functionality of the endpoint, but rather other useful applications on the same fieldset offered by that endpoint. Some are public like "Summary" on Property Search, and some are custom-crafted for a specific business need and exclusive to an organization. If you think you need a custom API modification or functionality off one of the main endpoints, please email us at [dev@realestateapi.com](mailto:dev@realestateapi.com) or book a Brainstorming meeting with us.

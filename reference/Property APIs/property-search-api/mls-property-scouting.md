---
title: MLS Property Scouting
excerpt: >-
  Are you on the hunt for MLS listings, pendings, and cancellations? You've come
  to the right place. We get our MLS Listings updated weekly, so you can catch
  the freshest listings for your business.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
There are a couple options available in the Property Search API for finding MLS properties.

The first way is to use the MLS boolean flags for listings. The 3 available are:

* mls\_active
* mls\_pending
* mls\_cancelled

```
//find active listings
let request = {
  size: 250,
  count: false,
  mls_active: true,
  state: 'VA'
}

//find pendings
let request = {
  size: 250,
  count: false,
  mls_pending: true,
  city: 'Houston'
}

//find cancelled listings
let request = {
  size: 250,
  count: false,
  mls_cancelled: true,
  state: 'FL'
}
```

The second way to search for MLS properties is by MLS Listing Price. The fields available are:

* mls\_listing\_price
* mls\_operator
* mls\_listing\_min
* mls\_listing\_max

```
// mls_listing_price & mls_operator must be used together
let request = {
  size: 250,
  count: false,
  mls_listing_price: 250000,
  mls_operator: 'gte',
  zip: 22205
}

// mls_listing_min & mls_listing_max can be used together, but don't have to be
// if using min/max, you should exclude mls_listing_price & mls_operator
let request = {
  size: 250,
  count: false,
  mls_listing_min: 250000,
  mls_listing_min: 350000,
  zip: 22205
}

// -- OR -- Just specify a min or max  //
let request = {
  size: 250,
  count: false,
  mls_listing_min: 250000,
  zip: 22205
}


```

## Getting Agent Info and More Listing Data

Take the Property ID's or addresses from your Property Search result objects above and make an API Call to Property Detail (or Detail Bulk).

Inspect the response for the ".mlsHistory" array:

```
{
	"mlsHistory": [
  	{
        "propertyId": "18871883",
        "type": "single_family",
        "price": "525000",
        "beds": 3,
        "baths": 2.5,
        "daysOnMarket": "30",
        "agentName": "Bryan Goldman",
        "agentOffice": "Keller Williams Realty",
        "agentPhone": "3606933336",
        "status": "offmarket",
        "statusDate": "2022-05-13",
        "seqNo": "1"
      },
    	...
  ],
	
}
```

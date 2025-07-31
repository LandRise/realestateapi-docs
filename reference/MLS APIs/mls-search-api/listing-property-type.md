---
title: Listing Property Type
excerpt: listing_property_type [string]
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
| Enum Value             | Enum Descriptor      |
| :--------------------- | :------------------- |
| RENTAL                 | Rental               |
| LAND                   | Land Lot             |
| BUSINESS\_OPPORTUNITY  | Business Opportunity |
| RESIDENTIAL\_INCOME    | Residential Income   |
| RESIDENTIAL            | Residential          |
| RESIDENTIAL\_LEASE     | Residential Lease    |
| COMMERCIAL             | Commercial           |
| COMMERCIAL\_FOR\_LEASE | Commercial for Lease |

<br />

## Fully Excluding Rentals

```json
{
  city: "Richmond",
  state: "VA",
  active: true,
  exclude: [
    { listing_property_type: "RENTAL" },
    { listing_property_type: "RESIDENTIAL_LEASE" }  
	]
}


```

<br />

## Get Commercial & Commercial for Lease

```json json
{
  city: "Richmond",
  state: "VA",
	active: true,
  "and": [
    {
      "or": [
        { listing_property_type: "COMMERCIAL" },
        { listing_property_type: "COMMERCIAL_FOR_LEASE" } 
			]

    }
	]
}


```
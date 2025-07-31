---
title: 'Step 2: Set your Status(es)'
excerpt: Find listings based on their current MLS status
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
For simple searching on listing status use the following boolean filters:

* active: true
* cancelled: true
* failed: true
* pending: true
* sold: true

<br />

Options Available for the "status" field:

* Active
* Closed
* Coming Soon
* Contingent
* Expired
* Off Market
* Pending
* Pending Sale
* Sold
* Active Under Contract

```
{
  status: "Active",
  city: "Richmond",
  state: "VA"
}
```

<br />

## Want to include multiple statuses?

```json
{
  city: "Richmond",
  state: "VA",
  "and": [
    {
      "or": [
        { active: true },
        { pending: true } 
			]

    }
	]
}

--OR--

{
  city: "Richmond",
  state: "VA",
  "and": [
    {
      "or": [
        { status: "Active" },
        { status: "Pending" } 
			]

    }
	]
}


```
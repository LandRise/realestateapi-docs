---
title: '"count" Query'
excerpt: >-
  Get counts of any search before you run it! Quickly compare counts across any
  type of search without spending any credits.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
* Find out how many properties we have in Arlington, VA

```
{
	count: true,
  city: "Arlington",
  state: "VA"
}
```

* find out how many SFRs in Arlington, VA

```
{
	count: true,
  city: "Arlington",
  state: "VA",
  property_type: "SFR"
}
```

* find out how many NOD pre-foreclosures in Arlington, VA

```
{
  count: true,
  city: "Arlington",
  state: "VA",
  pre_foreclosure: true,
  notice_type: "NOD"
}
```

When "count": true is specified, the credit spend for your API call is 0 credits.

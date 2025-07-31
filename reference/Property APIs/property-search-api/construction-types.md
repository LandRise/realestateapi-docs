---
title: Construction Types
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
"construction" - property search request field

For a full list of the possible values you can search using the "construction" input field, go here: [https://developer.realestateapi.com/reference/construction-types-1](https://developer.realestateapi.com/reference/construction-types-1)

<br />

Specify a single construction type:

```
{
  city: "Arlington",
  state: "VA",
  construction: "Steel Frame"
}
```

<br />

Specify that building must match one of the following construction types:

```
{
  city: "Arlington",
  state: "VA",
  "and": [
    {
    	"or": [
        { construction: "Brick" },
        { construction: "Log" }
      ]
    }
  ]
}
```

<br />
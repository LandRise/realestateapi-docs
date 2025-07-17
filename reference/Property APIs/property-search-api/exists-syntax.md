---
title: '"exists" Syntax'
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
Filter out results where certain fields don't exist

* house
* unit
* street
* city
* state
* county
* zip
* mail\_house
* mail\_unit
* mail\_street
* mail\_city
* mail\_state
* mail\_county
* mail\_zip

**Example 1**: A common use case for "exists" is to ensure you are only getting valid mailing addresses to reach absentee owners

This example will only pull back properties where the owner's mailing address is verified to be in a format: "123 Main St, Arlington, VA 22205"

```
{
  absentee_owner: true,
  exists: {
    mail_house: true,
    mail_street: true,
    mail_city: true,
    mail_state: true,
    mail_zip: true
  }
}
```

**Example 2**: Simply do some cleaning for your commonly run queries to prevent undesired results

* using \{ house: true } can be functionally useful to eliminate " propertyType: 'LAND' " properties much the same as an "exclude" filter for land or an explicit setting to the property type that you want such as "SFR"
* Land is a good example here because those addresses come back with a missing "house" number in more concentration than any other property type

```
{
  exists: [
    { house: true } 
  ]
}
```

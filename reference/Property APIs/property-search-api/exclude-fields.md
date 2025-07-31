---
title: '"exclude" Field'
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
All Property Search input parameters are able to be excluded.

* Examples:
  * exclude mls\_active: false will remove non-active listings
  * county: "Arlington", state: "VA" + exclude zip: "22205" will return all properties in Arlington County, VA except ones in zip code 22205

The following table is a list of exclude filters where the types are different than what is defined in the Property Search input schema. The purpose of these are to filter out results that have null-values (when set to false) or filter out results that have non-null values (when set to true)

| Field                  | Type    |
| :--------------------- | :------ |
| house                  | boolean |
| unit                   | boolean |
| street                 | boolean |
| city                   | boolean |
| state                  | boolean |
| county                 | boolean |
| zip                    | boolean |
| mail\_house            | boolean |
| mail\_unit             | boolean |
| mail\_street           | boolean |
| mail\_city             | boolean |
| mail\_state            | boolean |
| mail\_county           | boolean |
| mail\_zip              | boolean |
| last\_sale\_date       | boolean |
| bedrooms               | boolean |
| bathrooms              | boolean |
| year\_built            | boolean |
| years\_owned           | boolean |
| living\_square\_feet   | boolean |
| building\_square\_feet | boolean |
| stories                | boolean |
| equity\_percent        | boolean |
| properties\_owned      | boolean |
| hoa                    | boolean |

<br />

<br />

In this example I take 2 zips, which in theory could be any arbitrary number of zipcodes, maybe that you pull from a spreadsheet.

```
{
  count: true,
  zip: ["22205", "23857"],
  exclude: [
    { zip: "22205" }
  ]
}
```

The "exclude" field will allow you to manually extract zips from your search without having to course through the entire list.

The field works with other root level fields or compound queries.

Counts:

23857 => 732

22205 => 6,264

Result of above query: 732

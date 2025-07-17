---
title: Compound Queries
excerpt: >-
  Sometimes simple flat queries don't cut it. Fully narrow down your searches
  just the way you want to with our First in Class compound property data
  querying language.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Ever feel frustrated by a Property Search API that can't give you exactly what you want?

We did too! That's why we've designed a unique way of searching across our Nationwide Property Data Sets. 

Just add the "and" field to your Property Search request in order to get more granular with your searches.

```
   const options = {
        "count": false,
        "size": 10,
        
        "and": [
          //all inner 'and'-ed  clauses must be satisfied along with
          //at least one of the 'or'-ed conditions
          //there is no limit to the amount of and/or clauses that can be included

          // conditions that all must be satisfied
          {
              and: [
                  { absentee_owner: true },
                  { beds_min: 3, beds_max: 5 },
                  { corporate_owned: true }
              ]
          },

          // conditions where at least one needs to be satisfied
          {
              or : [
                  { property_type: "LAND" },
                  { property_type: "MOBILE" }
              ]
          }
        ]
    }
```

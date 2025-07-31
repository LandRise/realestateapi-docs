---
title: '"sort" Search Results by Param'
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
The following Property Search fields are sortable:

* years\_owned
* equity\_percent
* year\_built
* building\_size
* lot\_size
* assessed\_value
* last\_sale\_date
* estimated\_equity
* estimated\_value
* assessed\_value
* assessed\_land\_value

Properly forming the "sort" field looks like:

```
{
  sort: {
    years_owned: "asc",
    year_built: "desc"
  }
  
}
```

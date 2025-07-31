---
title: (Pre-)Foreclosure Searches
excerpt: Daily updated pre-foreclosures
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Pre-Foreclosure

* basic pre\_foreclosure search

```
let request = {
  size: 200,
  pre_foreclosure: true,
  city: 'San Francisco',
  state: 'CA'
}

//with notice_type


//with notice_type & search_range

```

* Find **NODs** (Notice of Default) in the last month

```
let request = {
  size: 200,
  pre_foreclosure: true,
  notice_type: "NOD",
  search_range: "1_MONTH",
  city: 'San Francisco',
  state: 'CA'
}
```

* Use **pre\_foreclosure\_date\_min** & **pre\_foreclosure\_date\_max** in place of "search\_range" to be more precise with your date range (November 2023 in this example)

```
let request = {
  size: 200,
  pre_foreclosure: true,
  notice_type: "NOD",
  pre_foreclosure_date_min: "2023-11-01",
  pre_foreclosure_date_max: "2023-11-31",
  city: 'San Francisco',
  state: 'CA'
}
```

### Foreclosure

```
//basic
let request = {
  size: 200,
  foreclosure: true,
  city: 'San Francisco',
  state: 'CA'
}

//with notice_type


//with notice_type & search_range

```

### REO

* Find Banked Owned Properties

```
let request = {
  size: 50,
  reo: true,
  city: 'Boise',
  state: 'ID'
}
```

* With a Time Range - searches over foreclosures and document types that reflect purchase by bank, trust, service entity, or tax entity

```
let request = {
  size: 50,
  reo: true,
  search_range: "6_MONTH",
  city: 'Boise',
  state: 'ID'
}
```

### Auction

* basic auction search

```
let request = {
  size: 50,
  auction: true,
  city: 'Boise',
  state: 'ID'
}
```

* auction search with time range to find timely auctions

```
let request = {
  size: 50,
  auction: true,
  search_range: "1_MONTH",
  city: 'Boise',
  state: 'ID'
}
```

* auction with exact date range

```
let request = {
  size: 50,
  auction: true,
  auction_date_min: "2023-12-20",
  auction_date_max: "2024-01-10",
  city: 'Boise',
  state: 'ID'
}
```

### Document Types

For more specific document type searches to go along with these fields, please visit [Document Types Reference](https://beta.realestateapi.com/reference/document-type-codes)

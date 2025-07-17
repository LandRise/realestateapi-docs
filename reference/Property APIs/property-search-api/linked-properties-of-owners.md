---
title: Linked Properties & Portfolio Searches
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
## Find by Size of Portfolio

"properties\_owned\_min" & "properties\_owned\_max" are used to find owners with a certain quantity of properties

```
{
  "properties_owned_min": 10,
  "properties_owned_max": 50
}
```

## Active Buyer Discovery through Linked Properties

Search for active buyers by looking at linked properties' sale dates within the last 6 and 12 months.

```
{
  "size": 50,
  "state": "OK",
  "portfolio_purchased_last12_min": 5,
  "portfolio_purchased_last12_max": 10
}
```

<br />

## Find by Nominal Value of Portfolio

* Find the whales based on total portfolio property value

```
{
  "portfolio_value_min": 10000000, //10 Million 
  "portfolio_value_max": 75000000 //75 Million
}
```

## Find by Equity Amounts Owned Across Portfolio

* could combine with the nominal value filters to find total size and find portfolio owners that have plenty of equity or may be in an equity pinch

```
{
  "portfolio_equity_min": 5000000, //5M
  "portfolio_equity_max": 25000000 //25M
}
```

## Find by Remaining Mortgage Balance of an Owner's Portfolio

* could combine with an adjustable\_rate: true search & find tired landlords that may be pressured by interest rates to unload their portfolio given large outstanding mortgage balances

```
{
  "portfolio_mortgage_balance_min": 10000000, //10M
  "portfolio_mortgage_balance_max": 50000000 //50M
}
```
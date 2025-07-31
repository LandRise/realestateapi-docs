---
title: Buyer Searches
excerpt: Find different types of buyers based on our Extensive Transaction Data
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Cash Buyers Search

These would be properties that look like they were all cash transactions.

```
{
  cash_buyer: true
}
```

## Private Lenders Search

These would be properties where it looks like the deals were completed by a private/hard money lender

```
{
  private_lender: true
}
```

## Investor Buyers Search

Similar to cash_buyer, this adds an additional filter to only include properties where the buyer has a different mailing address than the property.

```
{
  investor_buyer: true
}
```

For more deterministic searching:

## Properties Owned Search

Find larger or institutional buyers using our linked properties and properties owned searches.

properties_owned_min: `[some number]`  
This will bring back properties where the current owner has a portfolio of properties greater than or equal to the number you specify.

You can couple that with  
properties_owned_max: `[some maximum number of properties owned]`  
This will allow you to create a range if say you want to focus on smaller landlords that aren't hedgefunds. Or the reverse - find potential hedge fund buyers by setting the minimum number higher.

```
{
  properties_owned_min: 10,
  properties_owned_max: 50
}
```

In either case, inspect the linkedProperties object to get total portfolio value as well.

```
for (let result of results) {
  console.log('linked properties: ', result.linkedProperties);
}
```

Go here for a few more examples that also sort by the Buyer's Portfolio size, equity, or mortgage balance remaining: [https://developer.realestateapi.com/reference/linked-properties-of-owners](https://developer.realestateapi.com/reference/linked-properties-of-owners)

## Flipped Property Buyers

You can also filter on possible flips by searching based on how long the prior owner owned a property:

```
{
  prior_owner_months_owned_min: 6,
  prior_owner_months_owned_max: 18
}
```

You can combine this with sales that occurred recently to try to find prior owners who meet this criteria.  
last_sale_date_min: `[set to some recent date 'YYYY-MM-DD']`  
You'd inspect the salesHistory object to get the prior owner's information.

So you can look at sales within a given window to try and determine flips.

<br />

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
---
title: .taxInfo
excerpt: Get basic Tax Assessor Data Points across the nation
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## assessedValue

The "assessedValue" field inside of *.taxInfo* will give you the assessed value of the property as deemed by the county assessor's office.

Check the "assessmentYear" inside of *.taxInfo* for when the "assessedValue" was last updated.

<br />

## taxAmount

Need to know the **property taxes** set by the county for a given property? Look no further than the "taxAmount" field inside of *.taxInfo*

<br />

## taxDelinquentYear & Estimating Delinquent Amount

You can filter for properties that have tax delinquencies using the following filters on Property Search:

* tax\_delinquent\_year\_min / tax\_delinquent\_year\_max

Once we have a property where we see "taxDelinquentYear" field set inside of *.taxInfo*, you'll be able to establish an estimated range for how much is owed.

Example:

(taxDelinquentYear = 2023) [current date = October 2024]

* low end estimate => (end of 2023 filed ) => (0-2 months of 2023 *some fraction of taxAmount) + (10 months of 2024* 0.83taxAmount)
* high end estimate => (beginning of 2023 filed ) => ( 12 months (of 2023) *taxAmount ) + ( 10 months of 2024* 0.83taxAmount ) 

<br />

Notes:

* Limitation: different counties have different reporting standards on tax delinquency (for when they are initially becoming delinquent AND after they may have paid off their tax liability) - some one month, some every quarter, some every 6 months, and some once a year. 
* Limitation: actual payments made on a tax delinquency are not shown as that data is Credit related and not readily accessible. To see if a property eventual leaves tax delinquency status, you would have to monitor it along the county update schedule for tax delinquents for the specific county.

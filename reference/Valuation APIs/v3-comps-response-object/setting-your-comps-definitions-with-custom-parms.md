---
title: Setting Your Comps Definitions with Custom Parms
excerpt: >-
  Use our custom parameters for generating the most accurate comps for your
  market and your use case
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Custom Param
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Fields to Use
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        armsLength
      </td>

      <td style={{ textAlign: "left" }}>
        If set to true, this will grab only sales that have the "lastSale.transactionType" of arms length (check all the txn types we support: [https://developer.realestateapi.com/reference/transaction-types](https://developer.realestateapi.com/reference/transaction-types))
      </td>

      <td style={{ textAlign: "left" }}>
        armsLength: true
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        baths
      </td>

      <td style={{ textAlign: "left" }}>
        Use Case: subject property has 3 bathrooms; I want to find comps that have at most 5 baths, and at least 3 baths.  

        bathrooms\_min: 3, bathrooms\_max: 5, bathrooms\_boost: 50
      </td>

      <td style={{ textAlign: "left" }}>
        bathrooms\_min, bathrooms\_max, bathrooms\_boost
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        same\_baths
      </td>

      <td style={{ textAlign: "left" }}>
        If set to true, will only grab comps with the same number of bathrooms
      </td>

      <td style={{ textAlign: "left" }}>
        same\_baths: true
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        beds
      </td>

      <td style={{ textAlign: "left" }}>
        Use Case: subject property has 3 bedrooms; I want to find comps that have at most 5 beds, and at least 3 beds  

        bedrooms\_min: 3, bedrooms\_max: 5, bedrooms\_boost: 50
      </td>

      <td style={{ textAlign: "left" }}>
        bedrooms\_min, bedrooms\_max, bathrooms\_boost
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        same\_beds
      </td>

      <td style={{ textAlign: "left" }}>
        If set to true, will only grab comps with the same number of bedrooms
      </td>

      <td style={{ textAlign: "left" }}>
        same\_beds: true
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        livingSqureFeet
      </td>

      <td style={{ textAlign: "left" }}>
        Use Case: subject property has 2500 living sqft; I want to find comps that have at most 4000 living sqft, and at least 1800 sqft  

        living\_square\_feet\_min: 1800, living\_square\_feet\_max: 4000, living\_square\_feet\_boost: 50
      </td>

      <td style={{ textAlign: "left" }}>
        living\_square\_feet\_min, living\_square\_feet\_max, living\_square\_feet\_boost
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        lotSquareFeet
      </td>

      <td style={{ textAlign: "left" }}>
        Use Case: subject property has a lot size of 5000 sqft; I want to find comps that have lots that are at most 10000 sqft, and at least 4000 sqft  

        lot\_square\_feet\_min: 1800, lot\_square\_feet\_max: 4000, lot\_square\_feet\_boost: 50
      </td>

      <td style={{ textAlign: "left" }}>
        lot\_square\_feet\_min, lot\_square\_feet\_max, lot\_square\_feet\_boost
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        yearBuilt
      </td>

      <td style={{ textAlign: "left" }}>
        Use Case: only want to get comps that were built after 1980  

        year\_built\_min: 1980, year\_built\_max: 2024, year\_built\_boost: 50
      </td>

      <td style={{ textAlign: "left" }}>
        year\_built\_min, year\_built\_max, year\_built\_boost
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        lastSalePrice
      </td>

      <td style={{ textAlign: "left" }}>
        Use Case: if you know your expected value range of the comps ahead of time  

        last\_sale\_price\_min: 500000, last\_sale\_price\_max: 750000
      </td>

      <td style={{ textAlign: "left" }}>
        last\_sale\_price\_min, last\_sale\_price\_max
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        mlsListingPrice
      </td>

      <td style={{ textAlign: "left" }}>
        Use Case: having issues with non-disclosure state last sale price reporting when generating list of comps  

        mls\_listing\_price\_min: 500000, mls\_listing\_price\_max: 750000
      </td>

      <td style={{ textAlign: "left" }}>
        mls\_listing\_price\_min, mls\_listing\_price\_max
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

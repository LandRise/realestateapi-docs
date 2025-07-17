---
title: Address Verification Response Schema
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
| Parent      | REAPI Field Name      | Type     | Field Description                                                                                                                   |
| :---------- | :-------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| root        | id                    | integer  | our unique property Identifer                                                                                                       |
| root        | propertyId            | string   | our unique property Identifer (as String)                                                                                           |
| root        | vacant                | boolean  | Indicates if the property is currently vacant.                                                                                      |
| root        | absenteeOwner         | boolean  | Indicates if the owner of the property is not residing in it.                                                                       |
| root        | apn                   | string   | Assessor's Parcel Number assigned by the county assessor.                                                                           |
| root        | latitude              | float    | Latitude of the property's location.                                                                                                |
| root        | longitude             | float    | Longitude of the property's location.                                                                                               |
| root        | lotNumber             | string   | Lot number assigned to the property.                                                                                                |
| root        | propertyUse           | string   | Actual use of the property (e.g., single-family residence, rental).                                                                 |
| root        | precision             | string   | Level of accuracy for latitude/longitude values (most are zip9)                                                                     |
| root        | searchType            | string   | A searchType of “A” indicates that the property being verified is a full address                                                    |
| root        | match                 | boolean  | Indicates if a matching address in our system was found for the address provided                                                    |
| root        | confidence            | float    | A score ranging from 0 to 1 that provides info on the statistical strength of the match. Matches only provided for confidence > .85 |
|             |                       |          |                                                                                                                                     |
| address     | fips                  | string   | Federal Information Processing Standards code for the property's location.                                                          |
|             | house                 | string   | House number of the property address.                                                                                               |
|             | address               | string   | Full address of the property.                                                                                                       |
|             | street                | string   | Street name of the property address.                                                                                                |
|             | preDirection          | string   | Directional prefix for the street name (e.g., N, S, E, W).                                                                          |
|             | streetType            | string   | Type of street (e.g., Avenue, Street, Boulevard).                                                                                   |
|             | unit                  | string   | Unit number of the property address.                                                                                                |
|             | unitType              | string   | Type of unit (e.g., apartment, suite).                                                                                              |
|             | city                  | string   | City where the property is located.                                                                                                 |
|             | county                | string   | County where the property is located.                                                                                               |
|             | state                 | string   | State where the property is located (state codes used: VA, MD, NC)                                                                  |
|             | zip                   | string   | ZIP code of the property address.                                                                                                   |
|             | zip4                  | string   | Extended ZIP+4 code for more precise delivery.                                                                                      |
|             | carrierRoute          | string   | Carrier route associated with the property address.                                                                                 |
|             | congressionalDistrict | integer  | Congressional district where the property is located.                                                                               |
|             | label                 | string   | Label or tag for the address, typically for internal use.                                                                           |
|             |                       |          |                                                                                                                                     |
| mailAddress | fips                  | string   | Federal Information Processing Standards code for the property's location.                                                          |
|             | house                 | string   | House number of the property address.                                                                                               |
|             | address               | string   | Full address of the property.                                                                                                       |
|             | street                | string   | Street name of the property address.                                                                                                |
|             | preDirection          | string   | Directional prefix for the street name (e.g., N, S, E, W).                                                                          |
|             | streetType            | string   | Type of street (e.g., Avenue, Street, Boulevard).                                                                                   |
|             | unit                  | string   | Unit number of the property address.                                                                                                |
|             | unitType              | string   | Type of unit (e.g., apartment, suite).                                                                                              |
|             | city                  | string   | City where the property is located.                                                                                                 |
|             | county                | string   | County where the property is located.                                                                                               |
|             | state                 | string   | State where the property is located.                                                                                                |
|             | zip                   | string   | ZIP code of the property address.                                                                                                   |
|             | zip4                  | string   | Extended ZIP+4 code for more precise delivery.                                                                                      |
|             | carrierRoute          | string   | Carrier route associated with the property address.                                                                                 |
|             | addressFormat         | string   | Formatted address for mailing purposes.                                                                                             |
|             | label                 | string   | Label or tag for the address, typically for internal use.                                                                           |
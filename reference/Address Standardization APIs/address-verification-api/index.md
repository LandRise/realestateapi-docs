---
title: Address Verification API
excerpt: Verify 1 - 100 addresses at a time.
api:
  file: property-apis.json
  operationId: address-verification-api
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# What is a "Valid" Property?

* A verified property is a REAPI recognized physical property
  * known structure with a unique property identifier
  * mailing addresses provided for nearly all verified addresses
* Addresses that cannot be "valid":
  * P. O. Boxes
  * Land parcels without physical structures
* Confidence Scores
  * Just because an address gets rejected with a "match: false" doesn't mean we didn't find anything that couldn't be a match
  * We only return a match when our machine learning algos have 100% determined that the address provided can be confidently verified with the correct property in our system
  * Only confidence scores of .88 or above will yield a match property in the response data

# Request Requirements

Submit an **addresses** array with a combination of:

* **street, city, state and zip**
* **street and zip**, city and state are not required in this case
* **address**, the separate street, city, state and zip fields are not required in this case

# Max Size per API Call

* The max amount of addresses per call is 100

# The "key" to mapping your response data

* using the "key" field on the objects in the "addresses" array will allow you to map your input data to your output data easily, address by address

# Error Handling

* Every address inside of the "addresses" array will be treated independent of the other addresses. This allows us to fail individual address objects and still return a 200 response with the output data for all the addresses that could be validated properly. 
* Each address could be failed with any of the following: 404 (Not Found) - address does not exist in our data warehouse; 400 (Bad Request) - the address is not parseable by our system without manual revision of the address provided
* If you are experiencing an "error" and "errorMessage" property on all of your result objects, then try to clean your data according to rules for this endpoint that allow addresses to be processed properly

# Data Normalization/Standardization

* in the response, street types in full provided as input will be returned in short-form with initial capitals casing with no periods
  * e.g. "Street" => "St"
* Includes commas after "address.label" & "address.city"
* pre- & post- directions in the address will only have the first character as capital (Northwest => Nw; NW => Nw)
* Partial addresses get filled on response data
  * "123 Main S", the incomplete string will still returned match and present as "123 Main St" in the response data
* As long as all address parts are detected as present, there is a bit of leeway with things such as whitespace, mispelling, incompleteness, extra characters, etc.
  * e.g. "4508 Nw 48ht Str.   eet, Olkaho  a       Citty, OK        73107" could be valid
  * and as always the response data would normalize this input to something like: "4508 Nw 48th St, Oklahoma City, OK 73107"

# Enriching your Verified Addresses

## Using the REAPI property "id"

* one of the benefits to RealEstateAPI is tying all of your data together with our unique property ids. Once your address is verified by us, there's so much more we can do!
* create an array of the property ids on the response objects and feed into **Property Detail Bulk API** as input and get the full property details (mortgages, sales history, tax info, etc.) on every verified address

## SkipTracing Verified Addresses

* once your addresses have been verified, don't forget to enrich them with the [SkipTrace API](https://developer.realestateapi.com/reference/bulk-skiptrace-api)

---
title: RealEstateAPI Developer Documentation
excerpt: >-
  THE Property Data Solution. Our revolutionary tech allows us to get you
  property and owner data (and lots of it!) faster and cheaper than you've ever
  been able to before.  Slow or buggy applications due to unreliable third party
  data APIs are a problem of the past.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# What We Do

* [x] **Simple APIs** — most of our APIs only take minutes to set up. Get a test API key and start using our generous free tier to try out our various data offerings. If you need any help getting anything implemented, you can make use of our daily onboarding sessions with our Developer Advocates

* [x] **Big Data(warehousing) as a Service** — has your organization ever faced the daunting task of building out your internal or customer facing data operations? Our data subscriptions offer a level of access akin to having your own in-house data warehouse. Building out your own data infrastructure takes a lot of time and resources; save yourself the headache and build with RealEstateAPI for a fraction of the cost

* [x] **Onboarding and White Glove Service** — and it doesn't cost a dime. Get working code samples from our devs and an hour of their time anytime you want. Our bookings can range in topics from help with API implementation details and Webhook Servers for the bulk endpoints to general application architecture, UI design, building out a low code integration or plugin, and feature idea brainstorming with our data. 

* [x] **Low Code Integrations and Beyond** —  using Bubble, WordPress, Wix or other similar sites to host your application? Using SalesForce, Zapier, GoogleSheets or other tools internally? Let us help you integrate the property or contact data your business needs regardless of what tools or current processes you have. We are expanding our integration offerings weekly to cut your integration times. Submit integration ideas to our team at [dev@realestateapi.com](mailto:dev@realestateapi.com)

* [x] **Bulk Data Lists** — tap into the power of our machine learning capabilities with custom property lists. Choose what property or owner characteristics you want to focus on and let the algo go to work. Whether you're looking for owner propensity to sell or the perfect house to get a hedge fund cash buyer interested, our ML models will provide unparalleled realtime data insights and predictions. 

# Our API Offerings

## Mapping APIs

### Property Boundary API

* find the geo-point (lat/lng coordinates) and latitude/longitude boundaries for a specific property parcel/address (WKT)

### Mapping ("Pins") API

* endpoint that'll let you give the best map experience to users
* provides unlimited pin locations matching your search criteria for unlimited user searches

<br />

## Valuation APIs

### Property Comps API

#### v2 - basic comparables API with single AVM

* find nearby properties with similar characteristics and valuations to the one provided. Results include Sale Dates, Sale Amounts, Lenders and more!

#### v3 (BETA) - advanced comparables API with AVM range and more sophisticated algorithm

* utilize custom parameters along with the address provided to create precise definitions to help automate your internal comping engines or processes
* customizable on living square feet, lot square feet, # of bedrooms, # of bathrooms, and year built

### Lender Grade AVM API

* reap the benefits our multi-model approach to generating accurate valuations for properties
* returns a valuation range & statistical confidence scores so you know how reliable your regularly updated valuations are

<br />

<br />

## Property APIs

### Property Search API

* Select a Geo: search properties by city, state, county, zip, latitude/longitude+radius, polygons, multiple polygons, Fips, or neighborhood name
* Pick Property Types: SFRs, MFRs, Land, Condos, Mobile Homes and Commercial Properties
* On or Off Market? Supports MLS searches or more broad searches for off-market properties
* Powerful Modes: Such as "count" mode to get the total number of matching properties based on your query before deciding to fetch them. "ids\_only" mode allows you to work with the Property Detail Bulk API to get the full set of data points for 1000s+ properties / second; perfect for batch jobs and lead generation at scale.
* Plethora of Filters: searchability on data points across lot, building, owner, and area characteristics (incl. schools & neighborhood info)
* Compound Queries - need more expressiveness to retrieve the exact properties you need with multiple clauses of logic? Look no further than our nested statements syntax.

### Property Detail API

* MLS Listing, Pending, and Cancellation History
* Mortgage History and Current Mortgages
* Sales History
* Building Specs
* Property Owner Info & Mailing Addresses
* Tax Information & Property Valuations
* Property Comps (comps: true)
* Foreclosures
* Lot Information
* Schools
* Neighborhood Info
* Median Income & Suggested Rents of Area

### Property Detail Bulk API

* get the full schema results for your Property Search API responses (using ids\_only: true)
* Supports up to 1000 property IDs per request

### AutoComplete API

* unlimited use for free for any monthly data subscribers
  * save on or remove your Google AutoComplete Bills immediately!
* power your application with user driven search
* supports seamless detection on a number of real estate specific contexts such as:
  * city/state
  * county name
  * Full Address (Google AutoComplete equivalent mode)
  * Neighborhood name
  * entire state
  * zipcode
  * APN for land parcels

### Address Verification API

* Sync and validate your internal property database with ours to ensure best results with our other APIs
* Helps avoid writing complicated address logic to standardize or normalize your address formatting by using ours after we match it

### PropGPT API

* Use natural language queries to run searches on our Property Search API

<br />

### CSV Generator APIs

* *Property Search CSV Generator*
  * Turn your Property Search API calls into downloadable CSV files

***

## Skip Trace APIs

* *Skiptrace API* 
  * find contact phone numbers, emails, and social media profiles by providing a name and address
* *Bulk Skiptrace API* 
  * find phone numbers, emails, and social media profiles for a list of up to 1,000 contacts in one API call
* *Bulk Skiptrace Await API*
  * different architectures and designs call for different solutions. If you don't feel like setting up webhooks, you can easily get batches of skips run in an async/await style. The max records is lower but will be quicker to implement for POCs!

***

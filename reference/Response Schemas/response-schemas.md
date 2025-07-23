# Real Estate API v2 Response Schemas

This document provides comprehensive documentation of all response schemas for the Real Estate API v2 endpoints. This documentation is structured for both developers and RAG (Retrieval-Augmented Generation) systems to understand the data structures returned by each API endpoint.

## Table of Contents

1. [AddressVerificationAPI](#addressverificationapi)
2. [AutoCompleteAPI](#autocompleteapi)
3. [MLSDetailAPI](#mlsdetailapi)
4. [MLSSearchAPI](#mlssearchapi)
5. [PropGPTAPI](#propgptapi)
6. [PropertyAvmAPI](#propertyavmapi)
7. [PropertyAvmBulkAPI](#propertyavmbulkapi)
8. [PropertyCsvBuilderAPI](#propertycsvbuilderapi)
9. [PropertyDetailAPI](#propertydetailapi)
10. [PropertyDetailBulkAPI](#propertydetailbulkapi)
11. [PropertyLiensAPI](#propertyliensapi)
12. [PropertyMappingAPI](#propertymappingapi)
13. [PropertySearchAPI](#propertysearchapi)

---

## AddressVerificationAPI

**API Endpoint:** `POST /v2/AddressVerification`

**Description:** Verify addresses in bulk

**Business Purpose:** This API validates and standardizes addresses, providing property matches with confidence scores. It's used for address validation, property identification, and data quality assurance.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `data` | Array | Array of address verification results |
| `data[].input` | Object | The input parameters used for the request |
| `data[].id` | Number/null | The property ID |
| `data[].propertyId` | String/null | The property ID as a string |
| `data[].address` | Object/null | Property address information |
| `data[].address.fips` | String/null | FIPS code |
| `data[].address.house` | String/null | House number |
| `data[].address.address` | String/null | Full address |
| `data[].address.street` | String/null | Street name |
| `data[].address.preDirection` | String/null | Pre-direction (e.g., N, S, E, W) |
| `data[].address.streetType` | String/null | Street type (e.g., St, Ave, Blvd) |
| `data[].address.unit` | String/null | Unit number |
| `data[].address.unitType` | String/null | Unit type (e.g., Apt, Suite) |
| `data[].address.city` | String/null | City |
| `data[].address.county` | String/null | County |
| `data[].address.state` | String/null | State |
| `data[].address.zip` | String/null | ZIP code |
| `data[].address.zip4` | String/null | ZIP+4 code |
| `data[].address.carrierRoute` | String/null | Carrier route |
| `data[].address.congressionalDistrict` | String/null | Congressional district |
| `data[].address.label` | String/null | Address label |
| `data[].mailAddress` | Object/null | Mailing address information |
| `data[].mailAddress.fips` | String/null | FIPS code |
| `data[].mailAddress.house` | String/null | House number |
| `data[].mailAddress.address` | String/null | Full address |
| `data[].mailAddress.street` | String/null | Street name |
| `data[].mailAddress.preDirection` | String/null | Pre-direction (e.g., N, S, E, W) |
| `data[].mailAddress.streetType` | String/null | Street type (e.g., St, Ave, Blvd) |
| `data[].mailAddress.unit` | String/null | Unit number |
| `data[].mailAddress.unitType` | String/null | Unit type (e.g., Apt, Suite) |
| `data[].mailAddress.city` | String/null | City |
| `data[].mailAddress.county` | String/null | County |
| `data[].mailAddress.state` | String/null | State |
| `data[].mailAddress.zip` | String/null | ZIP code |
| `data[].mailAddress.zip4` | String/null | ZIP+4 code |
| `data[].mailAddress.carrierRoute` | String/null | Carrier route |
| `data[].mailAddress.addressFormat` | String/null | Address format |
| `data[].mailAddress.label` | String/null | Address label |
| `data[].vacant` | Boolean/null | Indicates if the property is vacant |
| `data[].absenteeOwner` | Boolean/null | Indicates if the owner is absentee |
| `data[].apn` | String/null | Assessor Parcel Number |
| `data[].latitude` | String/Number/null | Latitude coordinate |
| `data[].longitude` | String/Number/null | Longitude coordinate |
| `data[].lotNumber` | String/null | Lot number |
| `data[].propertyUse` | String/null | Property use |
| `data[].precision` | String/null | Precision level of the address match |
| `data[].searchType` | String/null | Type of search performed |
| `data[].match` | Boolean | Indicates if the address was matched |
| `data[].confidence` | Number | Confidence score of the match |
| `data[].error` | Boolean | Indicates if an error occurred (error responses only) |
| `data[].errorMessage` | String | Error message (error responses only) |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `matchCount` | Number | The number of successful matches |
| `live` | Boolean | Indicates if the request was made with a live API key |
| `requestExecutionTimeMS` | String | The time taken to execute the request |
| `addressVerificationExecutionTimeMS` | String/null | The time taken to execute the address verification |

---

## AutoCompleteAPI

**API Endpoint:** `POST /v2/AutoComplete`

**Description:** Get a list of property detail results

**Business Purpose:** This API provides autocomplete functionality for property searches, allowing users to quickly find properties by partial address, city, county, or other location-based criteria.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `input` | Object | The input parameters used for the request |
| `input.search` | String | The search text |
| `input.search_types` | String/Array | The types of search to perform |
| `input.latitude` | Number | Latitude coordinate for location-based search |
| `input.longitude` | Number | Longitude coordinate for location-based search |
| `input.precision` | Number | Precision level for coordinates |
| `data` | Array | The autocomplete results |
| `data[].id` | String/null | Property ID |
| `data[].apn` | String/null | Assessor Parcel Number |
| `data[].state` | String/null | State code |
| `data[].stateId` | String/null | State ID |
| `data[].stateName` | String/null | State name |
| `data[].zip` | String/null | ZIP code |
| `data[].county` | String/null | County name |
| `data[].countyId` | String/null | County ID |
| `data[].city` | String/null | City name |
| `data[].house` | String/null | House number |
| `data[].street` | String/null | Street name |
| `data[].searchType` | String/null | Type of search result |
| `data[].address` | String/null | Full address |
| `data[].fips` | String/null | FIPS code |
| `data[].latitude` | Number/null | Latitude coordinate |
| `data[].longitude` | Number/null | Longitude coordinate |
| `data[].title` | String/null | Display title |
| `data[].location` | String/null | Location description |
| `totalResults` | Number | The total number of results available |
| `returnedResults` | Number | The number of results returned |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `live` | Boolean | Indicates if the request was made with a live API key |
| `requestExecutionTimeMS` | String | The time taken to execute the request |

---

## MLSDetailAPI

**API Endpoint:** `POST /v2/MLSDetail`

**Description:** Retrieve detailed MLS information for a specific property using its MLS number, ID, or address

**Business Purpose:** This API provides comprehensive MLS (Multiple Listing Service) property details including listing information, agent details, property features, and pricing history.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `live` | Boolean | Indicates if the request was made with a live API key |
| `input` | Object | The input parameters used for the request |
| `data` | Object | The data returned from the API |
| `data.listingId` | Number/null | The listing ID |
| `data.reapiId` | String/null | The REAPI ID |
| `data.courtesyOf` | String/null | Courtesy information |
| `data.customStatus` | String/null | Custom status of the listing |
| `data.daysOnMarket` | Number/null | Number of days the property has been on the market |
| `data.standardStatus` | String/null | Standard status of the listing |
| `data.hasPhotos` | Boolean/null | Indicates if the listing has photos |
| `data.isListed` | Boolean/null | Indicates if the property is currently listed |
| `data.listingAgentEmailAddress` | String/null | Email address of the listing agent |
| `data.listingContractDate` | String/null | Date of the listing contract |
| `data.listPrice` | Number/null | List price of the property |
| `data.mlsNumber` | String/null | MLS number |
| `data.mlsBoardCode` | String/null | MLS board code |
| `data.modificationTimestamp` | String/null | Timestamp of the last modification |
| `data.priceChangeTimestamp` | String/null | Timestamp of the last price change |
| `data.pricePerSqFt` | Number/null | Price per square foot |
| `data.publicRemarks` | String/null | Public remarks about the property |
| `data.sellingOfficeName` | String/null | Name of the selling office |
| `data.soldDate` | String/null | Date the property was sold |
| `data.url` | String/null | URL to the listing |
| `data.homedetails` | Object/null | Home details |
| `data.homedetails.appliances` | Array/null | Appliances included with the property |
| `data.homedetails.associationFeeFrequency` | String/null | Frequency of association fee payments |
| `data.homedetails.cooling` | String/null | Cooling system information |
| `data.homedetails.directions` | String/null | Directions to the property |
| `data.homedetails.exteriorFeatures` | String/null | Exterior features of the property |
| `data.homedetails.fireplacesTotal` | Number/null | Total number of fireplaces |
| `data.homedetails.fireplaceYn` | Boolean/null | Indicates if the property has a fireplace |
| `data.homedetails.flooring` | String/null | Flooring information |
| `data.homedetails.heating` | String/null | Heating system information |
| `data.homedetails.lotFeatures` | String/null | Features of the lot |
| `data.homedetails.lotSizeAcres` | Number/null | Lot size in acres |
| `data.homedetails.lotSizeArea` | Number/null | Lot size area |
| `data.homedetails.roof` | String/null | Roof information |
| `data.homedetails.sewer` | String/null | Sewer information |
| `data.homedetails.taxAmount` | Number/null | Tax amount |
| `data.homedetails.watersource` | String/null | Water source information |
| `data.homedetails.zoning` | String/null | Zoning information |
| `data.address` | Object/null | Property address |
| `data.address.city` | String/null | City |
| `data.address.countyOrParish` | String/null | County or parish |
| `data.address.stateOrProvince` | String/null | State or province |
| `data.address.unparsedAddress` | String/null | Unparsed address |
| `data.address.zipCode` | String/null | ZIP code |
| `data.property` | Object/null | Property details |
| `data.property.associationFee` | Number/null | Association fee |
| `data.property.bathroomsText` | String/null | Bathrooms text description |
| `data.property.bathroomsHalf` | Number/null | Number of half bathrooms |
| `data.property.bathroomsTotal` | Number/null | Total number of bathrooms |
| `data.property.bedroomsTotal` | Number/null | Total number of bedrooms |
| `data.property.garageSpaces` | String/Number/null | Number of garage spaces |
| `data.property.hasBasement` | Boolean/null | Indicates if the property has a basement |
| `data.property.hasPool` | Boolean/null | Indicates if the property has a pool |
| `data.property.isCityView` | Boolean/null | Indicates if the property has a city view |
| `data.property.isMountainView` | Boolean/null | Indicates if the property has a mountain view |
| `data.property.isParkView` | Boolean/null | Indicates if the property has a park view |
| `data.property.isWaterfront` | Boolean/null | Indicates if the property is waterfront |
| `data.property.isWaterview` | Boolean/null | Indicates if the property has a water view |
| `data.property.latitude` | Number/null | Latitude coordinate |
| `data.property.livingArea` | Number/null | Living area square footage |
| `data.property.location` | Array/null | Location coordinates [longitude, latitude] |
| `data.property.longitude` | Number/null | Longitude coordinate |
| `data.property.lotSizeSquareFeet` | Number/null | Lot size in square feet |
| `data.property.neighborhood` | String/null | Neighborhood |
| `data.property.propertySubType` | String/null | Property sub-type |
| `data.property.propertyType` | String/null | Property type |
| `data.property.stories` | String/Number/null | Number of stories |
| `data.property.subdivisionName` | String/null | Subdivision name |
| `data.property.yearBuilt` | Number/null | Year the property was built |
| `data.schools` | Object/null | School information |
| `data.schools.elementarySchool` | String/null | Elementary school |
| `data.schools.highSchool` | String/null | High school |
| `data.schools.middleOrJuniorSchool` | String/null | Middle or junior school |
| `data.schools.schoolDistrict` | String/null | School district |
| `data.media` | Array/null | Media associated with the listing |
| `data.listingAgent` | Object/null | Listing agent information |
| `data.listingAgent.email` | String/null | Email of the listing agent |
| `data.listingAgent.firstName` | String/null | First name of the listing agent |
| `data.listingAgent.fullName` | String/null | Full name of the listing agent |
| `data.listingAgent.lastName` | String/null | Last name of the listing agent |
| `data.listingAgent.mlsAgentId` | String/null | MLS agent ID |
| `data.listingAgent.mlsCode` | String/null | MLS code |
| `data.listingAgent.phone` | String/null | Phone number of the listing agent |
| `data.listingOffice` | Object/null | Listing office information |
| `data.listingOffice.address` | String/null | Address of the listing office |
| `data.listingOffice.city` | String/null | City of the listing office |
| `data.listingOffice.email` | String/null | Email of the listing office |
| `data.listingOffice.mlsCode` | String/null | MLS code |
| `data.listingOffice.mlsOfficeId` | String/null | MLS office ID |
| `data.listingOffice.name` | String/null | Name of the listing office |
| `data.listingOffice.phone` | String/null | Phone number of the listing office |
| `data.listingOffice.postalCode` | String/null | Postal code of the listing office |
| `data.listingOffice.stateOrProvince` | String/null | State or province of the listing office |
| `data.listingOffice.websiteUrl` | String/null | Website URL of the listing office |
| `data.sellingAgent` | Object/null | Selling agent information |
| `data.sellingAgent.email` | String/null | Email of the selling agent |
| `data.sellingAgent.firstName` | String/null | First name of the selling agent |
| `data.sellingAgent.fullName` | String/null | Full name of the selling agent |
| `data.sellingAgent.lastName` | String/null | Last name of the selling agent |
| `data.sellingAgent.mlsAgentId` | String/null | MLS agent ID |
| `data.sellingAgent.mlsCode` | String/null | MLS code |
| `data.sellingAgent.phone` | String/null | Phone number of the selling agent |
| `data.sellingOffice` | Object/null | Selling office information |
| `data.sellingOffice.address` | String/null | Address of the selling office |
| `data.sellingOffice.city` | String/null | City of the selling office |
| `data.sellingOffice.email` | String/null | Email of the selling office |
| `data.sellingOffice.mlsCode` | String/null | MLS code |
| `data.sellingOffice.mlsOfficeId` | String/null | MLS office ID |
| `data.sellingOffice.name` | String/null | Name of the selling office |
| `data.sellingOffice.phone` | String/null | Phone number of the selling office |
| `data.sellingOffice.postalCode` | String/null | Postal code of the selling office |
| `data.sellingOffice.stateOrProvince` | String/null | State or province of the selling office |
| `data.sellingOffice.websiteUrl` | String/null | Website URL of the selling office |
| `recordCount` | Number | The number of records returned |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `errorMessage` | String | Error message if applicable |
| `warning` | String | Warning message if applicable |
| `requestExecutionTimeMS` | String | The time taken to execute the request |

---

## MLSSearchAPI

**API Endpoint:** `POST /v2/MLSSearch`

**Description:** MLS Search API

**Business Purpose:** This API provides comprehensive MLS property search capabilities with advanced filtering options, agent information, and property details for real estate professionals and investors.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `live` | Boolean | Indicates if the request was made with a live API key |
| `input` | Object | The input parameters used for the request |
| `data` | Array | The data returned from the API |
| `data[].listingId` | Number/null | The listing ID |
| `data[].id` | String/null | The ID |
| `data[].modificationTimestamp` | String/null | Timestamp of the last modification |
| `data[].listing` | Object/null | Listing information |
| `data[].listing.courtesyOf` | String/null | Courtesy information |
| `data[].listing.customStatus` | String/null | Custom status of the listing |
| `data[].listing.hasPhotos` | Boolean/null | Indicates if the listing has photos |
| `data[].listing.internetAddressDisplayYN` | Boolean/null | Indicates if the address is displayed on the internet |
| `data[].listing.isListed` | Boolean/null | Indicates if the property is currently listed |
| `data[].listing.listingAgentEmailAddress` | String/null | Email address of the listing agent |
| `data[].listing.listingContractDate` | String/null | Date of the listing contract |
| `data[].listing.listPriceLow` | Number/null | List price of the property |
| `data[].listing.mlsNumber` | String/null | MLS number |
| `data[].listing.mlsBoardCode` | String/null | MLS board code |
| `data[].listing.pricePerSqFt` | Number/null | Price per square foot |
| `data[].listing.priceChangeTimestamp` | String/null | Timestamp of the last price change |
| `data[].listing.publicRemarks` | String/null | Public remarks about the property |
| `data[].listing.sellingOfficeName` | String/null | Name of the selling office |
| `data[].listing.soldDate` | String/null | Date the property was sold |
| `data[].listing.standardStatus` | String/null | Standard status of the listing |
| `data[].listing.url` | String/null | URL to the listing |
| `data[].listing.address` | Object/null | Property address |
| `data[].listing.address.city` | String/null | City |
| `data[].listing.address.countyOrParish` | String/null | County or parish |
| `data[].listing.address.stateOrProvince` | String/null | State or province |
| `data[].listing.address.unparsedAddress` | String/null | Unparsed address |
| `data[].listing.address.zipCode` | String/null | ZIP code |
| `data[].listing.leadTypes` | Object/null | Lead types information |
| `data[].listing.leadTypes.mlsActive` | Boolean/null | Indicates if the listing is active |
| `data[].listing.leadTypes.mlsCancelled` | Boolean/null | Indicates if the listing is cancelled |
| `data[].listing.leadTypes.mlsDaysOnMarket` | Number/null | Number of days on market |
| `data[].listing.leadTypes.mlsFailed` | Boolean/null | Indicates if the listing failed |
| `data[].listing.leadTypes.mlsHasPhotos` | Boolean/null | Indicates if the listing has photos |
| `data[].listing.leadTypes.mlsLastStatusDate` | String/null | Date of the last status change |
| `data[].listing.leadTypes.mlsListingDate` | String/null | Date the property was listed |
| `data[].listing.leadTypes.mlsListingPrice` | Number/null | Listing price |
| `data[].listing.leadTypes.mlsPending` | Boolean/null | Indicates if the listing is pending |
| `data[].listing.leadTypes.mlsSold` | Boolean/null | Indicates if the property is sold |
| `data[].listing.leadTypes.mlsStatus` | String/null | MLS status |
| `data[].listing.leadTypes.mlsType` | String/null | MLS type |
| `data[].listing.property` | Object/null | Property details |
| `data[].listing.property.associationFee` | Number/null | Association fee |
| `data[].listing.property.bathroomsText` | String/null | Bathrooms text description |
| `data[].listing.property.bathroomsTotal` | Number/null | Total number of bathrooms |
| `data[].listing.property.bedroomsTotal` | Number/null | Total number of bedrooms |
| `data[].listing.property.garageSpaces` | String/Number/null | Number of garage spaces |
| `data[].listing.property.hasBasement` | Boolean/null | Indicates if the property has a basement |
| `data[].listing.property.hasPool` | Boolean/null | Indicates if the property has a pool |
| `data[].listing.property.isCityView` | Boolean/null | Indicates if the property has a city view |
| `data[].listing.property.isMountainView` | Boolean/null | Indicates if the property has a mountain view |
| `data[].listing.property.isParkView` | Boolean/null | Indicates if the property has a park view |
| `data[].listing.property.isWaterFront` | Boolean/null | Indicates if the property is waterfront |
| `data[].listing.property.isWaterView` | Boolean/null | Indicates if the property has a water view |
| `data[].listing.property.latitude` | Number/null | Latitude coordinate |
| `data[].listing.property.livingArea` | Number/null | Living area square footage |
| `data[].listing.property.location` | Array/null | Location coordinates [longitude, latitude] |
| `data[].listing.property.longitude` | Number/null | Longitude coordinate |
| `data[].listing.property.lotSizeSquareFeet` | Number/null | Lot size in square feet |
| `data[].listing.property.neighborhood` | String/null | Neighborhood |
| `data[].listing.property.propertySubType` | String/null | Property sub-type |
| `data[].listing.property.propertyType` | String/null | Property type |
| `data[].listing.property.stories` | String/Number/null | Number of stories |
| `data[].listing.property.subdivisionName` | String/null | Subdivision name |
| `data[].listing.property.yearBuilt` | Number/null | Year the property was built |
| `data[].listing.schools` | Object/null | School information |
| `data[].listing.schools.elementarySchool` | String/null | Elementary school |
| `data[].listing.schools.highSchool` | String/null | High school |
| `data[].listing.schools.middleOrJuniorSchool` | String/null | Middle or junior school |
| `data[].listing.media` | Object/null | Media information |
| `data[].listing.media.primaryListingImageUrl` | String/null | URL to the primary listing image |
| `data[].listing.media.photosCount` | Number/null | Number of photos |
| `data[].listing.media.photosList` | Array/null | List of photos |
| `data[].listingAgent` | Object/null | Listing agent information |
| `data[].listingAgent.email` | String/null | Email of the listing agent |
| `data[].listingAgent.firstName` | String/null | First name of the listing agent |
| `data[].listingAgent.fullName` | String/null | Full name of the listing agent |
| `data[].listingAgent.lastName` | String/null | Last name of the listing agent |
| `data[].listingAgent.mlsAgentId` | String/null | MLS agent ID |
| `data[].listingAgent.mlsCode` | String/null | MLS code |
| `data[].listingAgent.phone` | String/null | Phone number of the listing agent |
| `data[].listingOffice` | Object/null | Listing office information |
| `data[].listingOffice.address` | String/null | Address of the listing office |
| `data[].listingOffice.city` | String/null | City of the listing office |
| `data[].listingOffice.email` | String/null | Email of the listing office |
| `data[].listingOffice.mlsCode` | String/null | MLS code |
| `data[].listingOffice.mlsOfficeId` | String/null | MLS office ID |
| `data[].listingOffice.name` | String/null | Name of the listing office |
| `data[].listingOffice.phone` | String/null | Phone number of the listing office |
| `data[].listingOffice.postalCode` | String/null | Postal code of the listing office |
| `data[].listingOffice.stateOrProvince` | String/null | State or province of the listing office |
| `data[].listingOffice.websiteUrl` | String/null | Website URL of the listing office |
| `data[].sellingAgent` | Object/null | Selling agent information |
| `data[].sellingAgent.email` | String/null | Email of the selling agent |
| `data[].sellingAgent.firstName` | String/null | First name of the selling agent |
| `data[].sellingAgent.fullName` | String/null | Full name of the selling agent |
| `data[].sellingAgent.lastName` | String/null | Last name of the selling agent |
| `data[].sellingAgent.mlsAgentId` | String/null | MLS agent ID |
| `data[].sellingAgent.mlsCode` | String/null | MLS code |
| `data[].sellingAgent.phone` | String/null | Phone number of the selling agent |
| `data[].sellingOffice` | Object/null | Selling office information |
| `data[].sellingOffice.address` | String/null | Address of the selling office |
| `data[].sellingOffice.city` | String/null | City of the selling office |
| `data[].sellingOffice.email` | String/null | Email of the selling office |
| `data[].sellingOffice.mlsCode` | String/null | MLS code |
| `data[].sellingOffice.mlsOfficeId` | String/null | MLS office ID |
| `data[].sellingOffice.name` | String/null | Name of the selling office |
| `data[].sellingOffice.phone` | String/null | Phone number of the selling office |
| `data[].sellingOffice.postalCode` | String/null | Postal code of the selling office |
| `data[].sellingOffice.stateOrProvince` | String/null | State or province of the selling office |
| `data[].sellingOffice.websiteUrl` | String/null | Website URL of the selling office |
| `data[].public` | Object/null | Public record information |
| `data[].public.absenteeType` | String/null | Absentee type |
| `data[].public.age` | Number/null | Age of the property |
| `data[].public.apn` | String/null | Assessor Parcel Number |
| `data[].public.assessedImprovementValue` | Number/null | Assessed improvement value |
| `data[].public.assessedLandValue` | Number/null | Assessed land value |
| `data[].public.assessedValue` | Number/null | Assessed value |
| `data[].public.auctionDate` | String/null | Auction date |
| `data[].public.bathrooms` | Number/null | Number of bathrooms |
| `data[].public.bedrooms` | Number/null | Number of bedrooms |
| `data[].public.companyName` | String/null | Company name |
| `data[].public.deckArea` | Number/null | Deck area |
| `data[].public.documentType` | String/null | Document type |
| `data[].public.documentTypeCode` | String/null | Document type code |
| `data[].public.equity` | Number/null | Equity |
| `data[].public.equityPercent` | Number/null | Equity percentage |
| `data[].public.estimatedEquity` | Number/null | Estimated equity |
| `data[].public.estimatedValue` | Number/null | Estimated value |
| `data[].public.floodZoneDescription` | String/null | Flood zone description |
| `data[].public.floodZoneType` | String/null | Flood zone type |
| `data[].public.imageUrl` | String/null | Image URL |
| `data[].public.landUse` | String/null | Land use |
| `data[].public.lastMortgage1Amount` | Number/null | Last mortgage amount |
| `data[].public.lastSaleAmount` | Number/null | Last sale amount |
| `data[].public.lastSaleDate` | String/null | Last sale date |
| `data[].public.lastUpdateDate` | String/null | Last update date |
| `data[].public.latitude` | Number/null | Latitude coordinate |
| `data[].public.lenderName` | String/null | Lender name |
| `data[].public.lienDocumentType` | String/null | Lien document type |
| `data[].public.listingAmount` | Number/null | Listing amount |
| `data[].public.loanTypeCode` | String/null | Loan type code |
| `data[].public.location` | Array/null | Location coordinates |
| `data[].public.longitude` | Number/null | Longitude coordinate |
| `data[].public.lotSquareFeet` | Number/null | Lot size in square feet |
| `data[].public.maturityDateFirst` | String/null | Maturity date of first mortgage |
| `data[].public.medianIncome` | Number/null | Median income |
| `data[].public.neighborhood` | String/null | Neighborhood |
| `data[].public.noticeType` | String/null | Notice type |
| `data[].public.openMortgageBalance` | Number/null | Open mortgage balance |
| `data[].public.owner1FirstName` | String/null | First name of owner 1 |
| `data[].public.owner1LastName` | String/null | Last name of owner 1 |
| `data[].public.owner2Company` | String/null | Company of owner 2 |
| `data[].public.owner2FirstName` | String/null | First name of owner 2 |
| `data[].public.owner2LastName` | String/null | Last name of owner 2 |
| `data[].public.parcelAccountNumber` | String/null | Parcel account number |
| `data[].public.patioArea` | Number/null | Patio area |
| `data[].public.poolArea` | Number/null | Pool area |
| `data[].public.portfolioPurchasedLast12Months` | Number/null | Portfolio purchased in last 12 months |
| `data[].public.portfolioPurchasedLast6Months` | Number/null | Portfolio purchased in last 6 months |
| `data[].public.pricePerSquareFoot` | Number/null | Price per square foot |
| `data[].public.priorOwnerMonthsOwned` | Number/null | Months owned by prior owner |
| `data[].public.priorSaleAmount` | Number/null | Prior sale amount |
| `data[].public.propertyId` | String/null | Property ID |
| `data[].public.propertyType` | String/null | Property type |
| `data[].public.propertyUse` | String/null | Property use |
| `data[].public.propertyUseCode` | String/Number/null | Property use code |
| `data[].public.recordingDate` | String/null | Recording date |
| `data[].public.rentAmount` | Number/null | Rent amount |
| `data[].public.roomsCount` | Number/null | Number of rooms |
| `data[].public.squareFeet` | Number/null | Square footage |
| `data[].public.stories` | Number/null | Number of stories |
| `data[].public.suggestedRent` | Number/null | Suggested rent |
| `data[].public.taxDelinquentYear` | Number/null | Tax delinquent year |
| `data[].public.taxType` | String/null | Tax type |
| `data[].public.totalPortfolioEquity` | Number/null | Total portfolio equity |
| `data[].public.totalPortfolioMortgageBalance` | Number/null | Total portfolio mortgage balance |
| `data[].public.totalPortfolioValue` | Number/null | Total portfolio value |
| `data[].public.totalPropertiesOwned` | Number/null | Total properties owned |
| `data[].public.unitsCount` | Number/null | Number of units |
| `data[].public.yearBuilt` | Number/null | Year built |
| `data[].public.yearsOwned` | Number/null | Years owned |
| `data[].public.leadTypes` | Object/null | Lead types information |
| `data[].public.leadTypes.absenteeOwner` | Boolean/null | Indicates if the owner is absentee |
| `data[].public.leadTypes.adjustableRate` | Boolean/null | Indicates if the mortgage has an adjustable rate |
| `data[].public.leadTypes.airConditioningAvailable` | Boolean/null | Indicates if air conditioning is available |
| `data[].public.leadTypes.assumable` | Boolean/null | Indicates if the mortgage is assumable |
| `data[].public.leadTypes.auction` | Boolean/null | Indicates if the property is in auction |
| `data[].public.leadTypes.basement` | Boolean/null | Indicates if the property has a basement |
| `data[].public.leadTypes.cashBuyer` | Boolean/null | Indicates if the buyer paid cash |
| `data[].public.leadTypes.corporateOwned` | Boolean/null | Indicates if the property is corporate owned |
| `data[].public.leadTypes.death` | Boolean/null | Indicates if there was a death associated with the property |
| `data[].public.leadTypes.deck` | Boolean/null | Indicates if the property has a deck |
| `data[].public.leadTypes.floodZone` | Boolean/null | Indicates if the property is in a flood zone |
| `data[].public.leadTypes.foreclosure` | Boolean/null | Indicates if the property is in foreclosure |
| `data[].public.leadTypes.forSale` | Boolean/null | Indicates if the property is for sale |
| `data[].public.leadTypes.freeClear` | Boolean/null | Indicates if the property is free and clear |
| `data[].public.leadTypes.garage` | Boolean/null | Indicates if the property has a garage |
| `data[].public.leadTypes.highEquity` | Boolean/null | Indicates if the property has high equity |
| `data[].public.leadTypes.inherited` | Boolean/null | Indicates if the property was inherited |
| `data[].public.leadTypes.inStateAbsenteeOwner` | Boolean/null | Indicates if the absentee owner is in-state |
| `data[].public.leadTypes.investorBuyer` | Boolean/null | Indicates if the buyer is an investor |
| `data[].public.leadTypes.judgment` | Boolean/null | Indicates if there is a judgment on the property |
| `data[].public.leadTypes.MFH2to4` | Boolean/null | Indicates if the property is a multi-family home with 2-4 units |
| `data[].public.leadTypes.MFH5plus` | Boolean/null | Indicates if the property is a multi-family home with 5+ units |
| `data[].public.leadTypes.negativeEquity` | Boolean/null | Indicates if the property has negative equity |
| `data[].public.leadTypes.outOfStateAbsenteeOwner` | Boolean/null | Indicates if the absentee owner is out-of-state |
| `data[].public.leadTypes.ownerOccupied` | Boolean/null | Indicates if the property is owner-occupied |
| `data[].public.leadTypes.patio` | Boolean/null | Indicates if the property has a patio |
| `data[].public.leadTypes.pool` | Boolean/null | Indicates if the property has a pool |
| `data[].public.leadTypes.preForeclosure` | Boolean/null | Indicates if the property is in pre-foreclosure |
| `data[].public.leadTypes.priorOwnerIndividual` | Boolean/null | Indicates if the prior owner was an individual |
| `data[].public.leadTypes.privateLender` | Boolean/null | Indicates if the lender is private |
| `data[].public.leadTypes.reo` | Boolean/null | Indicates if the property is REO (Real Estate Owned) |
| `data[].public.leadTypes.vacant` | Boolean/null | Indicates if the property is vacant |
| `data[].public.address` | Object/null | Property address |
| `data[].public.address.address` | String/null | Full address |
| `data[].public.address.street` | String/null | Street |
| `data[].public.address.city` | String/null | City |
| `data[].public.address.county` | String/null | County |
| `data[].public.address.state` | String/null | State |
| `data[].public.address.zip` | String/null | ZIP code |
| `data[].public.address.label` | String/null | Address label |
| `data[].public.mailAddress` | Object/null | Mailing address |
| `data[].public.mailAddress.address` | String/null | Full mail address |
| `data[].public.mailAddress.street` | String/null | Street |
| `data[].public.mailAddress.city` | String/null | City |
| `data[].public.mailAddress.county` | String/null | County |
| `data[].public.mailAddress.state` | String/null | State |
| `data[].public.mailAddress.zip` | String/null | ZIP code |
| `data[].public.mailAddress.label` | String/null | Address label |
| `recordCount` | Number | The number of records returned |
| `resultCount` | Number | The total number of results available |
| `resultIndex` | Number | The index of the last result returned |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `errorMessage` | String | Error message if applicable |
| `warning` | String | Warning message if applicable |
| `requestExecutionTimeMS` | String | The time taken to execute the request |

---

## PropGPTAPI

**API Endpoint:** `POST /v2/PropGPT`

**Description:** PropGPT Beta semantic search

**Business Purpose:** This API leverages AI to perform semantic property searches using natural language queries, providing intelligent property matching with GPT-powered analysis.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `live` | Boolean | Indicates if the request was made with a live API key |
| `input` | Object | The input parameters used for the search |
| `summary` | Object | Summary information if requested |
| `aggregations` | Object | Aggregation data from the search |
| `data` | Array | Array of property search results |
| `data[].id` | String/Number | Property ID |
| `data[].propertyInfo` | Object | Property information |
| `data[].ownerInfo` | Object | Owner information |
| `data[].lotInfo` | Object | Lot information |
| `data[].taxInfo` | Object | Tax information |
| `resultCount` | Number | Total number of results matching the search criteria |
| `resultIndex` | Number | Starting index of the returned results |
| `recordCount` | Number | Number of records in the data array |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `requestExecutionTimeMS` | String | The time taken to execute the entire request |
| `propGPTExecutionTimeMS` | String/null | The time taken for the PropGPT execution |
| `searchExecutionTimeMS` | String/null | The time taken for the search execution |
| `query` | Object | The query generated by PropGPT |

---

## PropertyAvmAPI

**API Endpoint:** `POST /v2/PropertyAvm`

**Description:** Get AVM for a set of addresses

**Business Purpose:** This API provides Automated Valuation Model (AVM) estimates for properties, helping users determine current market values with confidence scores.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `input` | Object | The input parameters used for the request |
| `input.strict` | Boolean | Strict matching mode |
| `input.key` | String/null | User-provided key |
| `input.id` | Number | Property ID |
| `input.address` | String/null | Property address |
| `data` | Object | The AVM data for the property |
| `data.id` | Number/null | Property ID |
| `data.apn` | String/null | Assessor Parcel Number |
| `data.fips` | String/null | FIPS code |
| `data.avm` | Number/null | Automated Valuation Model estimate |
| `data.avmMin` | Number/null | AVM minimum estimate |
| `data.avmMax` | Number/null | AVM maximum estimate |
| `data.confidence` | Number/null | Confidence score of the AVM estimate |
| `data.address` | String/null | Property address |
| `data.unit` | String/null | Unit number |
| `data.unitType` | String/null | Unit type |
| `data.city` | String/null | City |
| `data.state` | String/null | State |
| `data.zip` | String/null | ZIP code |
| `data.zip4` | String/null | ZIP+4 code |
| `data.label` | String/null | Full address label |
| `data.lastUpdateDate` | String/null | Last update date |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `live` | Boolean | Indicates if the request was made with a live API key |
| `requestExecutionTimeMS` | String | The time taken to execute the request |
| `errorMessage` | String | Error message if applicable |

---

## PropertyAvmBulkAPI

**API Endpoint:** `POST /v2/PropertyAvmBulk`

**Description:** Get AVM for a set of addresses

**Business Purpose:** This API provides bulk AVM estimates for multiple properties in a single request, enabling efficient valuation of property portfolios.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `data` | Array | Array of property AVM results |
| `data[].input` | Object | The input parameters used for the request |
| `data[].input.strict` | Boolean | Strict matching mode |
| `data[].input.id` | Number | Property ID |
| `data[].input.address` | String/null | Property address |
| `data[].input.key` | String/null | User-provided key |
| `data[].id` | Number/null | Property ID |
| `data[].apn` | String/null | Assessor Parcel Number |
| `data[].fips` | String/null | FIPS code |
| `data[].avm` | Number/null | Automated Valuation Model estimate |
| `data[].avmMin` | Number/null | AVM minimum estimate |
| `data[].avmMax` | Number/null | AVM maximum estimate |
| `data[].confidence` | Number/null | Confidence score of the AVM estimate |
| `data[].address` | String/null | Property address |
| `data[].unit` | String/null | Unit number |
| `data[].unitType` | String/null | Unit type |
| `data[].city` | String/null | City |
| `data[].state` | String/null | State |
| `data[].zip` | String/null | ZIP code |
| `data[].zip4` | String/null | ZIP+4 code |
| `data[].label` | String/null | Full address label |
| `data[].lastUpdateDate` | String/null | Last update date |
| `data[].error` | Boolean | Indicates if an error occurred (error responses only) |
| `data[].errorMessage` | String | Error message (error responses only) |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `live` | Boolean | Indicates if the request was made with a live API key |
| `requestExecutionTimeMS` | String | The time taken to execute the request |
| `errorMessage` | String | Error message if applicable |

---

## PropertyCsvBuilderAPI

**API Endpoint:** `POST /v2/CSVBuilder`

**Description:** Get a list of property search results

**Business Purpose:** This API generates CSV files from property search results, enabling bulk data export for analysis, reporting, and integration with external systems.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `live` | Boolean | Indicates if the request was made with a live API key |
| `input` | Object | The input parameters used for the request |
| `data` | Object | The data returned from the CSV builder |
| `data.processing` | Boolean | Indicates if the request is being processed asynchronously |
| `data.requestId` | String | Unique identifier for the request |
| `data.count` | Number | The count of records matching the search criteria (count mode) |
| `data.url` | String | URL to download the generated CSV file (processing mode) |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `requestExecutionTimeMS` | String | The time taken to execute the request |

---

## PropertyDetailAPI

**API Endpoint:** `POST /v2/PropertyDetail`

**Description:** Get a list of property detail results

**Business Purpose:** This API provides comprehensive property details including ownership information, property characteristics, financial data, and historical records for detailed property analysis.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `input` | Object | The input parameters used for the request |
| `data` | Object | The comprehensive property data |
| `data.id` | Number/null | Property ID |
| `data.MFH2to4` | Boolean/null | Multi-family home with 2-4 units |
| `data.MFH5plus` | Boolean/null | Multi-family home with 5+ units |
| `data.absenteeOwner` | Boolean/null | Indicates if the owner is absentee |
| `data.adjustableRate` | Boolean/null | Indicates if the mortgage has an adjustable rate |
| `data.assumable` | Boolean/null | Indicates if the mortgage is assumable |
| `data.auction` | Boolean/null | Indicates if the property is in auction |
| `data.equity` | Number/null | Property equity |
| `data.bankOwned` | Boolean/null | Indicates if the property is bank owned |
| `data.cashBuyer` | Boolean/null | Indicates if the buyer paid cash |
| `data.cashSale` | Boolean/null | Indicates if it was a cash sale |
| `data.corporateOwned` | Boolean/null | Indicates if the property is corporate owned |
| `data.death` | Boolean/null | Indicates if there was a death associated with the property |
| `data.deathTransfer` | Boolean/null | Indicates if the transfer was due to death |
| `data.deedInLieu` | Boolean/null | Indicates if there was a deed in lieu |
| `data.equityPercent` | Number/null | Equity percentage |
| `data.estimatedEquity` | Number/null | Estimated equity |
| `data.estimatedMortgageBalance` | Any/null | Estimated mortgage balance |
| `data.estimatedMortgagePayment` | Any/null | Estimated mortgage payment |
| `data.estimatedValue` | Number/null | Estimated value |
| `data.floodZone` | Boolean/null | Indicates if the property is in a flood zone |
| `data.floodZoneDescription` | String/null | Flood zone description |
| `data.floodZoneType` | String/null | Flood zone type |
| `data.freeClear` | Boolean/null | Indicates if the property is free and clear |
| `data.highEquity` | Boolean/null | Indicates if the property has high equity |
| `data.inStateAbsenteeOwner` | Boolean/null | Indicates if the absentee owner is in-state |
| `data.inherited` | Boolean/null | Indicates if the property was inherited |
| `data.investorBuyer` | Boolean/null | Indicates if the buyer is an investor |
| `data.judgment` | Boolean/null | Indicates if there is a judgment on the property |
| `data.lastSaleDate` | String/null | Last sale date |
| `data.lastSalePrice` | Any/null | Last sale price |
| `data.lastUpdateDate` | String/null | Last update date |
| `data.lien` | Boolean/null | Indicates if there is a lien on the property |
| `data.loanTypeCodeFirst` | String/null | First loan type code |
| `data.loanTypeCodeSecond` | String/null | Second loan type code |
| `data.loanTypeCodeThird` | String/null | Third loan type code |
| `data.maturityDateFirst` | String/null | Maturity date of first mortgage |
| `data.mlsActive` | Boolean | Indicates if the listing is active |
| `data.mlsCancelled` | Boolean | Indicates if the listing is cancelled |
| `data.mlsDaysOnMarket` | Number/null | Number of days on market |
| `data.mlsFailed` | Boolean | Indicates if the listing failed |
| `data.mlsFailedDate` | String/null | Date the listing failed |
| `data.mlsHasPhotos` | Boolean | Indicates if the listing has photos |
| `data.mlsLastSaleDate` | String/null | Last MLS sale date |
| `data.mlsLastStatusDate` | String/null | Last MLS status date |
| `data.mlsListingDate` | String/null | MLS listing date |
| `data.mlsListingPrice` | Number/null | MLS listing price |
| `data.mlsListingPricePerSquareFoot` | Number/null | MLS listing price per square foot |
| `data.mlsPending` | Boolean | Indicates if the listing is pending |
| `data.mlsSold` | Boolean | Indicates if the property is sold |
| `data.mlsSoldPrice` | Any/null | MLS sold price |
| `data.mlsStatus` | String/null | MLS status |
| `data.mlsTotalUpdates` | Number/null | Total MLS updates |
| `data.mlsType` | String/null | MLS type |
| `data.mobileHome` | Boolean/null | Indicates if it's a mobile home |
| `data.noticeType` | String/null | Notice type |
| `data.openMortgageBalance` | Number/null | Open mortgage balance |
| `data.outOfStateAbsenteeOwner` | Boolean/null | Indicates if the absentee owner is out-of-state |
| `data.ownerOccupied` | Boolean/null | Indicates if the property is owner-occupied |
| `data.preForeclosure` | Boolean/null | Indicates if the property is in pre-foreclosure |
| `data.privateLender` | Boolean/null | Indicates if the lender is private |
| `data.propertyType` | String/null | Property type |
| `data.quitClaim` | Boolean/null | Indicates if there was a quit claim deed |
| `data.reapi_loaded_at` | String/null | REAPI loaded timestamp |
| `data.sheriffsDeed` | Boolean/null | Indicates if there was a sheriff's deed |
| `data.spousalDeath` | Boolean/null | Indicates if there was a spousal death |
| `data.taxLien` | Boolean/null | Indicates if there is a tax lien |
| `data.trusteeSale` | Boolean/null | Indicates if it was a trustee sale |
| `data.vacant` | Boolean/null | Indicates if the property is vacant |
| `data.warrantyDeed` | Boolean/null | Indicates if there was a warranty deed |
| `data.auctionInfo` | Object/null | Auction information |
| `data.auctionInfo.active` | Boolean/null | Indicates if auction is active |
| `data.auctionInfo.auctionDate` | String/null | Date of auction |
| `data.auctionInfo.auctionStreetAddress` | String/null | Street address of auction |
| `data.auctionInfo.auctionTime` | String/null | Time of auction |
| `data.auctionInfo.caseNumber` | String/null | Case number |
| `data.auctionInfo.defaultAmount` | Any/null | Default amount |
| `data.auctionInfo.documentType` | String/null | Document type |
| `data.auctionInfo.estimatedBankValue` | Any/null | Estimated bank value |
| `data.auctionInfo.foreclosureId` | Any/null | Foreclosure ID |
| `data.auctionInfo.judgmentAmount` | Any/null | Judgment amount |
| `data.auctionInfo.judgmentDate` | String/null | Judgment date |
| `data.auctionInfo.lenderName` | String/null | Lender name |
| `data.auctionInfo.lenderPhone` | String/null | Lender phone |
| `data.auctionInfo.noticeType` | String/null | Notice type |
| `data.auctionInfo.openingBid` | Any/null | Opening bid amount |
| `data.auctionInfo.originalLoanAmount` | Any/null | Original loan amount |
| `data.auctionInfo.recordingDate` | String/null | Recording date |
| `data.auctionInfo.seqNo` | Number/null | Sequence number |
| `data.auctionInfo.trusteeAddress` | String/null | Trustee address |
| `data.auctionInfo.trusteeFullName` | String/null | Trustee full name |
| `data.auctionInfo.trusteePhone` | String/null | Trustee phone |
| `data.auctionInfo.trusteeSaleNumber` | String/null | Trustee sale number |
| `data.auctionInfo.typeName` | String/null | Type name |
| `data.currentMortgages` | Array | Current mortgages |
| `data.currentMortgages[].amount` | Number/null | Mortgage amount |
| `data.currentMortgages[].assumable` | Boolean/null | Indicates if mortgage is assumable |
| `data.currentMortgages[].book` | String/null | Book reference |
| `data.currentMortgages[].page` | String/null | Page reference |
| `data.currentMortgages[].documentNumber` | String/null | Document number |
| `data.currentMortgages[].deedType` | String/null | Deed type |
| `data.currentMortgages[].documentDate` | String/null | Document date |
| `data.currentMortgages[].granteeName` | String/null | Grantee name |
| `data.currentMortgages[].interestRate` | Number/null | Interest rate |
| `data.currentMortgages[].interestRateType` | String/null | Interest rate type |
| `data.currentMortgages[].lenderCode` | String/null | Lender code |
| `data.currentMortgages[].lenderName` | String/null | Lender name |
| `data.currentMortgages[].lenderType` | String/null | Lender type |
| `data.currentMortgages[].loanType` | String/null | Loan type |
| `data.currentMortgages[].loanTypeCode` | String/null | Loan type code |
| `data.currentMortgages[].maturityDate` | String/null | Maturity date |
| `data.currentMortgages[].mortgageId` | String/null | Mortgage ID |
| `data.currentMortgages[].position` | String/null | Position |
| `data.currentMortgages[].recordingDate` | String/null | Recording date |
| `data.currentMortgages[].seqNo` | Number/null | Sequence number |
| `data.currentMortgages[].term` | Any/null | Term |
| `data.currentMortgages[].termType` | String/null | Term type |
| `data.currentMortgages[].transactionType` | String/null | Transaction type |
| `data.demographics` | Object/null | Demographics information |
| `data.demographics.fmrEfficiency` | Any/null | Fair market rent for efficiency units |
| `data.demographics.fmrFourBedroom` | Any/null | Fair market rent for four bedroom units |
| `data.demographics.fmrOneBedroom` | Any/null | Fair market rent for one bedroom units |
| `data.demographics.fmrThreeBedroom` | Any/null | Fair market rent for three bedroom units |
| `data.demographics.fmrTwoBedroom` | Any/null | Fair market rent for two bedroom units |
| `data.demographics.fmrYear` | Any/null | Fair market rent year |
| `data.demographics.hudAreaCode` | String/null | HUD area code |
| `data.demographics.hudAreaName` | String/null | HUD area name |
| `data.demographics.medianIncome` | Any/null | Median income |
| `data.demographics.suggestedRent` | Any/null | Suggested rent |
| `data.foreclosureInfo` | Array | Foreclosure information |
| `data.foreclosureInfo[].active` | Boolean/null | Indicates if foreclosure is active |
| `data.foreclosureInfo[].auctionDate` | String/null | Auction date |
| `data.foreclosureInfo[].auctionStreetAddress` | String/null | Auction street address |
| `data.foreclosureInfo[].auctionTime` | String/null | Auction time |
| `data.foreclosureInfo[].caseNumber` | String/null | Case number |
| `data.foreclosureInfo[].defaultAmount` | Number/null | Default amount |
| `data.foreclosureInfo[].documentType` | String/null | Document type |
| `data.foreclosureInfo[].estimatedBankValue` | Number/null | Estimated bank value |
| `data.foreclosureInfo[].foreclosureId` | Number/null | Foreclosure ID |
| `data.foreclosureInfo[].judgmentAmount` | Any/null | Judgment amount |
| `data.foreclosureInfo[].judgmentDate` | String/null | Judgment date |
| `data.foreclosureInfo[].lenderName` | String/null | Lender name |
| `data.foreclosureInfo[].lenderPhone` | String/null | Lender phone |
| `data.foreclosureInfo[].noticeType` | String/null | Notice type |
| `data.foreclosureInfo[].openingBid` | Number/null | Opening bid |
| `data.foreclosureInfo[].originalLoanAmount` | Number/null | Original loan amount |
| `data.foreclosureInfo[].recordingDate` | String/null | Recording date |
| `data.foreclosureInfo[].seqNo` | Number/null | Sequence number |
| `data.foreclosureInfo[].trusteeAddress` | String/null | Trustee address |
| `data.foreclosureInfo[].trusteeFullName` | String/null | Trustee full name |
| `data.foreclosureInfo[].trusteePhone` | String/null | Trustee phone |
| `data.foreclosureInfo[].trusteeSaleNumber` | String/null | Trustee sale number |
| `data.foreclosureInfo[].typeName` | String/null | Type name |
| `data.lastSale` | Object/null | Last sale information |
| `data.lastSale.book` | String/null | Book reference |
| `data.lastSale.page` | String/null | Page reference |
| `data.lastSale.documentNumber` | String/null | Document number |
| `data.lastSale.armsLength` | Boolean/null | Arms length transaction |
| `data.lastSale.buyerNames` | String/null | Buyer names |
| `data.lastSale.documentType` | String/null | Document type |
| `data.lastSale.documentTypeCode` | String/null | Document type code |
| `data.lastSale.downPayment` | Number/null | Down payment |
| `data.lastSale.ltv` | Number/null | Loan to value ratio |
| `data.lastSale.ownerIndividual` | Boolean/null | Owner is individual |
| `data.lastSale.priorOwnerIndividual` | Boolean/null | Prior owner is individual |
| `data.lastSale.priorOwnerMonthsOwned` | Number/null | Prior owner months owned |
| `data.lastSale.purchaseMethod` | String/null | Purchase method |
| `data.lastSale.recordingDate` | String/null | Recording date |
| `data.lastSale.saleAmount` | Number/null | Sale amount |
| `data.lastSale.saleDate` | String/null | Sale date |
| `data.lastSale.sellerNames` | String/null | Seller names |
| `data.lastSale.seqNo` | Number/null | Sequence number |
| `data.lastSale.transactionType` | String/null | Transaction type |
| `data.linkedProperties` | Object/null | Linked properties information |
| `data.linkedProperties.ids` | Any/null | Property IDs |
| `data.linkedProperties.purchasedLast12mos` | Number/null | Purchased last 12 months |
| `data.linkedProperties.purchasedLast6mos` | Number/null | Purchased last 6 months |
| `data.linkedProperties.totalEquity` | Any/null | Total equity |
| `data.linkedProperties.totalMortgageBalance` | Any/null | Total mortgage balance |
| `data.linkedProperties.totalOwned` | Any/null | Total owned |
| `data.linkedProperties.totalValue` | Any/null | Total value |
| `data.lotInfo` | Object | Lot information |
| `data.lotInfo.apn` | String/null | Assessor Parcel Number |
| `data.lotInfo.apnUnformatted` | String/null | Unformatted APN |
| `data.lotInfo.censusBlock` | String/null | Census block |
| `data.lotInfo.censusBlockGroup` | String/null | Census block group |
| `data.lotInfo.censusTract` | String/null | Census tract |
| `data.lotInfo.landUse` | String/null | Land use |
| `data.lotInfo.legalDescription` | String/null | Legal description |
| `data.lotInfo.legalSection` | String/null | Legal section |
| `data.lotInfo.lotAcres` | Number/null | Lot acres |
| `data.lotInfo.lotNumber` | String/null | Lot number |
| `data.lotInfo.lotSquareFeet` | Number/null | Lot square feet |
| `data.lotInfo.lotDepthFeet` | Number/null | Lot depth feet |
| `data.lotInfo.lotWidthFeet` | Number/null | Lot width feet |
| `data.lotInfo.propertyClass` | String/null | Property class |
| `data.lotInfo.propertyUse` | String/null | Property use |
| `data.lotInfo.subdivision` | String/null | Subdivision |
| `data.lotInfo.zoning` | String/null | Zoning |
| `data.mlsHistory` | Array | MLS history |
| `data.mlsHistory[].agentEmail` | String/null | Agent email |
| `data.mlsHistory[].agentName` | String/null | Agent name |
| `data.mlsHistory[].agentOffice` | String/null | Agent office |
| `data.mlsHistory[].agentPhone` | String/null | Agent phone |
| `data.mlsHistory[].baths` | Number/null | Bathrooms |
| `data.mlsHistory[].beds` | Number/null | Bedrooms |
| `data.mlsHistory[].daysOnMarket` | Any/null | Days on market |
| `data.mlsHistory[].lastStatusDate` | String/null | Last status date |
| `data.mlsHistory[].price` | Number/null | Price |
| `data.mlsHistory[].propertyId` | Number/null | Property ID |
| `data.mlsHistory[].seqNo` | Number/null | Sequence number |
| `data.mlsHistory[].status` | String/null | Status |
| `data.mlsHistory[].statusDate` | String/null | Status date |
| `data.mlsHistory[].type` | String/null | Type |
| `data.mlsKeywords` | Object/null | MLS keywords |
| `data.mlsKeywords.creativeFinancing` | Boolean/null | Creative financing |
| `data.mlsKeywords.investorOwned` | Boolean/null | Investor owned |
| `data.mlsKeywords.motivatedSellerHigh` | Boolean/null | Motivated seller high |
| `data.mlsKeywords.motivatedSellerLow` | Boolean/null | Motivated seller low |
| `data.mlsKeywords.motivatedSellerMed` | Boolean/null | Motivated seller medium |
| `data.mortgageHistory` | Array | Mortgage history |
| `data.mortgageHistory[].amount` | Number/null | Mortgage amount |
| `data.mortgageHistory[].assumable` | Boolean/null | Assumable |
| `data.mortgageHistory[].book` | String/null | Book reference |
| `data.mortgageHistory[].page` | String/null | Page reference |
| `data.mortgageHistory[].documentNumber` | String/null | Document number |
| `data.mortgageHistory[].deedType` | String/null | Deed type |
| `data.mortgageHistory[].documentDate` | String/null | Document date |
| `data.mortgageHistory[].granteeName` | String/null | Grantee name |
| `data.mortgageHistory[].interestRate` | Number/null | Interest rate |
| `data.mortgageHistory[].interestRateType` | String/null | Interest rate type |
| `data.mortgageHistory[].lenderCode` | String/null | Lender code |
| `data.mortgageHistory[].lenderName` | String/null | Lender name |
| `data.mortgageHistory[].lenderType` | String/null | Lender type |
| `data.mortgageHistory[].loanType` | String/null | Loan type |
| `data.mortgageHistory[].loanTypeCode` | String/null | Loan type code |
| `data.mortgageHistory[].maturityDate` | String/null | Maturity date |
| `data.mortgageHistory[].mortgageId` | String/null | Mortgage ID |
| `data.mortgageHistory[].open` | Boolean/null | Open |
| `data.mortgageHistory[].position` | String/null | Position |
| `data.mortgageHistory[].recordingDate` | String/null | Recording date |
| `data.mortgageHistory[].seqNo` | Number/null | Sequence number |
| `data.mortgageHistory[].term` | Any/null | Term |
| `data.mortgageHistory[].termType` | String/null | Term type |
| `data.mortgageHistory[].transactionType` | String/null | Transaction type |
| `data.neighborhood` | Object/null | Neighborhood information |
| `data.neighborhood.center` | Any/null | Center coordinates |
| `data.neighborhood.id` | Any/null | Neighborhood ID |
| `data.neighborhood.name` | String/null | Neighborhood name |
| `data.neighborhood.type` | String/null | Neighborhood type |
| `data.ownerInfo` | Object | Owner information |
| `data.ownerInfo.absenteeOwner` | Boolean/null | Absentee owner |
| `data.ownerInfo.companyName` | String/null | Company name |
| `data.ownerInfo.corporateOwned` | Boolean/null | Corporate owned |
| `data.ownerInfo.equity` | Number/null | Equity |
| `data.ownerInfo.inStateAbsenteeOwner` | Boolean/null | In-state absentee owner |
| `data.ownerInfo.mailAddress` | Object/null | Mail address |
| `data.ownerInfo.mailAddress.address` | String/null | Address |
| `data.ownerInfo.mailAddress.addressFormat` | String/null | Address format |
| `data.ownerInfo.mailAddress.carrierRoute` | String/null | Carrier route |
| `data.ownerInfo.mailAddress.city` | String/null | City |
| `data.ownerInfo.mailAddress.county` | String/null | County |
| `data.ownerInfo.mailAddress.fips` | String/null | FIPS code |
| `data.ownerInfo.mailAddress.house` | String/null | House number |
| `data.ownerInfo.mailAddress.label` | String/null | Label |
| `data.ownerInfo.mailAddress.preDirection` | String/null | Pre-direction |
| `data.ownerInfo.mailAddress.state` | String/null | State |
| `data.ownerInfo.mailAddress.street` | String/null | Street |
| `data.ownerInfo.mailAddress.streetType` | String/null | Street type |
| `data.ownerInfo.mailAddress.unit` | String/null | Unit |
| `data.ownerInfo.mailAddress.unitType` | String/null | Unit type |
| `data.ownerInfo.mailAddress.zip` | String/null | ZIP code |
| `data.ownerInfo.mailAddress.zip4` | String/null | ZIP+4 code |
| `data.ownerInfo.outOfStateAbsenteeOwner` | Boolean/null | Out-of-state absentee owner |
| `data.ownerInfo.owner1FirstName` | String/null | Owner 1 first name |
| `data.ownerInfo.owner1FullName` | String/null | Owner 1 full name |
| `data.ownerInfo.owner1LastName` | String/null | Owner 1 last name |
| `data.ownerInfo.owner1Type` | String/null | Owner 1 type |
| `data.ownerInfo.owner2FirstName` | String/null | Owner 2 first name |
| `data.ownerInfo.owner2FullName` | String/null | Owner 2 full name |
| `data.ownerInfo.owner2LastName` | String/null | Owner 2 last name |
| `data.ownerInfo.owner2Type` | String/null | Owner 2 type |
| `data.ownerInfo.ownerOccupied` | Boolean/null | Owner occupied |
| `data.ownerInfo.ownershipLength` | Number/null | Ownership length |
| `data.priorOwnerInfo` | Object/null | Prior owner information |
| `data.priorOwnerInfo.companyName` | String/null | Company name |
| `data.priorOwnerInfo.ownershipLength` | Number/null | Ownership length |
| `data.priorOwnerInfo.owner1FirstName` | String/null | Owner 1 first name |
| `data.priorOwnerInfo.owner1LastName` | String/null | Owner 1 last name |
| `data.priorOwnerInfo.owner1FullName` | String/null | Owner 1 full name |
| `data.priorOwnerInfo.owner1VestingType` | String/null | Owner 1 vesting type |
| `data.priorOwnerInfo.owner2FirstName` | String/null | Owner 2 first name |
| `data.priorOwnerInfo.owner2LastName` | String/null | Owner 2 last name |
| `data.priorOwnerInfo.owner2FullName` | String/null | Owner 2 full name |
| `data.priorOwnerInfo.owner2Type` | String/null | Owner 2 type |
| `data.priorOwnerInfo.ownerNames` | String/null | Owner names |
| `data.priorOwnerInfo.mailAddress` | Object/null | Mail address |
| `data.priorOwnerInfo.mailAddress.house` | String/null | House number |
| `data.priorOwnerInfo.mailAddress.street` | String/null | Street |
| `data.priorOwnerInfo.mailAddress.address` | String/null | Address |
| `data.priorOwnerInfo.mailAddress.preDirection` | String/null | Pre-direction |
| `data.priorOwnerInfo.mailAddress.streetType` | String/null | Street type |
| `data.priorOwnerInfo.mailAddress.unit` | String/null | Unit |
| `data.priorOwnerInfo.mailAddress.unitType` | String/null | Unit type |
| `data.priorOwnerInfo.mailAddress.city` | String/null | City |
| `data.priorOwnerInfo.mailAddress.state` | String/null | State |
| `data.priorOwnerInfo.mailAddress.zip` | String/null | ZIP code |
| `data.priorOwnerInfo.mailAddress.zip4` | String/null | ZIP+4 code |
| `data.priorOwnerInfo.mailAddress.label` | String/null | Label |
| `data.priorOwnerInfo.error` | String/null | Error |
| `data.propertyInfo` | Object | Property information |
| `data.propertyInfo.address` | Object/null | Address |
| `data.propertyInfo.address.address` | String/null | Address |
| `data.propertyInfo.address.carrierRoute` | String/null | Carrier route |
| `data.propertyInfo.address.city` | String/null | City |
| `data.propertyInfo.address.congressionalDistrict` | String/null | Congressional district |
| `data.propertyInfo.address.county` | String/null | County |
| `data.propertyInfo.address.fips` | String/null | FIPS code |
| `data.propertyInfo.address.house` | String/null | House number |
| `data.propertyInfo.address.jurisdiction` | String/null | Jurisdiction |
| `data.propertyInfo.address.label` | String/null | Label |
| `data.propertyInfo.address.preDirection` | String/null | Pre-direction |
| `data.propertyInfo.address.state` | String/null | State |
| `data.propertyInfo.address.street` | String/null | Street |
| `data.propertyInfo.address.streetType` | String/null | Street type |
| `data.propertyInfo.address.unit` | String/null | Unit |
| `data.propertyInfo.address.unitType` | String/null | Unit type |
| `data.propertyInfo.address.zip` | String/null | ZIP code |
| `data.propertyInfo.address.zip4` | String/null | ZIP+4 code |
| `data.propertyInfo.airConditioningType` | String/null | Air conditioning type |
| `data.propertyInfo.attic` | Boolean/null | Attic |
| `data.propertyInfo.basementFinishedPercent` | Number/null | Basement finished percent |
| `data.propertyInfo.basementSquareFeet` | Number/null | Basement square feet |
| `data.propertyInfo.basementSquareFeetFinished` | Number/null | Basement square feet finished |
| `data.propertyInfo.basementSquareFeetUnfinished` | Number/null | Basement square feet unfinished |
| `data.propertyInfo.basementType` | String/null | Basement type |
| `data.propertyInfo.bathrooms` | Number/null | Bathrooms |
| `data.propertyInfo.bedrooms` | Number/null | Bedrooms |
| `data.propertyInfo.breezeway` | Boolean/null | Breezeway |
| `data.propertyInfo.buildingSquareFeet` | Number/null | Building square feet |
| `data.propertyInfo.buildingsCount` | Number/null | Buildings count |
| `data.propertyInfo.carport` | Boolean/null | Carport |
| `data.propertyInfo.construction` | String/null | Construction |
| `data.propertyInfo.deck` | Boolean/null | Deck |
| `data.propertyInfo.deckArea` | Number/null | Deck area |
| `data.propertyInfo.featureBalcony` | Boolean/null | Feature balcony |
| `data.propertyInfo.fireplace` | Boolean/null | Fireplace |
| `data.propertyInfo.fireplaces` | Number/null | Fireplaces |
| `data.propertyInfo.garageSquareFeet` | Number/null | Garage square feet |
| `data.propertyInfo.garageType` | String/null | Garage type |
| `data.propertyInfo.heatingFuelType` | String/null | Heating fuel type |
| `data.propertyInfo.heatingType` | String/null | Heating type |
| `data.propertyInfo.hoa` | Boolean/null | HOA |
| `data.propertyInfo.interiorStructure` | String/null | Interior structure |
| `data.propertyInfo.latitude` | Number/null | Latitude |
| `data.propertyInfo.livingSquareFeet` | Number/null | Living square feet |
| `data.propertyInfo.longitude` | Number/null | Longitude |
| `data.propertyInfo.lotSquareFeet` | Number/null | Lot square feet |
| `data.propertyInfo.parcelAccountNumber` | String/null | Parcel account number |
| `data.propertyInfo.parkingSpaces` | Number/null | Parking spaces |
| `data.propertyInfo.partialBathrooms` | Number/null | Partial bathrooms |
| `data.propertyInfo.patio` | Boolean/null | Patio |
| `data.propertyInfo.patioArea` | Any/null | Patio area |
| `data.propertyInfo.plumbingFixturesCount` | Number/null | Plumbing fixtures count |
| `data.propertyInfo.pool` | Boolean/null | Pool |
| `data.propertyInfo.poolArea` | Number/null | Pool area |
| `data.propertyInfo.porchArea` | Number/null | Porch area |
| `data.propertyInfo.porchType` | String/null | Porch type |
| `data.propertyInfo.pricePerSquareFoot` | Number/null | Price per square foot |
| `data.propertyInfo.propertyUse` | String/null | Property use |
| `data.propertyInfo.propertyUseCode` | Number/null | Property use code |
| `data.propertyInfo.roofConstruction` | String/null | Roof construction |
| `data.propertyInfo.roofMaterial` | String/null | Roof material |
| `data.propertyInfo.roomsCount` | Number/null | Rooms count |
| `data.propertyInfo.rvParking` | Boolean/null | RV parking |
| `data.propertyInfo.safetyFireSprinklers` | Boolean/null | Safety fire sprinklers |
| `data.propertyInfo.stories` | Number/null | Stories |
| `data.propertyInfo.taxExemptionHomeownerFlag` | Boolean/null | Tax exemption homeowner flag |
| `data.propertyInfo.unitsCount` | Number/null | Units count |
| `data.propertyInfo.utilitiesSewageUsage` | String/null | Utilities sewage usage |
| `data.propertyInfo.utilitiesWaterSource` | String/null | Utilities water source |
| `data.propertyInfo.yearBuilt` | Number/null | Year built |
| `data.saleHistory` | Array | Sale history |
| `data.saleHistory[].book` | String/null | Book reference |
| `data.saleHistory[].page` | String/null | Page reference |
| `data.saleHistory[].documentNumber` | String/null | Document number |
| `data.saleHistory[].armsLength` | Boolean/null | Arms length |
| `data.saleHistory[].buyerNames` | String/null | Buyer names |
| `data.saleHistory[].documentType` | String/null | Document type |
| `data.saleHistory[].documentTypeCode` | String/null | Document type code |
| `data.saleHistory[].downPayment` | Number/null | Down payment |
| `data.saleHistory[].ltv` | Number/null | Loan to value |
| `data.saleHistory[].ownerIndividual` | Boolean/null | Owner individual |
| `data.saleHistory[].purchaseMethod` | String/null | Purchase method |
| `data.saleHistory[].recordingDate` | String/null | Recording date |
| `data.saleHistory[].saleAmount` | Number/null | Sale amount |
| `data.saleHistory[].saleDate` | String/null | Sale date |
| `data.saleHistory[].sellerNames` | String/null | Seller names |
| `data.saleHistory[].seqNo` | Number/null | Sequence number |
| `data.saleHistory[].transactionType` | String/null | Transaction type |
| `data.schools` | Array | Schools information |
| `data.schools[].city` | String/null | City |
| `data.schools[].enrollment` | Number/null | Enrollment |
| `data.schools[].grades` | String/null | Grades |
| `data.schools[].levels` | Object/null | Levels |
| `data.schools[].levels.elementary` | Boolean/null | Elementary level |
| `data.schools[].levels.high` | Boolean/null | High school level |
| `data.schools[].levels.middle` | Boolean/null | Middle school level |
| `data.schools[].levels.preschool` | Boolean/null | Preschool level |
| `data.schools[].location` | Any/null | Location |
| `data.schools[].name` | String/null | School name |
| `data.schools[].parentRating` | Number/null | Parent rating |
| `data.schools[].rating` | Number/null | Rating |
| `data.schools[].state` | String/null | State |
| `data.schools[].street` | String/null | Street |
| `data.schools[].type` | String/null | School type |
| `data.schools[].zip` | String/null | ZIP code |
| `data.taxInfo` | Object | Tax information |
| `data.taxInfo.assessedImprovementValue` | Number/null | Assessed improvement value |
| `data.taxInfo.assessedLandValue` | Number/null | Assessed land value |
| `data.taxInfo.assessedValue` | Number/null | Assessed value |
| `data.taxInfo.assessmentYear` | Number/null | Assessment year |
| `data.taxInfo.estimatedValue` | Number/null | Estimated value |
| `data.taxInfo.marketImprovementValue` | Number/null | Market improvement value |
| `data.taxInfo.marketLandValue` | Number/null | Market land value |
| `data.taxInfo.marketValue` | Number/null | Market value |
| `data.taxInfo.propertyId` | Number/null | Property ID |
| `data.taxInfo.taxAmount` | Number/null | Tax amount |
| `data.taxInfo.taxDelinquentYear` | Any/null | Tax delinquent year |
| `data.taxInfo.year` | Number/null | Tax year |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `live` | Boolean | Indicates if the request was made with a live API key |
| `requestExecutionTimeMS` | String | The time taken to execute the request |
| `propertyLookupExecutionTimeMS` | String/null | Property lookup execution time |
| `compsLookupExecutionTimeMS` | String/null | Comps lookup execution time |
| `reason` | String | Reason for the response |

---

## PropertyDetailBulkAPI

**API Endpoint:** `POST /v2/PropertyDetailBulk`

**Description:** Get property detail results from a list of IDs

**Business Purpose:** This API provides bulk property details for multiple properties, enabling efficient retrieval of comprehensive property information for portfolios or large datasets.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `input` | Object | The input parameters used for the request |
| `input.ids` | Array | Array of property IDs to retrieve |
| `input.prior_owner` | Boolean | Whether to include prior owner information |
| `input.legacy` | Boolean | Set legacy priority for priorId |
| `data` | Array | Array of property detail results (same structure as PropertyDetailAPI) |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `live` | Boolean | Indicates if the request was made with a live API key |
| `requestExecutionTimeMS` | String | The time taken to execute the request |
| `errorMessage` | String | Error message if applicable |

---

## PropertyLiensAPI

**API Endpoint:** `POST /v2/Reports/PropertyLiens`

**Description:** Retrieve property liens information including tax liens, judgment liens, and other encumbrances

**Business Purpose:** This API provides comprehensive lien information for properties, helping users identify financial encumbrances and legal claims against properties.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `live` | Boolean | Indicates if the request was made with a live API key |
| `input` | Object | The input parameters used for the request |
| `input.id` | Number | Property ID |
| `input.address` | String | Property address |
| `input.zip` | String | ZIP code |
| `input.apn` | String/null | Assessor Parcel Number |
| `input.fips` | String/null | FIPS code |
| `data` | Object | The lien data |
| `data.liens` | Array | Array of liens |
| `data.liens[].amount` | Number/null | Lien amount |
| `data.liens[].irsSerialNumber` | String | IRS serial number |
| `data.liens[].judgeVacatedDate` | String | Judge vacated date |
| `data.liens[].originFilingDate` | String | Origin filing date |
| `data.liens[].releaseDate` | String | Release date |
| `data.liens[].filingJurisdiction` | String | Filing jurisdiction |
| `data.liens[].filingJurisdictionName` | String | Filing jurisdiction name |
| `data.liens[].filings` | Array/null | Filing information |
| `data.liens[].filings[].agencyName` | String | Agency name |
| `data.liens[].filings[].agencyCounty` | String | Agency county |
| `data.liens[].filings[].agencyState` | String | Agency state |
| `data.liens[].filings[].filingDate` | String | Filing date |
| `data.liens[].filings[].filingNumber` | String | Filing number |
| `data.liens[].filings[].filingType` | String | Filing type |
| `data.liens[].creditors` | Array/null | Creditor information |
| `data.liens[].creditors[].name` | String | Creditor name |
| `data.liens[].creditors[].address` | String | Creditor address |
| `data.liens[].debtors` | Array/null | Debtor information |
| `data.liens[].debtors[].name` | String | Debtor name |
| `data.liens[].debtors[].address` | String | Debtor address |
| `data.liens[].status` | String | Lien status ('Released' or 'Active') |
| `data.property` | Object | Property information |
| `data.property.id` | Number/null | Property ID |
| `data.property.fips` | String | FIPS code |
| `data.property.apn` | String | Assessor Parcel Number |
| `data.property.address` | String | Property address |
| `data.property.useCode` | String | Use code |
| `data.property.useCodeDescription` | String | Use code description |
| `data.property.owner` | String | Property owner |
| `resultCount` | Number | The number of results returned |
| `recordCount` | Number | The number of records returned |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `warning` | String | Warning message if applicable |
| `errorMessage` | String | Error message if applicable |
| `requestExecutionTimeMS` | String | The time taken to execute the request |

---

## PropertyMappingAPI

**API Endpoint:** `POST /v2/PropertyMapping`

**Description:** Get latitude, longitude, and REAPI id for properties matching search query

**Business Purpose:** This API provides geolocation data for properties, enabling mapping and spatial analysis of property search results.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `input` | Object | The input parameters used for the request |
| `data` | Array | Array of property mapping results |
| `data[].id` | Number | Property ID |
| `data[].latitude` | Number | Latitude coordinate |
| `data[].longitude` | Number | Longitude coordinate |
| `resultCount` | Number/null | The total number of results available |
| `resultIndex` | Number/null | The index of the last result returned |
| `recordCount` | Number/null | The number of records returned |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `credits` | Number | Credits used for the request |
| `requestExecutionTimeMS` | String | The time taken to execute the request |

---

## PropertySearchAPI

**API Endpoint:** `POST /v2/PropertySearch`

**Description:** Get a list of property search results

**Business Purpose:** This API provides comprehensive property search functionality with advanced filtering capabilities, enabling users to find properties based on various criteria including location, price, features, and lead types.

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `live` | Boolean | Indicates if the request was made with a live API key |
| `input` | Object | The input parameters used for the request |
| `data` | Array | Array of property search results |
| `data[].id` | Number/null | Property ID |
| `data[].vacant` | Boolean/null | Indicates if the property is vacant |
| `data[].absenteeType` | String/null | Absentee type |
| `data[].absenteeOwner` | Boolean/null | Indicates if the owner is absentee |
| `data[].corporateOwned` | Boolean/null | Indicates if the property is corporate owned |
| `data[].outOfStateAbsenteeOwner` | Boolean/null | Indicates if the absentee owner is out-of-state |
| `data[].inStateAbsenteeOwner` | Boolean/null | Indicates if the absentee owner is in-state |
| `data[].freeClear` | Boolean/null | Indicates if the property is free and clear |
| `data[].auction` | Boolean/null | Indicates if the property is in auction |
| `data[].auctionDate` | String/null | Auction date |
| `data[].ownerOccupied` | Boolean/null | Indicates if the property is owner-occupied |
| `data[].reo` | Boolean/null | Indicates if the property is REO (Real Estate Owned) |
| `data[].death` | Boolean/null | Indicates if there was a death associated with the property |
| `data[].foreclosure` | Boolean/null | Indicates if the property is in foreclosure |
| `data[].MFH2to4` | Boolean/null | Multi-family home with 2-4 units |
| `data[].MFH5plus` | Boolean/null | Multi-family home with 5+ units |
| `data[].mlsActive` | Boolean/null | Indicates if the listing is active |
| `data[].mlsSold` | Boolean/null | Indicates if the property is sold |
| `data[].mlsFailed` | Boolean/null | Indicates if the listing failed |
| `data[].mlsPending` | Boolean/null | Indicates if the listing is pending |
| `data[].mlsCancelled` | Boolean/null | Indicates if the listing is cancelled |
| `data[].mlsHasPhotos` | Boolean/null | Indicates if the listing has photos |
| `data[].airConditioningAvailable` | Boolean/null | Indicates if air conditioning is available |
| `data[].preForeclosure` | Boolean/null | Indicates if the property is in pre-foreclosure |
| `data[].judgment` | Boolean/null | Indicates if there is a judgment on the property |
| `data[].forSale` | Boolean/null | Indicates if the property is for sale |
| `data[].cashBuyer` | Boolean/null | Indicates if the buyer paid cash |
| `data[].investorBuyer` | Boolean/null | Indicates if the buyer is an investor |
| `data[].highEquity` | Boolean/null | Indicates if the property has high equity |
| `data[].negativeEquity` | Boolean/null | Indicates if the property has negative equity |
| `data[].inherited` | Boolean/null | Indicates if the property was inherited |
| `data[].privateLender` | Boolean/null | Indicates if the lender is private |
| `data[].equity` | Boolean/null | Property equity |
| `data[].adjustableRate` | Boolean/null | Indicates if the mortgage has an adjustable rate |
| `data[].assumable` | Boolean/null | Indicates if the mortgage is assumable |
| `data[].patio` | Boolean/null | Indicates if the property has a patio |
| `data[].patioArea` | Number/null | Patio area |
| `data[].pool` | Boolean/null | Indicates if the property has a pool |
| `data[].poolArea` | Number/null | Pool area |
| `data[].deck` | Boolean/null | Indicates if the property has a deck |
| `data[].deckArea` | Number/null | Deck area |
| `data[].floodZone` | Boolean/null | Indicates if the property is in a flood zone |
| `data[].floodZoneType` | String/null | Flood zone type |
| `data[].floodZoneDescription` | String/null | Flood zone description |
| `data[].hoa` | Boolean/null | Indicates if there is an HOA |
| `data[].loanTypeCode` | String/null | Loan type code |
| `data[].propertyId` | Number/null | Property ID |
| `data[].bedrooms` | Number/null | Number of bedrooms |
| `data[].bathrooms` | Number/null | Number of bathrooms |
| `data[].stories` | Number/null | Number of stories |
| `data[].unitsCount` | Number/null | Number of units |
| `data[].roomsCount` | Number/null | Number of rooms |
| `data[].yearBuilt` | Number/null | Year built |
| `data[].squareFeet` | Number/null | Square footage |
| `data[].estimatedValue` | Number/null | Estimated value |
| `data[].assessedValue` | Number/null | Assessed value |
| `data[].assessedLandValue` | Number/null | Assessed land value |
| `data[].assessedImprovementValue` | Number/null | Assessed improvement value |
| `data[].estimatedEquity` | Number/null | Estimated equity |
| `data[].equityPercent` | Number/null | Equity percentage |
| `data[].rentAmount` | Number/null | Rent amount |
| `data[].yearsOwned` | Number/null | Years owned |
| `data[].maturityDateFirst` | String/null | Maturity date of first mortgage |
| `data[].lastSaleDate` | String/null | Last sale date |
| `data[].lastSaleAmount` | Any/null | Last sale amount |
| `data[].lastSaleArmsLength` | Boolean/null | Indicates if the last sale was at arm's length |
| `data[].recordingDate` | String/null | Recording date |
| `data[].noticeType` | String/null | Notice type |
| `data[].priorOwnerIndividual` | Boolean/null | Indicates if the prior owner was an individual |
| `data[].priorOwnerMonthsOwned` | Number/null | Months owned by prior owner |
| `data[].priorSaleAmount` | Number/null | Prior sale amount |
| `data[].documentType` | String/null | Document type |
| `data[].documentTypeCode` | String/null | Document type code |
| `data[].lienDocumentType` | String/null | Lien document type |
| `data[].listingAmount` | Number/null | Listing amount |
| `data[].mlsListingPrice` | Number/null | MLS listing price |
| `data[].mlsStatus` | String/null | MLS status |
| `data[].mlsType` | String/null | MLS type |
| `data[].mlsListingDate` | String/null | MLS listing date |
| `data[].mlsDaysOnMarket` | Number/null | Number of days on market |
| `data[].mlsFailedDate` | String/null | Date the listing failed |
| `data[].mlsLastStatusDate` | String/null | Last MLS status date |
| `data[].mlsLastSaleDate` | String/null | Last MLS sale date |
| `data[].mlsSoldPrice` | Any/null | MLS sold price |
| `data[].lotSquareFeet` | Number/null | Lot size in square feet |
| `data[].latitude` | Number/null | Latitude coordinate |
| `data[].longitude` | Number/null | Longitude coordinate |
| `data[].openMortgageBalance` | Number/null | Open mortgage balance |
| `data[].lastMortgage1Amount` | Number/null | Last mortgage amount |
| `data[].apn` | String/null | Assessor Parcel Number |
| `data[].parcelAccountNumber` | String/null | Parcel account number |
| `data[].landUse` | String/null | Land use |
| `data[].propertyType` | String/null | Property type |
| `data[].propertyUse` | String/null | Property use |
| `data[].propertyUseCode` | Number/null | Property use code |
| `data[].owner1FirstName` | String/null | First name of owner 1 |
| `data[].owner1LastName` | String/null | Last name of owner 1 |
| `data[].owner2FirstName` | String/null | First name of owner 2 |
| `data[].owner2LastName` | String/null | Last name of owner 2 |
| `data[].companyName` | String/null | Company name |
| `data[].owner2Company` | String/null | Company of owner 2 |
| `data[].garage` | Boolean/null | Indicates if the property has a garage |
| `data[].basement` | Boolean/null | Indicates if the property has a basement |
| `data[].taxLien` | Boolean/null | Indicates if there is a tax lien |
| `data[].taxDelinquentYear` | Any/null | Tax delinquent year |
| `data[].amountEstimated` | Boolean/null | Indicates if the amount is estimated |
| `data[].lenderName` | String/null | Lender name |
| `data[].address` | Object | Property address |
| `data[].address.zip` | String/null | ZIP code |
| `data[].address.city` | String/null | City |
| `data[].address.county` | String/null | County |
| `data[].address.fips` | String/null | FIPS code |
| `data[].address.state` | String/null | State |
| `data[].address.street` | String/null | Street |
| `data[].address.address` | String/null | Full address |
| `data[].mailAddress` | Object | Mailing address |
| `data[].mailAddress.zip` | String/null | ZIP code |
| `data[].mailAddress.city` | String/null | City |
| `data[].mailAddress.county` | String/null | County |
| `data[].mailAddress.state` | String/null | State |
| `data[].mailAddress.street` | String/null | Street |
| `data[].mailAddress.address` | String/null | Full address |
| `data[].taxType` | String/null | Tax type |
| `data[].imageUrl` | String/null | Image URL |
| `data[].age` | Number/null | Age of the property |
| `data[].pricePerSquareFoot` | Number/null | Price per square foot |
| `data[].neighborhood` | Any/null | Neighborhood |
| `data[].medianIncome` | Any/null | Median income |
| `data[].suggestedRent` | Any/null | Suggested rent |
| `data[].totalPropertiesOwned` | Number/null | Total properties owned |
| `data[].totalPortfolioValue` | Number/null | Total portfolio value |
| `data[].totalPortfolioEquity` | Number/null | Total portfolio equity |
| `data[].totalPortfolioMortgageBalance` | Number/null | Total portfolio mortgage balance |
| `data[].portfolioPurchasedLast6Months` | Number/null | Portfolio purchased in last 6 months |
| `data[].portfolioPurchasedLast12Months` | Number/null | Portfolio purchased in last 12 months |
| `data[].roofConstruction` | String/null | Roof construction |
| `data[].roofMaterial` | String/null | Roof material |
| `data[].lastUpdateDate` | String/null | Last update date |
| `resultCount` | Number/null | The total number of results available |
| `resultIndex` | Number/null | The index of the last result returned |
| `recordCount` | Number/null | The number of records returned |
| `statusCode` | Number | The HTTP status code |
| `statusMessage` | String | The status message |
| `requestExecutionTimeMS` | String | The time taken to execute the request |
| `summary` | Object | Summary information (optional) |
| `summary.auction` | Number | Count of auction properties |
| `summary.highEquity` | Number | Count of high equity properties |
| `summary.freeClear` | Number | Count of free and clear properties |
| `summary.preForeclosure` | Number | Count of pre-foreclosure properties |
| `summary.vacant` | Number | Count of vacant properties |
| `summary.ownerOccupied` | Number | Count of owner-occupied properties |
| `summary.absenteeOwner` | Number | Count of absentee owner properties |
| `summary.inStateAbsenteeOwner` | Number | Count of in-state absentee owner properties |
| `summary.outOfStateAbsenteeOwner` | Number | Count of out-of-state absentee owner properties |
| `summary.corporateOwned` | Number | Count of corporate owned properties |
| `summary.cashBuyer` | Number | Count of cash buyer properties |
| `summary.investorBuyer` | Number | Count of investor buyer properties |
| `summary.reo` | Number | Count of REO properties |
| `summary.mlsActive` | Number | Count of active MLS properties |
| `summary.mlsPending` | Number | Count of pending MLS properties |
| `summary.privateLender` | Number | Count of private lender properties |
| `summary.MFH2to4` | Number | Count of multi-family homes with 2-4 units |
| `summary.MFH5plus` | Number | Count of multi-family homes with 5+ units |
| `summary.medianListingPrice` | Number | Median listing price |
| `summary.medianDaysOnMarket` | Number | Median days on market |
| `aggregations` | Object | Aggregation data (optional) |
| `aggregations.leastListingPrice` | Number | Least listing price |
| `aggregations.greatestListingPrice` | Number | Greatest listing price |
| `aggregations.medianListingPrice` | Number | Median listing price |
| `aggregations.averageListingPrice` | Number | Average listing price |
| `aggregations.leastSoldPrice` | Number | Least sold price |
| `aggregations.greatestSoldPrice` | Number | Greatest sold price |
| `aggregations.medianSoldPrice` | Number | Median sold price |
| `aggregations.averageSoldPrice` | Number | Average sold price |

---

## Data Types Reference

### Common Data Types

- **String**: Text data
- **Number**: Numeric values (integers or floats)
- **Boolean**: True/false values
- **Array**: List of items
- **Object**: Structured data with key-value pairs
- **null**: Represents no value or empty field
- **Any**: Can be any data type

### Notes for RAG Systems

This documentation is structured to enable efficient retrieval of API response schema information. Each API section includes:

1. **API Endpoint**: The exact URL path and HTTP method
2. **Description**: Brief functional description from the API definition
3. **Business Purpose**: Contextual information about the API's use cases
4. **Response Schema**: Comprehensive field documentation with types and descriptions

The schema documentation follows a consistent format for all APIs, making it easy to understand the data structure and field meanings across different endpoints in the Real Estate API v2 system.
# Real Estate OData API - Developer Guide

A complete guide for developers to integrate with the Real Estate Property Search OData API.

## 📋 Table of Contents
- [Authentication](#authentication)
- [Base URL & Endpoints](#base-url--endpoints)
- [Request Format](#request-format)
- [Response Format](#response-format)
- [Query Parameters](#query-parameters)
- [Supported Fields](#supported-fields)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [Rate Limits & Best Practices](#rate-limits--best-practices)
- [SDKs & Code Examples](#sdks--code-examples)

---

## 🔐 Authentication

All API requests require an API key to be included in the request headers.

### Required Header
```
x-api-key: YOUR_API_KEY_HERE
```

### Getting an API Key
Contact your API provider to obtain a valid API key. Each key is unique and should be kept secure.

### Authentication Example
```bash
curl -H "x-api-key: your-api-key-here" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$top=10"
```

---

## 🌐 Base URL & Endpoints

### Base URL
```
https://api.realestateapi.com/v2
```

### Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/PropertySearch/odata` | GET | Main property search with OData query support |
| `/health` | GET | API health check (no authentication required) |

---

## 📝 Request Format

### HTTP Method
All requests use the `GET` method.

### Required Headers
```
x-api-key: YOUR_API_KEY_HERE
Content-Type: application/json
```

### URL Structure
```
GET /PropertySearch/odata?[odata-parameters]
```

---

## 📊 Response Format

All successful responses follow the OData v4 JSON format:

```json
{
  "@odata.context": "$metadata#PropertySearch",
  "@odata.count": 1234,
  "value": [
    {
      "id": 12345,
      "propertyId": 12345,
      "address": {
        "street": "123 Main St",
        "city": "Austin",
        "state": "TX",
        "zip": "78701",
        "county": "Travis",
        "fips": "48453"
      },
      "propertyInfo": {
        "bedrooms": 3,
        "bathrooms": 2.5,
        "squareFeet": 2100,
        "yearBuilt": 2010,
        "latitude": 30.2672,
        "longitude": -97.7431
      },
      "estimatedValue": 650000,
      "estimatedEquity": 150000,
      "ownerInfo": {
        "absenteeOwner": false,
        "corporateOwned": false,
        "ownerOccupied": true
      },
      "vacant": false,
      "auction": false,
      "foreclosure": false,
      "mlsActive": false,
      "lastSaleDate": "2020-05-15",
      "lastSaleAmount": 500000
    }
  ]
}
```

### Response Fields Description

| Field | Type | Description |
|-------|------|-------------|
| `@odata.context` | string | OData metadata context |
| `@odata.count` | number | Total number of matching properties |
| `value` | array | Array of property objects |

---

## 🔍 Query Parameters

The API supports standard OData query parameters:

| Parameter | Description | Example |
|--------|-------------|---------|
| `$filter` | Filter results | `$filter=city eq 'Austin'` |
| `$top` | Limit results (max 1000) | `$top=10` |
| `$skip` | Skip results for pagination | `$skip=20` |
| `$orderby` | Sort results | `$orderby=estimatedValue desc` |
| `$count` | Include total count | `$count=true` |


### $filter
Filter properties based on field values.

**Syntax:** `$filter=field operator value`

**Supported Operators:**
- `eq` - equals
- `ne` - not equals  
- `gt` - greater than
- `gte` - greater than or equal
- `lt` - less than
- `lte` - less than or equal
- `and` - logical AND
- `or` - logical OR
- `not` - logical NOT

| Operator | Description | Example |
|----------|-------------|---------|
| `eq` | Equals | `city eq 'Austin'` |
| `ne` | Not equals | `vacant ne true` |
| `gt` | Greater than | `estimatedValue gt 500000` |
| `gte` | Greater than or equal | `bedrooms gte 3` |
| `lt` | Less than | `yearBuilt lt 2000` |
| `lte` | Less than or equal | `bathrooms lte 2` |
| `and` | Logical AND | `bedrooms eq 3 and bathrooms gt 2` |
| `or` | Logical OR | `vacant eq true or absenteeOwner eq true` |
| `not` | Logical NOT | `not (mlsActive eq true)` |


**Field-to-Field Comparisons:**
The API supports comparing two fields directly, including both top-level and nested field comparisons.

**Supported Patterns:**
- Top-level fields: `estimatedValue gt mlsListingPrice`
- Nested fields: `propertyInfo.bedrooms gt propertyInfo.bathrooms`
- Mixed levels: `estimatedValue gt taxInfo.assessedValue`

**Performance Note:** Field-to-field comparisons use null-checking for robustness. These are slightly slower than term/range queries, so consider pagination for large datasets.

**Examples:**
```
$filter=estimatedValue gt 500000
$filter=absenteeOwner eq true
$filter=estimatedValue gt mlsListingPrice
$filter=estimatedEquity gt openMortgageBalance
$filter=propertyInfo.bedrooms gt propertyInfo.bathrooms
$filter=taxInfo.assessedValue eq taxInfo.marketValue
$filter=estimatedValue gt 300000 and estimatedValue gt mlsListingPrice
```

### $top
Limit the number of results returned (max: 1000).

**Syntax:** `$top=number`

**Example:**
```
$top=25
```

### $skip
Skip a number of results for pagination.

**Syntax:** `$skip=number`

**Example:**
```
$skip=50
```

### $orderby
Sort results by one or more fields.

**Syntax:** `$orderby=field [asc|desc]`

**Examples:**
```
$orderby=estimatedValue desc
$orderby=propertyInfo.yearBuilt asc,estimatedValue desc
```

### $count
Include total count in response.

**Syntax:** `$count=true`

**Example:**
```
$count=true
```

---

## 🏠 Supported Fields

### Property Details
- `propertyInfo.bedrooms` - Number of bedrooms
- `propertyInfo.bathrooms` - Number of bathrooms  
- `propertyInfo.livingSquareFeet` - Square footage
- `propertyInfo.lotSquareFeet` - Lot size in square feet
- `propertyInfo.yearBuilt` - Year property was built
- `propertyInfo.stories` - Number of stories
- `propertyInfo.unitsCount` - Number of units
- `propertyInfo.roomsCount` - Total room count
- `propertyInfo.propertyUse` - Property use classification
- `propertyInfo.construction` - Construction type

### Address Information
- `propertyInfo.address.city` - City name
- `propertyInfo.address.state` - State abbreviation
- `propertyInfo.address.zip` - ZIP code
- `propertyInfo.address.county` - County name
- `propertyInfo.address.street` - Street address
- `propertyInfo.address.fips` - FIPS code

### Location Data
- `propertyInfo.latitude` - Latitude coordinate
- `propertyInfo.longitude` - Longitude coordinate
- `location` - Geo point (for geo queries)

### Financial Information
- `estimatedValue` - Estimated property value
- `estimatedEquity` - Estimated equity amount
- `estimatedMortgageBalance` - Estimated mortgage balance
- `openMortgageBalance` - Open mortgage balance
- `equityPercent` - Equity percentage
- `lastSalePrice` - Last sale amount
- `mlsListingPrice` - MLS listing price
- `mlsSoldPrice` - MLS sold price

### Tax Information
- `taxInfo.assessedValue` - Assessed value
- `taxInfo.assessedLandValue` - Assessed land value
- `taxInfo.assessedImprovementValue` - Assessed improvement value
- `taxInfo.marketValue` - Market value
- `taxInfo.taxAmount` - Tax amount
- `taxInfo.taxDelinquentYear` - Tax delinquent year

### Owner Information
- `ownerInfo.absenteeOwner` - Is absentee owner
- `ownerInfo.corporateOwned` - Is corporate owned
- `ownerInfo.ownerOccupied` - Is owner occupied
- `ownerInfo.instateAbsenteeOwner` - In-state absentee owner
- `ownerInfo.outOfStateAbsenteeOwner` - Out-of-state absentee owner
- `ownerInfo.owner1FirstName` - Primary owner first name
- `ownerInfo.owner1LastName` - Primary owner last name
- `ownerInfo.companyName` - Company name (if corporate)
- `ownerInfo.ownershipLength` - Length of ownership in months

### Property Status Flags
- `vacant` - Property is vacant
- `absenteeOwner` - Has absentee owner
- `corporateOwned` - Corporate owned
- `auction` - Is in auction
- `foreclosure` - In foreclosure
- `preForeclosure` - In pre-foreclosure
- `bankOwned` - Bank owned/REO
- `freeClear` - Free and clear (no mortgage)
- `highEquity` - High equity property
- `inherited` - Inherited property
- `privateLender` - Has private lender
- `cashBuyer` - Purchased with cash
- `investorBuyer` - Purchased by investor

### MLS Information
- `mlsActive` - Currently active on MLS
- `mlsSold` - Sold via MLS
- `mlsFailed` - Failed MLS listing
- `mlsPending` - Pending MLS sale
- `mlsCancelled` - Cancelled MLS listing
- `mlsHasPhotos` - Has MLS photos
- `mlsStatus` - MLS status
- `mlsType` - MLS property type
- `mlsListingDate` - MLS listing date
- `mlsDaysOnMarket` - Days on MLS market

### Dates
- `lastSaleDate` - Last sale date
- `mlsListingDate` - MLS listing date
- `mlsFailedDate` - MLS failed date
- `mlsLastStatusDate` - Last MLS status change date

### Property Features
- `propertyInfo.pool` - Has pool
- `propertyInfo.poolArea` - Pool area
- `propertyInfo.patio` - Has patio
- `propertyInfo.deck` - Has deck
- `propertyInfo.fireplace` - Has fireplace
- `propertyInfo.garage` - Has garage
- `propertyInfo.basement` - Has basement
- `floodZone` - In flood zone
- `floodZoneType` - Flood zone type

---

## 💡 Examples

### Basic Property Search

```bash
# Get first 10 properties (requires API key)
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?$top=10"

# Filter by city
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=propertyInfo.address.city eq 'Austin'"

# Filter with pagination and sorting
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=estimatedValue gt 500000&\$top=5&\$orderby=estimatedValue desc"
```


### Filter by City
```bash
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=propertyInfo.address.city eq 'Austin'&$top=25"
```

### High-Value Properties with Multiple Conditions
```bash
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=estimatedValue gt 750000 and propertyInfo.bedrooms gte 4 and propertyInfo.bathrooms gte 3&$orderby=estimatedValue desc&$top=20"
```

### Absentee Owner Properties
```bash
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=ownerInfo.absenteeOwner eq true and estimatedEquity gt 100000&$orderby=estimatedEquity desc&$top=50"
```

### Investment Opportunities
```bash
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=(vacant eq true or absenteeOwner eq true) and estimatedValue lt 500000&$orderby=estimatedValue asc&$top=100"
```

### Field-to-Field Comparisons
```bash
# Properties where estimated value exceeds MLS listing price
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=estimatedValue gt mlsListingPrice&$top=25"

# Properties with high equity (estimated equity > mortgage balance)
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=estimatedEquity gt openMortgageBalance&$orderby=estimatedEquity desc&$top=50"

# Complex field comparison with literal constraints
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=estimatedValue gt 400000 and estimatedValue gt mlsListingPrice and estimatedEquity gt 100000&$top=30"

# Nested field comparisons
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=propertyInfo.bedrooms gt propertyInfo.bathrooms&$top=25"

# Mixed field comparisons (nested to top-level)
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=estimatedValue gt taxInfo.assessedValue and propertyInfo.livingSquareFeet gte propertyInfo.lotSquareFeet&$top=20"
```

### Recently Built Properties
```bash
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=propertyInfo.yearBuilt gt 2015 and propertyInfo.address.state eq 'TX'&$top=30"
```

### Pagination Example
```bash
# Page 1 (results 1-25)
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=propertyInfo.address.city eq 'Houston'&$top=25&$skip=0&$count=true"

# Page 2 (results 26-50)  
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=propertyInfo.address.city eq 'Houston'&$top=25&$skip=25"
```

### Complex Query with Multiple Filters
```bash
curl -H "x-api-key: your-api-key" \
  "https://api.realestateapi.com/v2/PropertySearch/odata?$filter=propertyInfo.address.state eq 'CA' and estimatedValue gt 600000 and estimatedValue lt 1200000 and propertyInfo.bedrooms gte 3 and not (mlsActive eq true)&$orderby=estimatedValue desc,propertyInfo.yearBuilt desc&$top=50&$count=true"
```

### More Advanced Filtering
```bash
# Multiple conditions with AND
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=propertyInfo.bedrooms eq 3 and propertyInfo.bathrooms gt 2"

# Multiple conditions with OR
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=vacant eq true or absenteeOwner eq true"

# Range queries
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=estimatedValue gt 300000 and estimatedValue lt 800000"

# Nested field queries
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=ownerInfo.absenteeOwner eq true and propertyInfo.yearBuilt gt 2000"

# Field-to-field comparisons (top-level)
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=estimatedValue gt mlsListingPrice"

# Nested field-to-field comparisons
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=propertyInfo.bedrooms gt propertyInfo.bathrooms"
```

### Sorting and Pagination
```bash
# Sort by multiple fields
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$orderby=estimatedValue desc,propertyInfo.yearBuilt asc&\$top=10"

# Skip results (pagination)
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$skip=20&\$top=10"

# Get count
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$count=true&\$top=5"
```

---

## ⚠️ Error Handling

### HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid query parameters |
| 401 | Unauthorized - Invalid or missing API key |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

### Error Response Format
```json
{
  "error": "Invalid field(s) in query",
  "message": "The following fields are not valid",
  "details": {
    "invalidFields": ["nonExistentField"],
    "availableFields": ["propertyInfo.bedrooms", "propertyInfo.bathrooms", "..."]
  }
}
```

### Common Errors

#### Invalid API Key (401)
```json
{
  "error": "Invalid API key",
  "message": "Please provide a valid x-api-key header"
}
```

#### Invalid Field Name (400)
```json
{
  "error": "Invalid field(s) in query",
  "message": "Invalid field in query",
  "details": {
    "invalidFields": ["invalidFieldName"],
    "availableFields": ["propertyInfo.bedrooms", "propertyInfo.bathrooms", "..."]
  }
}
```

#### Invalid Filter Syntax (400)
```json
{
  "error": "Failed to parse $filter expression",
  "message": "Invalid OData query syntax"
}
```

---

## 🚀 Rate Limits & Best Practices

### Rate Limits
- **Requests per minute:** 100
- **Requests per hour:** 2,000
- **Daily limit:** 10,000

### Best Practices

1. **Use Specific Filters**
   - Always include meaningful filters to reduce response size
   - Avoid overly broad queries without filters

2. **Implement Pagination**
   - Use `$top` and `$skip` for large result sets
   - Recommended page size: 25-100 records

3. **Cache Results**
   - Cache responses when appropriate to reduce API calls
   - Property data typically updates daily

4. **Handle Errors Gracefully**
   - Implement retry logic for 5xx errors
   - Validate field names before making requests

5. **Optimize Queries**
   - Use `$count=true` only when needed
   - Sort results on indexed fields when possible

6. **Secure API Keys**
   - Never expose API keys in client-side code
   - Use environment variables for API key storage
   - Rotate API keys regularly

---

## 💻 SDKs & Code Examples

### JavaScript/Node.js
```javascript
const axios = require('axios');

class RealEstateAPI {
  constructor(apiKey, baseUrl = 'https://api.realestateapi.com/v2') {
    this.apiKey = apiKey;
    this.baseUrl = baseUrl;
  }

  async searchProperties(filters = {}) {
    const params = new URLSearchParams();
    
    if (filters.filter) params.append('$filter', filters.filter);
    if (filters.top) params.append('$top', filters.top);
    if (filters.skip) params.append('$skip', filters.skip);
    if (filters.orderby) params.append('$orderby', filters.orderby);
    if (filters.count) params.append('$count', 'true');

    try {
      const response = await axios.get(`${this.baseUrl}/PropertySearch/odata`, {
        headers: {
          'x-api-key': this.apiKey,
          'Content-Type': 'application/json'
        },
        params: Object.fromEntries(params)
      });
      
      return response.data;
    } catch (error) {
      if (error.response) {
        throw new Error(`API Error: ${error.response.data.message}`);
      }
      throw error;
    }
  }
}

// Usage Example
const api = new RealEstateAPI('your-api-key-here');

// Search for high-value properties in Austin
api.searchProperties({
  filter: "propertyInfo.address.city eq 'Austin' and estimatedValue gt 750000",
  top: 25,
  orderby: 'estimatedValue desc',
  count: true
}).then(result => {
  console.log(`Found ${result['@odata.count']} properties`);
  console.log('Properties:', result.value);
}).catch(error => {
  console.error('Error:', error.message);
});
```

### Python
```python
import requests
from urllib.parse import urlencode

class RealEstateAPI:
    def __init__(self, api_key, base_url='https://api.realestateapi.com/v2'):
        self.api_key = api_key
        self.base_url = base_url
    
    def search_properties(self, **filters):
        headers = {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        
        params = {}
        if 'filter' in filters:
            params['$filter'] = filters['filter']
        if 'top' in filters:
            params['$top'] = filters['top']
        if 'skip' in filters:
            params['$skip'] = filters['skip']
        if 'orderby' in filters:
            params['$orderby'] = filters['orderby']
        if 'count' in filters and filters['count']:
            params['$count'] = 'true'
        
        url = f"{self.base_url}/PropertySearch/odata"
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Usage Example
api = RealEstateAPI('your-api-key-here')

# Search for absentee owner properties
result = api.search_properties(
    filter="ownerInfo.absenteeOwner eq true and estimatedEquity gt 150000",
    top=50,
    orderby="estimatedEquity desc",
    count=True
)

print(f"Found {result['@odata.count']} properties")
for property in result['value']:
    print(f"Property {property['id']}: ${property['estimatedValue']:,}")
```

### PHP
```php
<?php

class RealEstateAPI {
    private $apiKey;
    private $baseUrl;
    
    public function __construct($apiKey, $baseUrl = 'https://api.realestateapi.com/v2') {
        $this->apiKey = $apiKey;
        $this->baseUrl = $baseUrl;
    }
    
    public function searchProperties($filters = []) {
        $params = [];
        
        if (isset($filters['filter'])) $params['$filter'] = $filters['filter'];
        if (isset($filters['top'])) $params['$top'] = $filters['top'];
        if (isset($filters['skip'])) $params['$skip'] = $filters['skip'];
        if (isset($filters['orderby'])) $params['$orderby'] = $filters['orderby'];
        if (isset($filters['count']) && $filters['count']) $params['$count'] = 'true';
        
        $url = $this->baseUrl . '/PropertySearch/odata?' . http_build_query($params);
        
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'Content-Type: application/json'
        ];
        
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        
        if ($httpCode === 200) {
            return json_decode($response, true);
        } else {
            throw new Exception("API Error: HTTP $httpCode");
        }
    }
}

// Usage Example
$api = new RealEstateAPI('your-api-key-here');

$result = $api->searchProperties([
    'filter' => "propertyInfo.address.state eq 'TX' and estimatedValue gt 500000",
    'top' => 30,
    'orderby' => 'estimatedValue desc',
    'count' => true
]);

echo "Found " . $result['@odata.count'] . " properties\n";
?>
```

### cURL Examples
```bash
# Basic search with authentication
curl -H "x-api-key: your-api-key" \
     -H "Content-Type: application/json" \
     "https://api.realestateapi.com/v2/PropertySearch/odata?$top=10"

# Complex search with multiple filters
curl -H "x-api-key: your-api-key" \
     -H "Content-Type: application/json" \
     -G \
     --data-urlencode '$filter=propertyInfo.address.city eq "Miami" and estimatedValue gt 800000 and propertyInfo.bedrooms gte 3' \
     --data-urlencode '$top=25' \
     --data-urlencode '$orderby=estimatedValue desc' \
     --data-urlencode '$count=true' \
     "https://api.realestateapi.com/v2/PropertySearch/odata"
```

---

## 📞 Support

For technical support, API issues, or questions about integration:

- **Documentation:** [Developer Portal](https://docs.realestate-api.com)
- **Email:** developers@realestate-api.com
- **Status Page:** [status.realestate-api.com](https://status.realestate-api.com)

---

---

## 📊 Field Data Catalogue

The following table contains all queryable fields available in the Real Estate OData API, organized by category with business descriptions and data types.

### Property Status & Lead Types

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `absenteeOwner` | boolean | Indicates if the owner of the property is not residing in it |
| `adjustableRate` | boolean | Indicates if the mortgage has an adjustable interest rate |
| `assumable` | boolean | Indicates if the mortgage is assumable by another buyer |
| `auction` | boolean | Indicates if the property is up for auction |
| `bankOwned` | boolean | Indicates if the property is owned by a bank |
| `cashBuyer` | boolean | Indicates if the buyer purchased the property with cash |
| `cashSale` | boolean | Indicates if the property was purchased with cash |
| `corporateOwned` | boolean | Indicates if the property is owned by a corporation |
| `death` | boolean | Indicates if the property is involved in an estate due to the owner's death |
| `deathTransfer` | boolean | Indicates if the property was transferred due to the owner's death |
| `deedInLieu` | boolean | Indicates if the property was transferred via a deed in lieu of foreclosure |
| `floodZone` | boolean | Indicates if the property is located in a flood zone |
| `freeClear` | boolean | Indicates if the property is free from any mortgage or liens |
| `highEquity` | boolean | Indicates if the property has a high equity percentage |
| `individualOwner` | boolean | Indicates if the owner is an individual person |
| `inherited` | boolean | Indicates if the property was inherited by the current owner |
| `inStateAbsenteeOwner` | boolean | Indicates if the absentee owner resides within the same state as the property |
| `investorBuyer` | boolean | Indicates if the buyer is an investor |
| `judgment` | boolean | Indicates if there is a legal judgment against the property |
| `lien` | boolean | Indicates if there is a lien on the property |
| `MFH2to4` | boolean | Indicates if the property is a multi-family home with 2 to 4 units |
| `MFH5plus` | boolean | Indicates if the property is a multi-family home with 5 or more units |
| `mobileHome` | boolean | Indicates if the property is a mobile home |
| `outOfStateAbsenteeOwner` | boolean | Indicates if the absentee owner resides outside the state where the property is located |
| `ownerOccupied` | boolean | Indicates if the property is occupied by the owner |
| `preForeclosure` | boolean | Indicates if the property is in pre-foreclosure status |
| `privateLender` | boolean | Indicates if the lender is a private entity |
| `quitClaim` | boolean | Indicates if the property was transferred via a quitclaim deed |
| `sheriffsDeed` | boolean | Indicates if the property was transferred via a sheriff's deed |
| `spousalDeath` | boolean | Indicates if the property is involved in an estate due to the death of a spouse |
| `taxLien` | boolean | Indicates if there is a tax lien on the property |
| `trusteeOwner` | boolean | Indicates if the property is owned by a trustee |
| `trusteeSale` | boolean | Indicates if the property was sold through a trustee sale |
| `vacant` | boolean | Indicates if the property is currently vacant |
| `warrantyDeed` | boolean | Indicates if the property was transferred via a warranty deed |

### Financial Information

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `availableEquity` | long | Equity available in the property for borrowing or selling purposes |
| `equityPercent` | integer | Percentage of the property value that is owned outright (equity) |
| `estimatedEquity` | long | Estimated equity in the property, calculated as property value minus mortgage balance |
| `estimatedMortgageBalance` | long | Estimated balance remaining on the property's mortgage |
| `estimatedMortgagePayment` | long | Estimated monthly mortgage payment |
| `estimatedValue` | long | Estimated market value of the property |
| `lastSalePrice` | long | Price at which the property was last sold |
| `openMortgageBalance` | long | Outstanding balance of any open mortgage on the property |

### Property Identification

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `id` | long | Unique identifier for the property record |
| `priorId` | long | Previous identifier for the property record |
| `listingKey` | text | Unique key associated with the property listing |
| `propertyType` | text | Type of the property (e.g., single-family, multi-family) |

### Dates

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `lastSaleDate` | date | Date when the property was last sold |
| `lastUpdateDate` | text | Date when the record was last updated |
| `maturityDateFirst` | date | Maturity date of the first mortgage |

### Location & Geography

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `location` | geo_point | Geographical location (latitude and longitude) |
| `floodZoneDescription` | text | Description of the flood zone associated with the property |
| `floodZoneType` | text | Type of flood zone the property is located in |

### Loan Information

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `loanTypeCodeFirst` | text | Code representing the type of the first mortgage loan |
| `loanTypeCodeSecond` | text | Code representing the type of the second mortgage loan |
| `loanTypeCodeThird` | text | Code representing the type of the third mortgage loan |
| `noticeType` | text | Type of foreclosure notice associated with the property |

### Property Information

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `propertyInfo.bedrooms` | long | Number of bedrooms in the property |
| `propertyInfo.bathrooms` | double | Number of bathrooms in the property |
| `propertyInfo.livingSquareFeet` | long | Total living area in square feet |
| `propertyInfo.lotSquareFeet` | long | Size of the lot in square feet |
| `propertyInfo.yearBuilt` | integer | Year the property was built |
| `propertyInfo.latitude` | double | Latitude of the property's location |
| `propertyInfo.longitude` | double | Longitude of the property's location |
| `propertyInfo.propertyUse` | text | Actual use of the property (e.g., single-family residence, rental) |
| `propertyInfo.propertyUseCode` | integer | Numeric code for property use classification |
| `propertyInfo.construction` | text | Construction type of the property |
| `propertyInfo.stories` | integer | Number of stories in the property |
| `propertyInfo.unitsCount` | integer | Number of units in the property |
| `propertyInfo.roomsCount` | integer | Total number of rooms in the property |
| `propertyInfo.fireplaces` | long | Number of fireplaces in the property |
| `propertyInfo.fireplace` | boolean | Indicates if the property has a fireplace |
| `propertyInfo.pool` | boolean | Indicates if the property has a pool |
| `propertyInfo.poolArea` | integer | Size of the pool area in square feet |
| `propertyInfo.patio` | boolean | Indicates if the property has a patio |
| `propertyInfo.patioArea` | text | Size of the patio area in square feet |
| `propertyInfo.deck` | boolean | Indicates if the property has a deck |
| `propertyInfo.deckArea` | integer | Size of the deck in square feet |
| `propertyInfo.attic` | boolean | Indicates if the property has an attic |
| `propertyInfo.carport` | boolean | Indicates if the property has a carport |
| `propertyInfo.garage` | boolean | Indicates if the property has a garage |
| `propertyInfo.garageType` | text | Type of garage at the property |
| `propertyInfo.garageSquareFeet` | long | Size of the garage in square feet |
| `propertyInfo.heatingType` | text | Type of heating system in the property |
| `propertyInfo.heatingFuelType` | text | Type of fuel used for heating (e.g., gas, electric) |
| `propertyInfo.airConditioningType` | text | Type of air conditioning system in the property |
| `propertyInfo.roofMaterial` | text | Material used for the roof |
| `propertyInfo.roofConstruction` | text | Construction type of the roof |

### Property Address

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `propertyInfo.address.address` | text | Full address of the property |
| `propertyInfo.address.city` | text | City where the property is located |
| `propertyInfo.address.county` | text | County where the property is located |
| `propertyInfo.address.state` | text | State where the property is located |
| `propertyInfo.address.zip` | text | ZIP code of the property address |
| `propertyInfo.address.zip4` | text | Extended ZIP+4 code for more precise delivery |
| `propertyInfo.address.house` | text | House number of the property address |
| `propertyInfo.address.street` | text | Street name of the property address |
| `propertyInfo.address.streetType` | text | Type of street (e.g., Avenue, Street, Boulevard) |
| `propertyInfo.address.unit` | text | Unit number of the property address |
| `propertyInfo.address.unitType` | text | Type of unit (e.g., apartment, suite) |
| `propertyInfo.address.preDirection` | text | Directional prefix for the street name (e.g., N, S, E, W) |
| `propertyInfo.address.fips` | text | Federal Information Processing Standards code for the property's location |
| `propertyInfo.address.carrierRoute` | text | Carrier route associated with the property address |
| `propertyInfo.address.congressionalDistrict` | text | Congressional district where the property is located |
| `propertyInfo.address.jurisdiction` | text | Governing jurisdiction of the property's location |
| `propertyInfo.address.label` | text | Label or tag for the address, typically for internal use |

### Owner Information

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `ownerInfo.absenteeOwner` | boolean | Indicates if the owner of the property is not residing in it |
| `ownerInfo.corporateOwned` | boolean | Indicates if the property is owned by a corporation |
| `ownerInfo.instateAbsenteeOwner` | boolean | Indicates if the absentee owner resides within the same state |
| `ownerInfo.outOfStateAbsenteeOwner` | boolean | Indicates if the absentee owner resides outside the state |
| `ownerInfo.ownerOccupied` | boolean | Indicates if the property is occupied by the owner |
| `ownerInfo.ownershipLength` | long | Length of ownership of the property in months |
| `ownerInfo.owner1FirstName` | text | First name of the first property owner |
| `ownerInfo.owner1FullName` | text | Full name of the first property owner |
| `ownerInfo.owner1LastName` | text | Last name of the first property owner |
| `ownerInfo.owner1Type` | text | Type of the first property owner (e.g., individual, company) |
| `ownerInfo.owner2FirstName` | text | First name of the second property owner |
| `ownerInfo.owner2FullName` | text | Full name of the second property owner |
| `ownerInfo.owner2LastName` | text | Last name of the second property owner |
| `ownerInfo.owner2Type` | text | Type of the second property owner |
| `ownerInfo.ownerNames` | text | Combined names of all property owners |
| `ownerInfo.companyName` | text | Name of the company owning the property |

### Owner Mail Address

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `ownerInfo.mailAddress.address` | text | Full mailing address of the property owner |
| `ownerInfo.mailAddress.city` | text | City of the owner's mailing address |
| `ownerInfo.mailAddress.county` | text | County of the owner's mailing address |
| `ownerInfo.mailAddress.state` | text | State of the owner's mailing address |
| `ownerInfo.mailAddress.zip` | text | ZIP code of the owner's mailing address |
| `ownerInfo.mailAddress.zip4` | text | Extended ZIP+4 code for the owner's mailing address |
| `ownerInfo.mailAddress.house` | text | House number of the owner's mailing address |
| `ownerInfo.mailAddress.street` | text | Street name of the owner's mailing address |
| `ownerInfo.mailAddress.streetType` | text | Type of street for the owner's mailing address |
| `ownerInfo.mailAddress.unit` | text | Unit number of the owner's mailing address |
| `ownerInfo.mailAddress.unitType` | text | Type of unit for the owner's mailing address |
| `ownerInfo.mailAddress.preDirection` | text | Directional prefix for the owner's mailing address |
| `ownerInfo.mailAddress.fips` | text | FIPS code for the owner's mailing address location |
| `ownerInfo.mailAddress.carrierRoute` | text | Carrier route for the owner's mailing address |
| `ownerInfo.mailAddress.carrierRouteFromDeed` | text | Carrier route derived from deed records |
| `ownerInfo.mailAddress.label` | text | Label for the owner's mailing address |
| `ownerInfo.mailAddress.addressFormat` | text | Formatted version of the owner's mailing address |

### Tax Information

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `taxInfo.assessedValue` | long | Value of the property as assessed by the county |
| `taxInfo.assessedLandValue` | long | Value of the land as assessed by the county |
| `taxInfo.assessedImprovementValue` | long | Value of improvements on the land (e.g., buildings) as assessed by the county |
| `taxInfo.marketValue` | long | Market value of the property |
| `taxInfo.marketLandValue` | long | Market value of the land |
| `taxInfo.marketImprovementValue` | long | Market value of the improvements on the land |
| `taxInfo.estimatedValue` | float | Estimated tax value of the property |
| `taxInfo.taxAmount` | long | Total amount of tax assessed on the property |
| `taxInfo.taxDelinquentYear` | long | Year in which the property taxes became delinquent |
| `taxInfo.assessmentYear` | long | Year of the most recent property assessment |
| `taxInfo.year` | long | Year of the tax assessment |
| `taxInfo.propertyId` | long | Unique identifier for the property in tax records |

### MLS (Multiple Listing Service)

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `mlsActive` | boolean | Indicates if the property is currently active in MLS |
| `mlsCancelled` | boolean | Indicates if the property was cancelled in MLS |
| `mlsFailed` | boolean | Indicates if the property failed to sell in MLS |
| `mlsFailedDate` | date | Date when the property failed to sell in MLS |
| `mlsHasPhotos` | boolean | Indicates if the MLS record has associated photos |
| `mlsPending` | boolean | Indicates if the property is pending sale in MLS |
| `mlsSold` | boolean | Indicates if the property was sold in MLS |
| `mlsStatus` | text | Current status of the property in MLS |
| `mlsType` | text | Type of MLS record (e.g., listing, sale) |
| `mlsListingDate` | date | Date when the property was listed in MLS |
| `mlsListingPrice` | long | Listing price of the property in MLS |
| `mlsListingAmount` | long | Listed amount of the property in MLS |
| `mlsSoldPrice` | long | Price at which the property was sold in MLS |
| `mlsDaysOnMarket` | long | Total number of days the property has been on the MLS |
| `mlsLastStatusDate` | date | Date when the status was last updated in MLS |
| `mlsLastSaleDate` | date | Date of the last sale of the property in MLS |
| `mlsTotalUpdates` | integer | Total number of updates made to the MLS record |

### Lot Information

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `lotInfo.apn` | text | Assessor's Parcel Number assigned by the county assessor |
| `lotInfo.apnUnformatted` | text | Unformatted version of the Assessor's Parcel Number |
| `lotInfo.lotSquareFeet` | long | Size of the lot in square feet |
| `lotInfo.lotAcres` | double | Size of the lot in acres |
| `lotInfo.lotWidthFeet` | float | Width of the lot in feet |
| `lotInfo.lotDepthFeet` | float | Depth of the lot in feet |
| `lotInfo.landUse` | text | Intended use of the land (e.g., residential, commercial) |
| `lotInfo.propertyClass` | text | Classification of the property according to tax records |
| `lotInfo.propertyUse` | text | Actual use of the property according to lot records |
| `lotInfo.zoning` | text | Zoning designation of the property |
| `lotInfo.subdivision` | text | Subdivision name where the property is located |
| `lotInfo.legalDescription` | text | Legal description of the property according to public records |
| `lotInfo.legalSection` | text | Section of the property in the legal description |
| `lotInfo.lotNumber` | text | Lot number assigned to the property |
| `lotInfo.censusBlock` | text | Census block where the property is located |
| `lotInfo.censusBlockGroup` | text | Census block group where the property is located |
| `lotInfo.censusTract` | text | Census tract where the property is located |

### Neighborhood Information

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `neighborhood.id` | long | Unique identifier for the neighborhood |
| `neighborhood.name` | text | Name of the neighborhood, school, or area |
| `neighborhood.type` | text | Type of neighborhood classification |
| `neighborhood.center` | geo_point | Geographical center of the neighborhood |

### Demographics & Market Data

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `demographics.fmrEfficiency` | text | Fair Market Rent (FMR) for efficiency units in the area |
| `demographics.fmrFourBedroom` | text | Fair Market Rent (FMR) for four-bedroom units in the area |
| `demographics.fmrOneBedroom` | text | Fair Market Rent (FMR) for one-bedroom units in the area |
| `demographics.fmrThreeBedroom` | text | Fair Market Rent (FMR) for three-bedroom units in the area |
| `demographics.fmrTwoBedroom` | text | Fair Market Rent (FMR) for two-bedroom units in the area |
| `demographics.fmrYear` | text | Fair Market Rent (FMR) year |
| `demographics.hudAreaCode` | text | HUD-defined area code |
| `demographics.hudAreaName` | text | HUD-defined area name |
| `demographics.medianIncome` | text | Median income of residents in the area |
| `demographics.suggestedRent` | text | Suggested rent price for properties in the area |

### Auction Information

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `auctionInfo.FIPSCode` | text | Federal Information Processing Standards code for auction location |
| `auctionInfo.active` | boolean | Indicates if the foreclosure or auction is active |
| `auctionInfo.auctionDate` | date | Date of the foreclosure auction |
| `auctionInfo.auctionStreetAddress` | text | Street address where the auction will take place |
| `auctionInfo.auctionTime` | text | Time of the foreclosure auction |
| `auctionInfo.caseNumber` | text | Case number associated with the foreclosure |
| `auctionInfo.defaultAmount` | text | Amount in default in the foreclosure |
| `auctionInfo.documentType` | text | Type of document associated with the auction |
| `auctionInfo.estimatedBankValue` | text | Estimated value of the property by the bank |
| `auctionInfo.foreclosureId` | text | Unique identifier for the foreclosure |
| `auctionInfo.judgmentAmount` | text | Judgment amount associated with the foreclosure |
| `auctionInfo.judgmentDate` | date | Date of the judgment in the foreclosure |
| `auctionInfo.lenderName` | text | Name of the lender for the mortgage |
| `auctionInfo.lenderPhone` | text | Phone number of the foreclosing lender |
| `auctionInfo.noticeType` | text | Type of foreclosure notice |
| `auctionInfo.openingBid` | text | Opening bid amount for the auction |
| `auctionInfo.originalLoanAmount` | text | Original amount of the loan in foreclosure |
| `auctionInfo.recordingDate` | date | Date when the mortgage or transaction was recorded |
| `auctionInfo.seqNo` | text | Sequence number for the auction record |
| `auctionInfo.trusteeAddress` | text | Address of the trustee handling the foreclosure |
| `auctionInfo.trusteeFullName` | text | Full name of the trustee handling the foreclosure |
| `auctionInfo.trusteePhone` | text | Phone number of the trustee handling the foreclosure |
| `auctionInfo.trusteeSaleNumber` | text | Trustee sale number for the foreclosure |
| `auctionInfo.typeName` | text | Name or type of the foreclosure or auction |

---

## 📄 License & Terms

By using this API, you agree to the [Terms of Service](https://realestate-api.com/terms) and [Privacy Policy](https://realestate-api.com/privacy).

---

*Last updated: 2024-06-25*
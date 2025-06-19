# Address Verification API

The Address Verification API validates, standardizes, and enriches address data to ensure accuracy in your real estate applications.

## Endpoint

```
POST /addresses/verify
```

## Request Body

```json
{
  "address": {
    "street": "123 Main Street",
    "unit": "Apt 4B",
    "city": "Austin",
    "state": "TX",
    "zip": "78701"
  },
  "options": {
    "standardize": true,
    "geocode": true,
    "validate_deliverability": true,
    "return_components": true
  }
}
```

## Parameters

### Address Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `street` | string | Yes | Street address including number |
| `unit` | string | No | Unit, apartment, or suite number |
| `city` | string | Yes* | City name |
| `state` | string | Yes* | Two-letter state code |
| `zip` | string | Yes* | 5 or 9 digit ZIP code |

*Either city/state or ZIP code is required

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `standardize` | boolean | true | Standardize to USPS format |
| `geocode` | boolean | true | Return coordinates |
| `validate_deliverability` | boolean | false | Check USPS deliverability |
| `return_components` | boolean | false | Return parsed components |

## Response

```json
{
  "status": "success",
  "data": {
    "is_valid": true,
    "confidence_score": 0.98,
    "original_address": {
      "street": "123 Main Street",
      "unit": "Apt 4B",
      "city": "Austin",
      "state": "TX",
      "zip": "78701"
    },
    "standardized_address": {
      "street": "123 Main St",
      "unit": "Apt 4B",
      "city": "Austin",
      "state": "TX",
      "zip": "78701-2345",
      "plus4": "2345",
      "formatted": "123 Main St Apt 4B, Austin, TX 78701-2345"
    },
    "components": {
      "primary_number": "123",
      "street_name": "Main",
      "street_suffix": "St",
      "street_predirection": "",
      "street_postdirection": "",
      "secondary_designator": "Apt",
      "secondary_number": "4B",
      "city": "Austin",
      "state": "TX",
      "zip": "78701",
      "plus4": "2345",
      "county": "Travis",
      "county_fips": "48453"
    },
    "geocode": {
      "latitude": 30.2672,
      "longitude": -97.7431,
      "accuracy": "rooftop",
      "census_tract": "48453001100",
      "census_block": "484530011001000"
    },
    "deliverability": {
      "is_deliverable": true,
      "delivery_type": "residential",
      "carrier_route": "C001",
      "dpv_confirmed": true,
      "vacant": false
    },
    "property_match": {
      "found": true,
      "property_id": "PROP123456",
      "apn": "123-456-789",
      "property_type": "condo"
    },
    "validation_flags": {
      "is_residential": true,
      "is_commercial": false,
      "is_po_box": false,
      "is_known_invalid": false,
      "requires_unit": true,
      "missing_unit": false
    }
  }
}
```

## Bulk Address Verification

Verify multiple addresses in a single request (up to 1,000):

### Endpoint
```
POST /addresses/verify/bulk
```

### Request Body
```json
{
  "addresses": [
    {
      "id": "addr1",
      "street": "123 Main St",
      "city": "Austin",
      "state": "TX",
      "zip": "78701"
    },
    {
      "id": "addr2",
      "street": "456 Oak Ave",
      "city": "Houston",
      "state": "TX",
      "zip": "77001"
    }
  ],
  "options": {
    "standardize": true,
    "geocode": true
  }
}
```

### Response
```json
{
  "status": "success",
  "data": {
    "results": [
      {
        "id": "addr1",
        "is_valid": true,
        "standardized_address": {
          "formatted": "123 Main St, Austin, TX 78701-2345"
        }
      },
      {
        "id": "addr2",
        "is_valid": true,
        "standardized_address": {
          "formatted": "456 Oak Ave, Houston, TX 77001-1234"
        }
      }
    ],
    "summary": {
      "total": 2,
      "valid": 2,
      "invalid": 0
    }
  }
}
```

## Address Autocomplete

Get address suggestions as users type:

### Endpoint
```
GET /addresses/autocomplete
```

### Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Partial address input |
| `limit` | integer | No | Max results (default: 10) |
| `bounds` | object | No | Geographic bounds |

### Example Request
```bash
curl -X GET "https://api.realestateapi.com/v1/addresses/autocomplete?query=123%20Main&limit=5" \
  -H "X-API-Key: YOUR_API_KEY"
```

### Response
```json
{
  "status": "success",
  "data": {
    "suggestions": [
      {
        "address": "123 Main St, Austin, TX 78701",
        "components": {
          "street": "123 Main St",
          "city": "Austin",
          "state": "TX",
          "zip": "78701"
        },
        "confidence": 0.95
      }
    ]
  }
}
```

## Error Handling

### Invalid Address
```json
{
  "status": "success",
  "data": {
    "is_valid": false,
    "confidence_score": 0.2,
    "validation_errors": [
      {
        "code": "STREET_NOT_FOUND",
        "message": "Street name not found in the specified city"
      }
    ],
    "suggestions": [
      {
        "address": "123 Main St, Austin, TX 78701",
        "confidence": 0.85
      }
    ]
  }
}
```

## Use Cases

1. **Lead Capture Forms**: Validate addresses in real-time
2. **Property Listings**: Standardize addresses before saving
3. **Marketing Campaigns**: Verify mailing addresses
4. **Analytics**: Geocode addresses for mapping
5. **Data Import**: Clean and standardize bulk address data

## Best Practices

1. **Always validate** addresses before storing
2. **Use autocomplete** to reduce errors during input
3. **Handle suggestions** when validation fails
4. **Store standardized** addresses for consistency
5. **Cache results** to reduce API calls
6. **Batch process** for bulk operations
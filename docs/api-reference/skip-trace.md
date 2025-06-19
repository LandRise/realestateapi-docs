# Skip Trace API

The Skip Trace API helps you find property owner contact information, verify identities, and locate hard-to-reach individuals for real estate transactions.

## Endpoint

```
POST /skip-trace/search
```

## Request Body

```json
{
  "search_criteria": {
    "name": {
      "first": "John",
      "last": "Doe",
      "middle": "A"
    },
    "address": {
      "street": "123 Main St",
      "city": "Austin",
      "state": "TX",
      "zip": "78701"
    },
    "phone": "512-555-0123",
    "email": "john.doe@email.com",
    "ssn_last4": "1234"
  },
  "search_type": "person",
  "options": {
    "include_relatives": true,
    "include_associates": true,
    "include_property_history": true,
    "include_phone_history": true,
    "max_results": 10
  }
}
```

## Parameters

### Search Types
- `person` - Find individual contact information
- `property_owner` - Find property owner details
- `business` - Find business entity information

### Search Criteria

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | object | Yes* | Person's name components |
| `address` | object | Yes* | Current or previous address |
| `phone` | string | Yes* | Phone number (any format) |
| `email` | string | Yes* | Email address |
| `ssn_last4` | string | No | Last 4 digits of SSN |

*At least one search criteria is required

## Response

```json
{
  "status": "success",
  "data": {
    "matches": [
      {
        "confidence_score": 0.95,
        "person": {
          "full_name": "John Andrew Doe",
          "first_name": "John",
          "middle_name": "Andrew",
          "last_name": "Doe",
          "age": 45,
          "date_of_birth": "1979-05-15"
        },
        "current_address": {
          "street": "123 Main St",
          "city": "Austin",
          "state": "TX",
          "zip": "78701",
          "county": "Travis",
          "resident_length_years": 3,
          "move_date": "2021-03-01",
          "property_type": "single_family",
          "ownership_status": "owner"
        },
        "contact_information": {
          "phones": [
            {
              "number": "512-555-0123",
              "type": "mobile",
              "carrier": "AT&T",
              "is_current": true,
              "do_not_call": false,
              "last_verified": "2024-01-15"
            },
            {
              "number": "512-555-0456",
              "type": "landline",
              "is_current": true
            }
          ],
          "emails": [
            {
              "address": "john.doe@email.com",
              "is_current": true,
              "last_verified": "2024-01-10"
            },
            {
              "address": "jdoe@work.com",
              "is_current": true
            }
          ]
        },
        "previous_addresses": [
          {
            "street": "456 Oak Ave",
            "city": "Houston",
            "state": "TX",
            "zip": "77001",
            "move_in_date": "2015-06-01",
            "move_out_date": "2021-02-28"
          }
        ],
        "property_ownership": [
          {
            "address": "123 Main St, Austin, TX 78701",
            "property_type": "single_family",
            "ownership_type": "sole_owner",
            "purchase_date": "2021-03-15",
            "purchase_price": 450000,
            "estimated_value": 525000,
            "property_id": "PROP123456"
          },
          {
            "address": "789 Beach Rd, Galveston, TX 77550",
            "property_type": "condo",
            "ownership_type": "joint_tenant",
            "purchase_date": "2019-08-20",
            "purchase_price": 250000
          }
        ],
        "relatives": [
          {
            "name": "Jane Mary Doe",
            "relationship": "spouse",
            "age": 43,
            "current_address": "123 Main St, Austin, TX 78701"
          },
          {
            "name": "Robert Doe",
            "relationship": "father",
            "age": 72,
            "current_address": "999 Elm St, Dallas, TX 75201"
          }
        ],
        "associates": [
          {
            "name": "Michael Smith",
            "relationship": "business_partner",
            "shared_addresses": 0,
            "shared_phones": 1
          }
        ],
        "social_media": {
          "linkedin": "linkedin.com/in/johndoe",
          "facebook": "facebook.com/john.doe.123"
        },
        "financial_indicators": {
          "estimated_income_range": "$75,000-$100,000",
          "estimated_net_worth_range": "$500,000-$750,000",
          "bankruptcy_records": false,
          "lien_records": false
        },
        "verification_data": {
          "ssn_verified": true,
          "identity_confidence": "high",
          "fraud_indicators": []
        }
      }
    ],
    "search_metadata": {
      "total_matches": 1,
      "search_time_ms": 1250,
      "data_sources": ["public_records", "credit_headers", "utility_records"]
    }
  }
}
```

## Bulk Skip Trace

Process multiple skip trace requests (up to 100):

### Endpoint
```
POST /skip-trace/bulk
```

### Request Body
```json
{
  "searches": [
    {
      "id": "search1",
      "name": {
        "first": "John",
        "last": "Doe"
      },
      "address": {
        "street": "123 Main St",
        "city": "Austin",
        "state": "TX"
      }
    }
  ],
  "options": {
    "include_property_history": true
  }
}
```

## Property Owner Lookup

Find owner information for a specific property:

### Endpoint
```
POST /skip-trace/property-owner
```

### Request Body
```json
{
  "property": {
    "address": "123 Main St, Austin, TX 78701",
    "apn": "123-456-789"
  },
  "options": {
    "include_contact_info": true,
    "include_ownership_history": true
  }
}
```

## Reverse Phone Lookup

Find person information from a phone number:

### Endpoint
```
POST /skip-trace/reverse-phone
```

### Request Body
```json
{
  "phone": "512-555-0123",
  "options": {
    "include_address": true,
    "include_relatives": true
  }
}
```

## Compliance and Best Practices

### Legal Compliance
- Ensure compliance with FCRA, TCPA, and state laws
- Use only for permissible purposes
- Maintain proper consent documentation
- Respect Do Not Call lists

### Permissible Use Cases
1. **Locating property owners** for acquisitions
2. **Verifying seller identity** in transactions
3. **Finding heirs** for probate properties
4. **Contacting absentee owners**
5. **Due diligence** for real estate investments

### Data Accuracy
- Confidence scores indicate match reliability
- Cross-reference multiple data points
- Verify critical information independently
- Data freshness varies by source

## Error Responses

### No Matches Found
```json
{
  "status": "success",
  "data": {
    "matches": [],
    "search_metadata": {
      "total_matches": 0,
      "message": "No records found matching the search criteria"
    }
  }
}
```

### Invalid Search Criteria
```json
{
  "status": "error",
  "error": {
    "code": "INVALID_SEARCH_CRITERIA",
    "message": "Insufficient search criteria provided",
    "details": {
      "minimum_required": "name + address OR phone OR email"
    }
  }
}
```

## Rate Limits

Skip trace endpoints have strict rate limits:
- Individual searches: 60/minute
- Bulk searches: 5/minute
- Daily limit varies by plan
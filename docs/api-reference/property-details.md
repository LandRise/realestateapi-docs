# Property Details API

The Property Details API provides comprehensive information about a specific property including ownership, tax history, mortgage data, and property characteristics.

## Endpoint

```
GET /properties/{property_id}
```

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `property_id` | string | Yes | Unique property identifier |

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `include` | array | Additional data to include (see below) |
| `format` | string | Response format (json, xml) |

### Available Includes

- `ownership` - Current and historical ownership
- `tax` - Tax assessment and history
- `mortgage` - Mortgage and lien information
- `sales` - Sales history
- `permits` - Building permits
- `schools` - Nearby schools
- `demographics` - Neighborhood demographics
- `comps` - Comparable properties
- `images` - Property images
- `boundaries` - Property boundaries

Example: `/properties/PROP123456?include=ownership,tax,sales`

## Response

```json
{
  "status": "success",
  "data": {
    "property_id": "PROP123456",
    "apn": "123-456-789",
    "address": {
      "street": "123 Main St",
      "unit": "",
      "city": "Austin",
      "state": "TX",
      "zip": "78701",
      "county": "Travis",
      "formatted": "123 Main St, Austin, TX 78701"
    },
    "coordinates": {
      "latitude": 30.2672,
      "longitude": -97.7431
    },
    "property_type": "single_family",
    "property_use": "residential",
    "characteristics": {
      "bedrooms": 3,
      "bathrooms": 2.5,
      "full_bathrooms": 2,
      "half_bathrooms": 1,
      "square_feet": 2200,
      "lot_size_acres": 0.25,
      "lot_size_sqft": 10890,
      "year_built": 2005,
      "effective_year_built": 2010,
      "stories": 2,
      "garage_spaces": 2,
      "garage_type": "attached",
      "pool": true,
      "pool_type": "in_ground",
      "construction_type": "wood_frame",
      "roof_type": "composition_shingle",
      "foundation_type": "slab",
      "heating": "central",
      "cooling": "central_air",
      "fireplace": true,
      "fireplace_count": 1
    },
    "ownership": {
      "current": {
        "owner_names": ["John Doe", "Jane Doe"],
        "owner_type": "individual",
        "ownership_type": "joint_tenancy",
        "purchase_date": "2020-06-15",
        "purchase_price": 300000,
        "deed_type": "warranty_deed",
        "vesting": "Joint Tenancy"
      },
      "mailing_address": {
        "street": "123 Main St",
        "city": "Austin",
        "state": "TX",
        "zip": "78701"
      },
      "occupancy": "owner_occupied"
    },
    "tax": {
      "assessed_value": 340000,
      "assessed_year": 2024,
      "tax_amount": 7500,
      "tax_year": 2024,
      "exemptions": ["homestead"],
      "assessment_history": [
        {
          "year": 2023,
          "land_value": 100000,
          "improvement_value": 230000,
          "total_value": 330000
        }
      ]
    },
    "sales_history": [
      {
        "sale_date": "2020-06-15",
        "sale_price": 300000,
        "price_per_sqft": 136.36,
        "seller_names": ["Bob Smith"],
        "buyer_names": ["John Doe", "Jane Doe"],
        "deed_type": "warranty_deed",
        "financing": "conventional",
        "sale_type": "arms_length"
      }
    ],
    "mortgage": {
      "current_mortgages": [
        {
          "lender_name": "Wells Fargo",
          "loan_amount": 240000,
          "loan_type": "conventional",
          "loan_date": "2020-06-15",
          "interest_rate": 3.5,
          "term_months": 360
        }
      ],
      "liens": []
    },
    "valuation": {
      "estimated_value": 355000,
      "value_range": {
        "low": 340000,
        "high": 370000
      },
      "confidence_score": 0.92,
      "last_updated": "2024-01-15",
      "rent_estimate": {
        "monthly_rent": 2500,
        "rent_range": {
          "low": 2300,
          "high": 2700
        }
      }
    },
    "listing": {
      "is_listed": false,
      "last_list_date": "2020-04-01",
      "last_list_price": 310000,
      "days_on_market": 45
    },
    "schools": {
      "elementary": {
        "name": "Austin Elementary",
        "rating": 8,
        "distance_miles": 0.5
      },
      "middle": {
        "name": "Austin Middle School",
        "rating": 7,
        "distance_miles": 1.2
      },
      "high": {
        "name": "Austin High School",
        "rating": 9,
        "distance_miles": 2.1
      }
    },
    "demographics": {
      "median_income": 75000,
      "median_age": 35,
      "population": 25000,
      "growth_rate": 0.03
    }
  }
}
```

## Example Requests

### Basic Property Details

```bash
curl -X GET "https://api.realestateapi.com/v1/properties/PROP123456" \
  -H "X-API-Key: YOUR_API_KEY"
```

### Property with Specific Includes

```bash
curl -X GET "https://api.realestateapi.com/v1/properties/PROP123456?include=ownership,tax,sales,comps" \
  -H "X-API-Key: YOUR_API_KEY"
```

### Alternative Identifiers

You can also retrieve property details using:

#### By Address
```
GET /properties/by-address?address=123+Main+St&city=Austin&state=TX&zip=78701
```

#### By APN (Assessor's Parcel Number)
```
GET /properties/by-apn?apn=123-456-789&county=Travis&state=TX
```

#### By Coordinates
```
GET /properties/by-coordinates?latitude=30.2672&longitude=-97.7431
```

## Error Responses

```json
{
  "status": "error",
  "error": {
    "code": "PROPERTY_NOT_FOUND",
    "message": "No property found with the specified identifier",
    "details": {
      "property_id": "INVALID123"
    }
  }
}
```

## Data Freshness

- **Real-time data**: MLS listings, market status
- **Daily updates**: Tax records, ownership changes
- **Weekly updates**: Property characteristics, permits
- **Monthly updates**: Demographics, school ratings

## Rate Limits

Property detail requests are subject to the following limits:
- Standard: 100 requests/minute
- Premium: 500 requests/minute
- Enterprise: Custom limits
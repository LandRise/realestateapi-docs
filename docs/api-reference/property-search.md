# Property Search API

The Property Search API allows you to search for properties using various criteria including location, price, property type, and more.

## Endpoint

```
POST /properties/search
```

## Request Body

```json
{
  "location": {
    "city": "Austin",
    "state": "TX",
    "zip": "78701",
    "coordinates": {
      "latitude": 30.2672,
      "longitude": -97.7431
    },
    "radius_miles": 10
  },
  "filters": {
    "price": {
      "min": 200000,
      "max": 500000
    },
    "property_type": ["single_family", "condo"],
    "bedrooms": {
      "min": 2,
      "max": 4
    },
    "bathrooms": {
      "min": 1.5
    },
    "year_built": {
      "min": 1990
    },
    "square_feet": {
      "min": 1000,
      "max": 3000
    },
    "lot_size_acres": {
      "min": 0.1
    },
    "features": ["pool", "garage", "basement"]
  },
  "sort": {
    "field": "price",
    "order": "asc"
  },
  "pagination": {
    "limit": 50,
    "cursor": null
  }
}
```

## Parameters

### Location Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `city` | string | City name |
| `state` | string | Two-letter state code |
| `zip` | string | ZIP code |
| `coordinates` | object | Latitude and longitude |
| `radius_miles` | number | Search radius in miles |

### Filter Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `price` | object | Min/max price range |
| `property_type` | array | Property types to include |
| `bedrooms` | object | Min/max bedroom count |
| `bathrooms` | object | Min/max bathroom count |
| `year_built` | object | Min/max year built |
| `square_feet` | object | Min/max square footage |
| `lot_size_acres` | object | Min/max lot size |
| `features` | array | Required property features |

### Property Types

- `single_family`
- `condo`
- `townhouse`
- `multi_family`
- `land`
- `commercial`
- `mobile_home`

## Response

```json
{
  "status": "success",
  "data": {
    "properties": [
      {
        "property_id": "PROP123456",
        "address": {
          "street": "123 Main St",
          "city": "Austin",
          "state": "TX",
          "zip": "78701",
          "formatted": "123 Main St, Austin, TX 78701"
        },
        "coordinates": {
          "latitude": 30.2672,
          "longitude": -97.7431
        },
        "price": 350000,
        "property_type": "single_family",
        "details": {
          "bedrooms": 3,
          "bathrooms": 2.5,
          "square_feet": 2200,
          "lot_size_acres": 0.25,
          "year_built": 2005,
          "stories": 2
        },
        "features": ["pool", "garage", "hardwood_floors"],
        "listing": {
          "status": "active",
          "days_on_market": 15,
          "list_date": "2024-01-01",
          "mls_number": "MLS123456"
        },
        "valuation": {
          "estimated_value": 355000,
          "confidence": 0.92,
          "last_sale_price": 300000,
          "last_sale_date": "2020-06-15"
        },
        "images": [
          {
            "url": "https://images.realestateapi.com/prop123456_1.jpg",
            "type": "exterior",
            "caption": "Front view"
          }
        ]
      }
    ],
    "pagination": {
      "next_cursor": "eyJpZCI6MTczfQ",
      "has_more": true,
      "total_results": 245
    }
  }
}
```

## Example Requests

### Basic Search by City

```bash
curl -X POST "https://api.realestateapi.com/v1/properties/search" \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "location": {
      "city": "Austin",
      "state": "TX"
    }
  }'
```

### Advanced Search with Filters

```bash
curl -X POST "https://api.realestateapi.com/v1/properties/search" \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "location": {
      "zip": "78701",
      "radius_miles": 5
    },
    "filters": {
      "price": {
        "min": 300000,
        "max": 500000
      },
      "property_type": ["single_family"],
      "bedrooms": {
        "min": 3
      },
      "features": ["pool", "garage"]
    },
    "sort": {
      "field": "price",
      "order": "asc"
    }
  }'
```

### Polygon Search

```bash
curl -X POST "https://api.realestateapi.com/v1/properties/search/polygon" \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "polygon": [
      {"latitude": 30.2672, "longitude": -97.7431},
      {"latitude": 30.2700, "longitude": -97.7400},
      {"latitude": 30.2650, "longitude": -97.7380},
      {"latitude": 30.2640, "longitude": -97.7420}
    ],
    "filters": {
      "property_type": ["single_family", "condo"]
    }
  }'
```

## Bulk Search

For searching multiple properties at once (up to 1,000):

```
POST /properties/search/bulk
```

Request body should contain an array of property identifiers:

```json
{
  "properties": [
    {"address": "123 Main St, Austin, TX 78701"},
    {"apn": "123-456-789"},
    {"property_id": "PROP123456"}
  ]
}
```
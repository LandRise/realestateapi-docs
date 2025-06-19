# MLS Listings API

The MLS Listings API provides access to active real estate listings from Multiple Listing Services across the United States.

## Endpoints

### Search MLS Listings
```
POST /mls/search
```

### Get MLS Listing Details
```
GET /mls/listings/{mls_number}
```

### Get Listing Agent Information
```
GET /mls/listings/{mls_number}/agent
```

## MLS Search

### Request Body

```json
{
  "location": {
    "city": "Austin",
    "state": "TX",
    "zip": "78701",
    "mls_area": "1A",
    "subdivision": "Travis Heights"
  },
  "filters": {
    "status": ["active", "pending"],
    "price": {
      "min": 300000,
      "max": 600000
    },
    "list_date": {
      "start": "2024-01-01",
      "end": "2024-01-31"
    },
    "property_type": ["single_family", "condo"],
    "bedrooms": {
      "min": 3
    },
    "bathrooms": {
      "min": 2
    },
    "square_feet": {
      "min": 1500
    },
    "days_on_market": {
      "max": 30
    },
    "new_construction": false,
    "pool": true,
    "waterfront": false,
    "hoa_fee": {
      "max": 200
    }
  },
  "sort": {
    "field": "list_date",
    "order": "desc"
  },
  "pagination": {
    "limit": 50,
    "cursor": null
  }
}
```

### Parameters

#### Listing Status Values
- `active` - Currently for sale
- `pending` - Under contract
- `coming_soon` - Pre-market listing
- `contingent` - Contingent offer
- `withdrawn` - Temporarily off market
- `expired` - Listing expired
- `sold` - Recently sold

### Response

```json
{
  "status": "success",
  "data": {
    "listings": [
      {
        "mls_number": "MLS123456",
        "list_date": "2024-01-15",
        "status": "active",
        "days_on_market": 5,
        "price": {
          "list_price": 450000,
          "original_price": 460000,
          "price_per_sqft": 204.55,
          "price_change_date": "2024-01-18",
          "price_changes": [
            {
              "date": "2024-01-18",
              "old_price": 460000,
              "new_price": 450000,
              "change_percent": -2.17
            }
          ]
        },
        "address": {
          "street": "456 Oak St",
          "city": "Austin",
          "state": "TX",
          "zip": "78704",
          "county": "Travis",
          "subdivision": "Travis Heights",
          "display_address": true
        },
        "property": {
          "type": "single_family",
          "style": "contemporary",
          "bedrooms": 4,
          "bathrooms": 3,
          "half_bathrooms": 1,
          "square_feet": 2200,
          "lot_size_acres": 0.25,
          "year_built": 2019,
          "stories": 2,
          "garage_spaces": 2,
          "construction": "frame",
          "roof": "composition",
          "foundation": "slab"
        },
        "features": {
          "interior": [
            "hardwood_floors",
            "granite_counters",
            "stainless_appliances",
            "walk_in_closet",
            "fireplace"
          ],
          "exterior": [
            "pool",
            "sprinkler_system",
            "covered_patio",
            "privacy_fence"
          ],
          "amenities": [
            "energy_efficient",
            "smart_home",
            "security_system"
          ]
        },
        "listing_details": {
          "description": "Beautiful contemporary home in Travis Heights...",
          "virtual_tour_url": "https://tours.realestateapi.com/MLS123456",
          "showing_instructions": "Call listing agent for appointment",
          "possession": "At closing",
          "exclusions": "Refrigerator in garage"
        },
        "financial": {
          "taxes": {
            "annual_amount": 8500,
            "year": 2023
          },
          "hoa": {
            "fee": 150,
            "frequency": "monthly",
            "amenities": ["community_pool", "playground"]
          },
          "utilities_included": []
        },
        "agent": {
          "listing_agent": {
            "name": "Jane Smith",
            "license": "TX123456",
            "phone": "512-555-0123",
            "email": "jane@realty.com",
            "office": "Austin Realty Group"
          },
          "co_listing_agent": null
        },
        "images": [
          {
            "url": "https://images.realestateapi.com/mls/MLS123456_1.jpg",
            "type": "primary",
            "caption": "Front exterior",
            "order": 1
          }
        ],
        "open_houses": [
          {
            "date": "2024-01-20",
            "start_time": "14:00",
            "end_time": "16:00",
            "comments": "Refreshments provided"
          }
        ],
        "showing_stats": {
          "total_showings": 15,
          "last_showing_date": "2024-01-19"
        }
      }
    ],
    "pagination": {
      "next_cursor": "eyJpZCI6NDU2fQ",
      "has_more": true,
      "total_results": 125
    }
  }
}
```

## Get Listing Details

### Endpoint
```
GET /mls/listings/{mls_number}
```

### Example Request
```bash
curl -X GET "https://api.realestateapi.com/v1/mls/listings/MLS123456" \
  -H "X-API-Key: YOUR_API_KEY"
```

## Listing History

Get the history of status changes and price changes for a listing:

```
GET /mls/listings/{mls_number}/history
```

### Response
```json
{
  "status": "success",
  "data": {
    "mls_number": "MLS123456",
    "history": [
      {
        "date": "2024-01-15",
        "event": "listed",
        "status": "active",
        "price": 460000
      },
      {
        "date": "2024-01-18",
        "event": "price_change",
        "old_price": 460000,
        "new_price": 450000
      },
      {
        "date": "2024-01-22",
        "event": "status_change",
        "old_status": "active",
        "new_status": "pending"
      }
    ]
  }
}
```

## Saved Searches

Create and manage saved MLS searches:

### Create Saved Search
```
POST /mls/saved-searches
```

### Get Saved Searches
```
GET /mls/saved-searches
```

### Run Saved Search
```
GET /mls/saved-searches/{search_id}/results
```

## Real-time Updates

Subscribe to real-time updates for MLS listings:

### Webhook Subscription
```json
{
  "webhook_url": "https://your-app.com/webhooks/mls",
  "events": ["new_listing", "price_change", "status_change"],
  "filters": {
    "location": {
      "city": "Austin",
      "state": "TX"
    },
    "price": {
      "min": 300000,
      "max": 600000
    }
  }
}
```

## Rate Limits

MLS API endpoints have specific rate limits:
- Search: 60 requests/minute
- Details: 300 requests/minute
- Bulk operations: 10 requests/minute
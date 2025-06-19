# Advanced Property Search

Beyond basic property search, RealEstateAPI offers powerful advanced search capabilities including compound queries, specialized search modes, and sophisticated filtering options.

## Advanced Search Modes

### 1. IDs Only Mode

For credit optimization, retrieve only property IDs (up to 10,000) without full property data:

```
POST /properties/search
```

```json
{
  "location": {
    "city": "Austin",
    "state": "TX"
  },
  "filters": {
    "price": {
      "min": 300000,
      "max": 500000
    }
  },
  "output_mode": "ids_only",
  "pagination": {
    "limit": 10000
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "property_ids": [
      "PROP123456",
      "PROP123457",
      "PROP123458"
    ],
    "total_count": 1247,
    "credits_used": 1
  }
}
```

### 2. Count Mode

Get total number of matching properties without retrieving data:

```json
{
  "location": {
    "city": "Austin",
    "state": "TX"
  },
  "filters": {
    "property_type": ["single_family"],
    "bedrooms": {"min": 3}
  },
  "output_mode": "count"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "total_count": 3547,
    "credits_used": 0
  }
}
```

### 3. Summary Statistics Mode

Get aggregated statistics about matching properties:

```json
{
  "location": {
    "city": "Austin",
    "state": "TX"
  },
  "filters": {
    "property_type": ["single_family"]
  },
  "output_mode": "summary_stats"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "statistics": {
      "total_properties": 3547,
      "price": {
        "min": 150000,
        "max": 2500000,
        "median": 425000,
        "mean": 467000
      },
      "bedrooms": {
        "min": 1,
        "max": 8,
        "median": 3,
        "distribution": {
          "1": 45,
          "2": 234,
          "3": 1789,
          "4": 1234,
          "5+": 245
        }
      },
      "square_feet": {
        "min": 800,
        "max": 8500,
        "median": 2200,
        "mean": 2350
      }
    }
  }
}
```

## Compound Queries

Create complex Boolean logic with nested AND/OR clauses:

### Basic Compound Query

```json
{
  "location": {
    "city": "Austin",
    "state": "TX"
  },
  "compound_query": {
    "operator": "AND",
    "conditions": [
      {
        "field": "price",
        "operator": "between",
        "value": [300000, 600000]
      },
      {
        "operator": "OR",
        "conditions": [
          {
            "field": "bedrooms",
            "operator": "gte",
            "value": 4
          },
          {
            "field": "bathrooms",
            "operator": "gte",
            "value": 3
          }
        ]
      }
    ]
  }
}
```

### Advanced Compound Query

```json
{
  "compound_query": {
    "operator": "AND",
    "conditions": [
      {
        "field": "property_type",
        "operator": "in",
        "value": ["single_family", "townhouse"]
      },
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {"field": "bedrooms", "operator": "gte", "value": 4},
              {"field": "price", "operator": "lte", "value": 500000}
            ]
          },
          {
            "operator": "AND",
            "conditions": [
              {"field": "bedrooms", "operator": "eq", "value": 3},
              {"field": "price", "operator": "lte", "value": 400000},
              {"field": "square_feet", "operator": "gte", "value": 2000}
            ]
          }
        ]
      }
    ]
  }
}
```

## Specialized Search Filters

### Ownership-Based Searches

#### Absentee Owner Search
```json
{
  "filters": {
    "owner_occupied": false,
    "mailing_address_different": true
  }
}
```

#### Corporate Ownership
```json
{
  "filters": {
    "owner_type": ["corporation", "llc", "trust"]
  }
}
```

#### Out-of-State Owners
```json
{
  "filters": {
    "owner_state_different": true
  }
}
```

### Distressed Property Searches

#### Pre-Foreclosure Properties
```json
{
  "filters": {
    "foreclosure_status": "pre_foreclosure",
    "auction_date": {
      "start": "2024-01-01",
      "end": "2024-12-31"
    }
  }
}
```

#### REO Properties
```json
{
  "filters": {
    "foreclosure_status": "reo",
    "lender_owned": true
  }
}
```

#### Tax Lien Properties
```json
{
  "filters": {
    "tax_liens": {
      "exists": true,
      "amount": {
        "min": 5000
      }
    }
  }
}
```

### Equity-Based Searches

#### High Equity Properties
```json
{
  "filters": {
    "equity_percentage": {
      "min": 0.5
    },
    "estimated_equity": {
      "min": 100000
    }
  }
}
```

#### Low Equity/Underwater Properties
```json
{
  "filters": {
    "equity_percentage": {
      "max": 0.1
    }
  }
}
```

### Investment Property Searches

#### Cash Flow Properties
```json
{
  "filters": {
    "rental_estimate": {
      "exists": true
    },
    "cap_rate": {
      "min": 0.08
    },
    "cash_flow": {
      "min": 500
    }
  }
}
```

#### Flipped Properties
```json
{
  "filters": {
    "flipped_indicator": true,
    "time_between_sales": {
      "max": 365
    },
    "profit_margin": {
      "min": 0.15
    }
  }
}
```

### Financing-Based Searches

#### Assumable Mortgages
```json
{
  "filters": {
    "assumable_mortgage": true,
    "interest_rate": {
      "max": 0.04
    }
  }
}
```

#### Cash Buyers
```json
{
  "filters": {
    "last_sale_financing": "cash",
    "no_mortgage": true
  }
}
```

#### Private Lenders
```json
{
  "filters": {
    "lender_type": ["private", "hard_money"],
    "conventional_financing": false
  }
}
```

## Geographic Search Options

### Multi-Polygon Search

Search across multiple non-contiguous areas:

```json
{
  "multi_polygon_search": [
    {
      "name": "Downtown Austin",
      "polygon": [
        {"latitude": 30.2672, "longitude": -97.7431},
        {"latitude": 30.2700, "longitude": -97.7400},
        {"latitude": 30.2650, "longitude": -97.7380}
      ]
    },
    {
      "name": "East Austin",
      "polygon": [
        {"latitude": 30.2500, "longitude": -97.7200},
        {"latitude": 30.2550, "longitude": -97.7150},
        {"latitude": 30.2480, "longitude": -97.7100}
      ]
    }
  ],
  "filters": {
    "property_type": ["single_family"]
  }
}
```

### Radius Search with Exclusions

```json
{
  "location": {
    "coordinates": {
      "latitude": 30.2672,
      "longitude": -97.7431
    },
    "radius_miles": 10
  },
  "exclude_areas": [
    {
      "polygon": [
        {"latitude": 30.2600, "longitude": -97.7500},
        {"latitude": 30.2650, "longitude": -97.7450},
        {"latitude": 30.2580, "longitude": -97.7420}
      ]
    }
  ]
}
```

### School District Search

```json
{
  "filters": {
    "school_district": "Austin ISD",
    "elementary_school_rating": {
      "min": 8
    },
    "high_school_rating": {
      "min": 7
    }
  }
}
```

## Property Characteristics Searches

### Building-Specific Searches

#### Construction Type
```json
{
  "filters": {
    "construction_type": ["wood_frame", "brick", "stone"],
    "roof_material": ["tile", "slate"],
    "foundation_type": ["basement", "crawl_space"]
  }
}
```

#### Age and Condition
```json
{
  "filters": {
    "year_built": {
      "min": 2000,
      "max": 2020
    },
    "effective_year_built": {
      "min": 2015
    },
    "condition": ["excellent", "good"]
  }
}
```

### Amenity Searches

#### Luxury Features
```json
{
  "filters": {
    "features": {
      "all_of": ["pool", "spa", "wine_cellar"],
      "any_of": ["elevator", "smart_home", "solar_panels"]
    }
  }
}
```

#### Utilities and Systems
```json
{
  "filters": {
    "heating_type": ["central", "radiant"],
    "cooling_type": ["central_air"],
    "water_source": ["public"],
    "sewage_system": ["public_sewer"]
  }
}
```

## Advanced Sorting Options

### Multi-Field Sorting

```json
{
  "sort": [
    {
      "field": "equity_percentage",
      "order": "desc"
    },
    {
      "field": "days_on_market",
      "order": "asc"
    },
    {
      "field": "price",
      "order": "asc"
    }
  ]
}
```

### Custom Scoring

```json
{
  "custom_scoring": {
    "weights": {
      "price_score": 0.3,
      "location_score": 0.25,
      "condition_score": 0.2,
      "equity_score": 0.15,
      "rental_yield_score": 0.1
    }
  },
  "sort": {
    "field": "custom_score",
    "order": "desc"
  }
}
```

## Exclude Fields for Performance

Exclude heavy fields when not needed:

```json
{
  "filters": {
    "city": "Austin",
    "state": "TX"
  },
  "exclude_fields": [
    "sales_history",
    "mortgage_history",
    "detailed_demographics",
    "property_photos",
    "comparable_properties"
  ]
}
```

## Response Processing

### Field Selection

Return only specific fields:

```json
{
  "filters": {
    "city": "Austin",
    "state": "TX"
  },
  "include_fields": [
    "property_id",
    "address",
    "price",
    "bedrooms",
    "bathrooms",
    "square_feet",
    "estimated_value"
  ]
}
```

### Data Obfuscation

Protect sensitive data in client-facing applications:

```json
{
  "filters": {
    "city": "Austin",
    "state": "TX"
  },
  "obfuscation": {
    "owner_names": true,
    "exact_address": true,
    "phone_numbers": true,
    "email_addresses": true
  }
}
```

## Performance Optimization

### Pagination Strategies

#### Cursor-Based Pagination
```json
{
  "pagination": {
    "cursor": "eyJpZCI6MTIzNDU2fQ==",
    "limit": 100
  }
}
```

#### Offset-Based Pagination
```json
{
  "pagination": {
    "offset": 1000,
    "limit": 100
  }
}
```

### Caching

```json
{
  "cache_options": {
    "ttl_seconds": 3600,
    "cache_key": "austin_sf_homes_500k"
  }
}
```

## Best Practices

1. **Use Count Mode First**: Check result size before full queries
2. **Leverage IDs Only**: For large datasets, get IDs first
3. **Optimize Compound Queries**: Structure for database efficiency
4. **Exclude Unused Fields**: Improve performance
5. **Use Appropriate Pagination**: Cursor for large datasets
6. **Cache Common Queries**: Store frequent search results
7. **Progressive Filtering**: Start broad, then narrow down
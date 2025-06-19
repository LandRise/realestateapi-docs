# Valuations API (AVM)

The Valuations API provides automated property valuations using our Lender Grade AVM (Automated Valuation Model) for accurate property value estimates.

## Endpoints

### Get Property Valuation
```
POST /valuations/avm
```

### Get Comparable Properties
```
POST /valuations/comps
```

### Get Rental Estimate
```
POST /valuations/rental-estimate
```

## Property Valuation (AVM)

### Request Body

```json
{
  "property": {
    "address": "123 Main St, Austin, TX 78701",
    "property_id": "PROP123456",
    "apn": "123-456-789"
  },
  "valuation_options": {
    "include_confidence_score": true,
    "include_value_range": true,
    "include_comparables": true,
    "include_market_trends": true,
    "adjustment_date": "2024-01-15"
  }
}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `address` | string | Yes* | Property address |
| `property_id` | string | Yes* | RealEstateAPI property ID |
| `apn` | string | Yes* | Assessor's Parcel Number |
| `adjustment_date` | string | No | Valuation as of date |

*One property identifier is required

### Response

```json
{
  "status": "success",
  "data": {
    "valuation": {
      "estimated_value": 525000,
      "confidence_score": 0.92,
      "confidence_level": "high",
      "value_range": {
        "low": 498750,
        "high": 551250
      },
      "forecast_standard_deviation": 26250,
      "valuation_date": "2024-01-15",
      "model_version": "3.2.1"
    },
    "property_details": {
      "address": "123 Main St, Austin, TX 78701",
      "property_type": "single_family",
      "bedrooms": 3,
      "bathrooms": 2.5,
      "square_feet": 2200,
      "lot_size_acres": 0.25,
      "year_built": 2005
    },
    "market_analysis": {
      "market_trend": "appreciating",
      "annual_appreciation_rate": 0.045,
      "months_of_inventory": 2.3,
      "average_dom": 21,
      "list_to_sale_ratio": 0.98
    },
    "comparables": [
      {
        "address": "456 Oak St, Austin, TX 78701",
        "distance_miles": 0.3,
        "sale_date": "2023-12-15",
        "sale_price": 515000,
        "price_per_sqft": 234,
        "similarity_score": 0.88,
        "adjustments": {
          "location": 5000,
          "size": -3000,
          "condition": 0,
          "time": 2000,
          "total_adjustment": 4000,
          "adjusted_price": 519000
        },
        "property_details": {
          "bedrooms": 3,
          "bathrooms": 2,
          "square_feet": 2100,
          "year_built": 2007
        }
      }
    ],
    "value_indicators": {
      "last_sale_price": 450000,
      "last_sale_date": "2021-03-15",
      "tax_assessed_value": 480000,
      "tax_assessment_year": 2023,
      "price_per_sqft": 238.64,
      "neighborhood_median_price": 510000
    },
    "risk_factors": {
      "market_volatility": "low",
      "property_condition": "unknown",
      "natural_hazards": ["flood_zone_x"],
      "economic_indicators": "stable"
    }
  }
}
```

## Comparable Properties Analysis

### Endpoint
```
POST /valuations/comps
```

### Request Body
```json
{
  "subject_property": {
    "address": "123 Main St, Austin, TX 78701"
  },
  "comp_criteria": {
    "radius_miles": 1.0,
    "property_type_match": true,
    "min_similarity_score": 0.7,
    "max_comps": 10,
    "sale_recency_days": 180,
    "adjustments": {
      "location": true,
      "size": true,
      "age": true,
      "condition": true,
      "amenities": true
    }
  }
}
```

### Response
```json
{
  "status": "success",
  "data": {
    "subject_property": {
      "address": "123 Main St, Austin, TX 78701",
      "estimated_value": 525000
    },
    "comparables": [
      {
        "comp_id": "COMP123",
        "address": "456 Oak St, Austin, TX 78701",
        "sale_date": "2023-12-15",
        "sale_price": 515000,
        "days_on_market": 18,
        "similarity_score": 0.88,
        "distance_miles": 0.3,
        "adjustments": {
          "gross_adjustment": 15000,
          "net_adjustment": 4000,
          "adjusted_sale_price": 519000
        },
        "adjustment_details": [
          {
            "factor": "square_feet",
            "subject_value": 2200,
            "comp_value": 2100,
            "adjustment": -3000
          },
          {
            "factor": "location",
            "adjustment": 5000,
            "reason": "Superior school district"
          }
        ]
      }
    ],
    "statistical_analysis": {
      "adjusted_price_mean": 521000,
      "adjusted_price_median": 519000,
      "standard_deviation": 12000,
      "confidence_interval": {
        "low": 509000,
        "high": 533000
      }
    }
  }
}
```

## Rental Estimate

### Endpoint
```
POST /valuations/rental-estimate
```

### Request Body
```json
{
  "property": {
    "address": "123 Main St, Austin, TX 78701"
  },
  "rental_options": {
    "include_comps": true,
    "include_market_analysis": true,
    "lease_term_months": 12,
    "furnished": false
  }
}
```

### Response
```json
{
  "status": "success",
  "data": {
    "rental_estimate": {
      "monthly_rent": 2500,
      "rent_range": {
        "low": 2300,
        "high": 2700
      },
      "confidence_score": 0.89,
      "price_per_sqft": 1.14,
      "annual_gross_rent": 30000
    },
    "rental_comps": [
      {
        "address": "789 Pine St, Austin, TX 78701",
        "monthly_rent": 2450,
        "lease_date": "2023-11-01",
        "bedrooms": 3,
        "bathrooms": 2,
        "square_feet": 2150,
        "similarity_score": 0.85
      }
    ],
    "market_metrics": {
      "neighborhood_avg_rent": 2475,
      "vacancy_rate": 0.05,
      "annual_rent_growth": 0.03,
      "avg_days_to_lease": 14
    },
    "investment_metrics": {
      "gross_rent_multiplier": 17.5,
      "cap_rate": 0.048,
      "cash_on_cash_return": 0.062,
      "monthly_cash_flow": 350
    }
  }
}
```

## Bulk Valuations

Process multiple property valuations (up to 100):

### Endpoint
```
POST /valuations/bulk
```

### Request Body
```json
{
  "properties": [
    {
      "id": "prop1",
      "address": "123 Main St, Austin, TX 78701"
    },
    {
      "id": "prop2",
      "address": "456 Oak Ave, Austin, TX 78701"
    }
  ],
  "valuation_options": {
    "include_confidence_score": true
  }
}
```

## Valuation Models

### Model Types
- **Lender Grade AVM**: High-accuracy model for lending decisions
- **Investor Model**: Optimized for investment analysis
- **Quick Estimate**: Fast, lower-accuracy estimates

### Confidence Levels
- **High** (0.90-1.00): Excellent data quality and model fit
- **Good** (0.80-0.89): Strong confidence in estimate
- **Fair** (0.70-0.79): Moderate confidence
- **Low** (<0.70): Limited data or unique property

## Best Practices

1. **Use multiple identifiers** when available for better matches
2. **Check confidence scores** before making decisions
3. **Review comparables** to understand valuation basis
4. **Consider market trends** in volatile markets
5. **Update valuations** regularly for active deals
6. **Use appropriate model** for your use case

## Limitations

- Rural properties may have lower confidence scores
- Unique properties require manual review
- Recent renovations may not be reflected
- Valuations are estimates, not appraisals
- Not suitable for lending without additional verification
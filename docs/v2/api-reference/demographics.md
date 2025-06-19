# Demographics API

The Demographics API provides detailed demographic and statistical information about neighborhoods, ZIP codes, and custom geographic areas.

## Endpoints

### Get Demographics by Location
```
GET /demographics/location
```

### Get Demographics by Radius
```
POST /demographics/radius
```

### Get Demographics by Polygon
```
POST /demographics/polygon
```

## Demographics by Location

### Request Parameters

```
GET /demographics/location?zip=78701&include=income,education,housing
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `zip` | string | Yes* | ZIP code |
| `city` | string | Yes* | City name |
| `state` | string | Yes* | State code |
| `county` | string | Yes* | County name |
| `include` | array | No | Specific data categories |

*One location parameter is required

### Available Data Categories

- `population` - Population statistics
- `income` - Income distribution
- `education` - Education levels
- `employment` - Employment statistics
- `housing` - Housing characteristics
- `age` - Age distribution
- `family` - Household composition
- `commute` - Commute patterns

### Response

```json
{
  "status": "success",
  "data": {
    "location": {
      "zip": "78701",
      "city": "Austin",
      "state": "TX",
      "county": "Travis"
    },
    "population": {
      "total": 25847,
      "density_per_sq_mile": 12453,
      "growth_rate_annual": 0.032,
      "growth_rate_5_year": 0.165,
      "households": 11234,
      "avg_household_size": 2.3
    },
    "income": {
      "median_household": 75234,
      "mean_household": 98456,
      "per_capita": 45678,
      "distribution": {
        "under_25k": 0.15,
        "25k_50k": 0.20,
        "50k_75k": 0.25,
        "75k_100k": 0.20,
        "100k_150k": 0.12,
        "150k_plus": 0.08
      },
      "poverty_rate": 0.089
    },
    "education": {
      "high_school_or_higher": 0.92,
      "bachelors_or_higher": 0.58,
      "graduate_degree": 0.24,
      "distribution": {
        "less_than_high_school": 0.08,
        "high_school": 0.22,
        "some_college": 0.28,
        "bachelors": 0.34,
        "graduate": 0.24
      }
    },
    "employment": {
      "unemployment_rate": 0.035,
      "labor_force_participation": 0.72,
      "white_collar": 0.68,
      "blue_collar": 0.22,
      "service": 0.10,
      "top_industries": [
        {
          "name": "Technology",
          "percentage": 0.25
        },
        {
          "name": "Healthcare",
          "percentage": 0.18
        },
        {
          "name": "Education",
          "percentage": 0.15
        }
      ]
    },
    "housing": {
      "median_home_value": 425000,
      "median_rent": 1850,
      "owner_occupied": 0.45,
      "renter_occupied": 0.55,
      "vacancy_rate": 0.08,
      "median_year_built": 1995,
      "housing_types": {
        "single_family": 0.35,
        "condo": 0.25,
        "townhouse": 0.15,
        "multi_family": 0.20,
        "mobile_home": 0.05
      }
    },
    "age": {
      "median_age": 33.5,
      "distribution": {
        "under_18": 0.15,
        "18_24": 0.12,
        "25_34": 0.28,
        "35_44": 0.20,
        "45_54": 0.12,
        "55_64": 0.08,
        "65_plus": 0.05
      }
    },
    "family": {
      "married_couples": 0.42,
      "with_children": 0.28,
      "single_parent": 0.08,
      "avg_family_size": 3.1
    },
    "commute": {
      "avg_time_minutes": 24.5,
      "methods": {
        "drive_alone": 0.68,
        "carpool": 0.08,
        "public_transit": 0.12,
        "walk": 0.06,
        "bike": 0.04,
        "work_from_home": 0.18
      }
    },
    "data_year": 2023,
    "last_updated": "2024-01-15"
  }
}
```

## Demographics by Radius

Get demographics for a circular area:

### Request Body

```json
{
  "center": {
    "latitude": 30.2672,
    "longitude": -97.7431
  },
  "radius_miles": 3,
  "include": ["population", "income", "housing"],
  "aggregation": "weighted"
}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `center` | object | Yes | Center coordinates |
| `radius_miles` | number | Yes | Radius in miles (max: 50) |
| `include` | array | No | Data categories to include |
| `aggregation` | string | No | How to aggregate data |

### Aggregation Methods

- `weighted` - Population-weighted average (default)
- `mean` - Simple average
- `sum` - Total for count metrics

## Demographics by Polygon

Get demographics for a custom area:

### Request Body

```json
{
  "polygon": [
    {"latitude": 30.2672, "longitude": -97.7431},
    {"latitude": 30.2700, "longitude": -97.7400},
    {"latitude": 30.2650, "longitude": -97.7380},
    {"latitude": 30.2640, "longitude": -97.7420}
  ],
  "include": ["population", "income"],
  "resolution": "block_group"
}
```

### Resolution Options

- `block` - Census block (highest detail)
- `block_group` - Census block group
- `tract` - Census tract
- `zip` - ZIP code level

## Comparative Demographics

Compare demographics across multiple areas:

### Endpoint
```
POST /demographics/compare
```

### Request Body

```json
{
  "locations": [
    {"zip": "78701"},
    {"zip": "78702"},
    {"city": "Austin", "state": "TX"}
  ],
  "metrics": [
    "population.total",
    "income.median_household",
    "housing.median_home_value",
    "education.bachelors_or_higher"
  ]
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "comparison": [
      {
        "location": {"zip": "78701"},
        "metrics": {
          "population.total": 25847,
          "income.median_household": 75234,
          "housing.median_home_value": 425000,
          "education.bachelors_or_higher": 0.58
        }
      },
      {
        "location": {"zip": "78702"},
        "metrics": {
          "population.total": 31245,
          "income.median_household": 68500,
          "housing.median_home_value": 385000,
          "education.bachelors_or_higher": 0.52
        }
      }
    ],
    "averages": {
      "population.total": 28546,
      "income.median_household": 71867,
      "housing.median_home_value": 405000,
      "education.bachelors_or_higher": 0.55
    }
  }
}
```

## Time Series Demographics

Get historical demographic trends:

### Endpoint
```
GET /demographics/trends
```

### Parameters

```
GET /demographics/trends?zip=78701&metrics=population.total,income.median_household&years=5
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `zip` | string | Yes | ZIP code |
| `metrics` | array | Yes | Metrics to track |
| `years` | integer | No | Years of history (default: 5) |

### Response

```json
{
  "status": "success",
  "data": {
    "location": {"zip": "78701"},
    "trends": {
      "population.total": [
        {"year": 2019, "value": 23456},
        {"year": 2020, "value": 24123},
        {"year": 2021, "value": 24890},
        {"year": 2022, "value": 25234},
        {"year": 2023, "value": 25847}
      ],
      "income.median_household": [
        {"year": 2019, "value": 65000},
        {"year": 2020, "value": 68000},
        {"year": 2021, "value": 70500},
        {"year": 2022, "value": 73000},
        {"year": 2023, "value": 75234}
      ]
    },
    "growth_rates": {
      "population.total": {
        "annual_avg": 0.025,
        "total": 0.102
      },
      "income.median_household": {
        "annual_avg": 0.037,
        "total": 0.157
      }
    }
  }
}
```

## School Districts

Get demographic data for school districts:

### Endpoint
```
GET /demographics/school-district
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `district_id` | string | Yes* | School district ID |
| `district_name` | string | Yes* | District name |
| `state` | string | Yes* | State code |

### Response Includes

- Student demographics
- Teacher statistics
- Performance metrics
- Funding information
- Enrollment trends

## Use Cases

### Real Estate Analysis
```javascript
async function analyzeNeighborhood(address) {
  // Get property details
  const property = await api.getProperty(address);
  
  // Get demographics for the area
  const demographics = await api.getDemographics({
    zip: property.address.zip,
    include: ['income', 'education', 'housing', 'age']
  });
  
  // Calculate affordability
  const medianIncome = demographics.income.median_household;
  const affordabilityRatio = property.price / medianIncome;
  
  return {
    property,
    demographics,
    analysis: {
      affordabilityRatio,
      collegeDegreeRate: demographics.education.bachelors_or_higher,
      medianAge: demographics.age.median_age,
      ownerOccupiedRate: demographics.housing.owner_occupied
    }
  };
}
```

### Market Research
```python
def compare_markets(zip_codes):
    # Get demographics for each ZIP
    demographics = []
    for zip_code in zip_codes:
        demo = api.get_demographics(zip=zip_code)
        demographics.append(demo)
    
    # Create comparison matrix
    comparison = pd.DataFrame({
        'ZIP': zip_codes,
        'Population': [d['population']['total'] for d in demographics],
        'Median Income': [d['income']['median_household'] for d in demographics],
        'Growth Rate': [d['population']['growth_rate_annual'] for d in demographics],
        'Home Value': [d['housing']['median_home_value'] for d in demographics]
    })
    
    # Rank markets
    comparison['Income Rank'] = comparison['Median Income'].rank(ascending=False)
    comparison['Growth Rank'] = comparison['Growth Rate'].rank(ascending=False)
    
    return comparison.sort_values('Income Rank')
```

## Data Sources & Updates

- **Source**: U.S. Census Bureau, American Community Survey
- **Update Frequency**: Annual
- **Coverage**: All U.S. ZIP codes, cities, counties
- **Historical Data**: Up to 10 years
- **Projections**: 5-year forecasts available

## Best Practices

1. **Cache demographic data** - Updates annually
2. **Use appropriate resolution** - Block level for precision, ZIP for performance
3. **Consider margins of error** - Smaller areas have higher uncertainty
4. **Combine with property data** - Create comprehensive market analysis
5. **Monitor trends** - Track changes over time
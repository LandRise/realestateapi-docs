# Mapping & Boundaries API

The Mapping & Boundaries API provides detailed geographic data including property boundaries, parcel information, and mapping coordinates for building comprehensive real estate mapping applications.

## Overview

The Mapping API enables:
- Property boundary visualization
- Parcel data retrieval
- GeoJSON boundary exports
- Multi-property mapping
- Custom map pin generation
- Geographic area analysis

## Endpoints

### Property Boundary API
```
GET /mapping/boundaries/property
POST /mapping/boundaries/bulk
```

### Mapping Pins API
```
POST /mapping/pins
GET /mapping/pins/{pin_id}
```

### Area Analysis API
```
POST /mapping/areas/analyze
```

## Property Boundary API

Get detailed property boundaries in GeoJSON format for mapping applications.

### Get Boundary by Address

```
GET /mapping/boundaries/property?address=123+Main+St+Austin+TX+78701
```

### Get Boundary by APN

```
GET /mapping/boundaries/property?apn=123-456-789&county=Travis&state=TX
```

### Get Boundary by Coordinates

```
GET /mapping/boundaries/property?latitude=30.2672&longitude=-97.7431
```

### Response

```json
{
  "status": "success",
  "data": {
    "property_id": "PROP123456",
    "apn": "123-456-789",
    "address": {
      "formatted": "123 Main St, Austin, TX 78701"
    },
    "boundary": {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [[
          [-97.7431, 30.2672],
          [-97.7425, 30.2672],
          [-97.7425, 30.2665],
          [-97.7431, 30.2665],
          [-97.7431, 30.2672]
        ]]
      },
      "properties": {
        "property_id": "PROP123456",
        "apn": "123-456-789",
        "area_sqft": 8712,
        "area_acres": 0.2,
        "perimeter_ft": 374.5
      }
    },
    "parcel_data": {
      "lot_size_sqft": 8712,
      "lot_size_acres": 0.2,
      "frontage_ft": 87.2,
      "depth_ft": 100,
      "irregular_lot": false,
      "corner_lot": true,
      "access_type": "public_road",
      "easements": [
        {
          "type": "utility",
          "width_ft": 10,
          "description": "Utility easement along rear property line"
        }
      ]
    },
    "zoning": {
      "zoning_code": "SF-3",
      "zoning_description": "Single Family Residential",
      "land_use": "residential",
      "density_units_per_acre": 8,
      "setbacks": {
        "front_ft": 25,
        "rear_ft": 15,
        "side_ft": 7.5
      }
    },
    "flood_zone": {
      "zone": "X",
      "description": "Area of minimal flood hazard",
      "panel_number": "48453C0381G",
      "effective_date": "2018-05-16"
    }
  }
}
```

## Bulk Boundary Retrieval

Get boundaries for multiple properties:

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
      "apn": "456-789-012",
      "county": "Travis",
      "state": "TX"
    },
    {
      "id": "prop3",
      "latitude": 30.2672,
      "longitude": -97.7431
    }
  ],
  "options": {
    "include_parcel_data": true,
    "include_zoning": true,
    "format": "geojson"
  }
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "boundaries": [
      {
        "id": "prop1",
        "property_id": "PROP123456",
        "boundary": {
          // GeoJSON Feature
        },
        "parcel_data": {
          // Parcel information
        }
      }
    ],
    "feature_collection": {
      "type": "FeatureCollection",
      "features": [
        // All boundaries as GeoJSON features
      ]
    },
    "summary": {
      "total_requested": 3,
      "successful": 3,
      "failed": 0
    }
  }
}
```

## Find Boundaries Within Polygon

Find all property boundaries within a custom polygon:

### Request Body

```json
{
  "polygon": [
    {"latitude": 30.2672, "longitude": -97.7431},
    {"latitude": 30.2700, "longitude": -97.7400},
    {"latitude": 30.2650, "longitude": -97.7380},
    {"latitude": 30.2640, "longitude": -97.7420}
  ],
  "options": {
    "include_properties": true,
    "max_results": 100,
    "property_types": ["residential", "commercial"]
  }
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "polygon_area_sqft": 2847653,
    "polygon_area_acres": 65.4,
    "boundaries": [
      {
        "property_id": "PROP123456",
        "apn": "123-456-789",
        "boundary": {
          // GeoJSON Feature
        },
        "property_summary": {
          "address": "123 Main St, Austin, TX 78701",
          "property_type": "single_family",
          "estimated_value": 425000
        }
      }
    ],
    "feature_collection": {
      "type": "FeatureCollection",
      "features": [
        // All boundaries as GeoJSON features
      ]
    },
    "statistics": {
      "total_properties": 47,
      "residential": 42,
      "commercial": 5,
      "total_land_area_acres": 58.3,
      "average_lot_size_sqft": 7234
    }
  }
}
```

## Mapping Pins API

Generate unlimited mapping pins for property visualization.

### Create Mapping Pins

```
POST /mapping/pins
```

### Request Body

```json
{
  "properties": [
    {
      "property_id": "PROP123456",
      "address": "123 Main St, Austin, TX 78701",
      "coordinates": {
        "latitude": 30.2672,
        "longitude": -97.7431
      },
      "pin_data": {
        "price": 425000,
        "bedrooms": 3,
        "bathrooms": 2,
        "status": "for_sale",
        "property_type": "single_family"
      }
    }
  ],
  "pin_options": {
    "cluster_distance": 50,
    "include_summary": true,
    "zoom_levels": [8, 10, 12, 15, 18]
  }
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "pin_collection_id": "pins_67890",
    "pins": [
      {
        "pin_id": "pin_123456",
        "property_id": "PROP123456",
        "coordinates": {
          "latitude": 30.2672,
          "longitude": -97.7431
        },
        "pin_data": {
          "price": 425000,
          "bedrooms": 3,
          "bathrooms": 2,
          "status": "for_sale",
          "property_type": "single_family"
        },
        "cluster_info": {
          "is_clustered": false,
          "cluster_id": null,
          "zoom_visibility": [12, 15, 18]
        }
      }
    ],
    "clusters": [
      {
        "cluster_id": "cluster_789",
        "center": {
          "latitude": 30.2650,
          "longitude": -97.7400
        },
        "property_count": 15,
        "zoom_levels": [8, 10],
        "summary": {
          "avg_price": 387000,
          "price_range": {
            "min": 275000,
            "max": 520000
          },
          "property_types": ["single_family", "condo"]
        }
      }
    ],
    "bounds": {
      "north": 30.2700,
      "south": 30.2640,
      "east": -97.7380,
      "west": -97.7431
    }
  }
}
```

## Area Analysis API

Analyze geographic areas for market insights:

### Request Body

```json
{
  "area": {
    "type": "polygon",
    "coordinates": [
      {"latitude": 30.2672, "longitude": -97.7431},
      {"latitude": 30.2700, "longitude": -97.7400},
      {"latitude": 30.2650, "longitude": -97.7380}
    ]
  },
  "analysis_options": {
    "include_demographics": true,
    "include_market_data": true,
    "include_zoning": true,
    "include_schools": true,
    "include_amenities": true
  }
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "area_summary": {
      "area_sqft": 2847653,
      "area_acres": 65.4,
      "center_point": {
        "latitude": 30.2674,
        "longitude": -97.7404
      }
    },
    "property_analysis": {
      "total_properties": 247,
      "property_types": {
        "single_family": 198,
        "condo": 32,
        "townhouse": 17
      },
      "price_analysis": {
        "median_price": 425000,
        "average_price": 467000,
        "price_per_sqft": {
          "median": 195,
          "average": 208
        },
        "price_distribution": {
          "under_300k": 15,
          "300k_500k": 165,
          "500k_750k": 52,
          "over_750k": 15
        }
      }
    },
    "demographics": {
      "population": 1247,
      "households": 523,
      "median_income": 78500,
      "education": {
        "bachelors_or_higher": 0.67
      }
    },
    "market_trends": {
      "price_trend_6_months": 0.034,
      "inventory_level": "low",
      "days_on_market_avg": 18,
      "sale_to_list_ratio": 0.98
    },
    "zoning_analysis": {
      "residential": 0.85,
      "commercial": 0.10,
      "mixed_use": 0.05,
      "future_development": [
        {
          "type": "mixed_use_development",
          "status": "approved",
          "estimated_completion": "2025-Q3"
        }
      ]
    },
    "amenities": {
      "schools": [
        {
          "name": "Austin Elementary",
          "type": "elementary",
          "rating": 9,
          "distance_miles": 0.3
        }
      ],
      "parks": [
        {
          "name": "Zilker Park",
          "type": "public",
          "distance_miles": 0.8
        }
      ],
      "transit": {
        "bus_stops": 3,
        "metro_stations": 0,
        "bike_lanes": true
      }
    }
  }
}
```

## Integration Examples

### Map Visualization

```javascript
class PropertyMap {
  async loadPropertyBoundaries(propertyIds) {
    const response = await api.post('/mapping/boundaries/bulk', {
      properties: propertyIds.map(id => ({ property_id: id })),
      options: {
        format: 'geojson',
        include_parcel_data: true
      }
    });
    
    // Add to map
    this.map.addLayer({
      id: 'property-boundaries',
      type: 'fill',
      source: {
        type: 'geojson',
        data: response.data.feature_collection
      },
      paint: {
        'fill-color': '#088',
        'fill-opacity': 0.2
      }
    });
  }
  
  async createPropertyPins(properties) {
    const pinData = await api.post('/mapping/pins', {
      properties: properties.map(p => ({
        property_id: p.id,
        coordinates: p.coordinates,
        pin_data: {
          price: p.price,
          status: p.status,
          property_type: p.type
        }
      })),
      pin_options: {
        cluster_distance: 50,
        include_summary: true
      }
    });
    
    // Add clustered pins to map
    this.addClusteredMarkers(pinData.data);
  }
}
```

### Area Analysis Tool

```python
class AreaAnalyzer:
    def analyze_investment_area(self, polygon_coords):
        analysis = api.analyze_area({
            'area': {
                'type': 'polygon',
                'coordinates': polygon_coords
            },
            'analysis_options': {
                'include_demographics': True,
                'include_market_data': True
            }
        })
        
        # Calculate investment metrics
        data = analysis['data']
        
        return {
            'market_score': self.calculate_market_score(data),
            'growth_potential': self.assess_growth_potential(data),
            'competition_level': self.assess_competition(data),
            'demographics_score': self.score_demographics(data['demographics'])
        }
    
    def calculate_market_score(self, data):
        property_data = data['property_analysis']
        market_data = data['market_trends']
        
        # Weighted scoring algorithm
        price_stability = 1 - abs(market_data['price_trend_6_months'])
        liquidity = 1 - (market_data['days_on_market_avg'] / 60)
        demand = market_data['sale_to_list_ratio']
        
        return (price_stability * 0.3 + liquidity * 0.4 + demand * 0.3) * 100
```

### Real Estate Mapping Dashboard

```javascript
class MapDashboard {
  constructor(mapContainer) {
    this.map = new mapboxgl.Map({
      container: mapContainer,
      style: 'mapbox://styles/mapbox/streets-v11'
    });
    
    this.initializeControls();
  }
  
  async loadMarketArea(polygon) {
    // Get area analysis
    const analysis = await api.analyzeArea({
      area: { type: 'polygon', coordinates: polygon },
      analysis_options: {
        include_demographics: true,
        include_market_data: true,
        include_amenities: true
      }
    });
    
    // Display analysis results
    this.displayAreaAnalysis(analysis.data);
    
    // Get all properties in area
    const boundaries = await api.findBoundariesInPolygon({
      polygon: polygon,
      options: { include_properties: true }
    });
    
    // Add property boundaries to map
    this.addPropertyBoundaries(boundaries.data.feature_collection);
    
    return {
      analysis: analysis.data,
      properties: boundaries.data.boundaries
    };
  }
  
  displayAreaAnalysis(data) {
    const summary = document.getElementById('area-summary');
    summary.innerHTML = `
      <h3>Area Analysis</h3>
      <p>Total Properties: ${data.property_analysis.total_properties}</p>
      <p>Median Price: $${data.property_analysis.price_analysis.median_price.toLocaleString()}</p>
      <p>Avg Days on Market: ${data.market_trends.days_on_market_avg}</p>
      <p>Population: ${data.demographics.population}</p>
      <p>Median Income: $${data.demographics.median_income.toLocaleString()}</p>
    `;
  }
}
```

## Best Practices

### Performance Optimization

1. **Batch Boundary Requests**: Use bulk endpoints for multiple properties
2. **Cache Boundary Data**: Property boundaries rarely change
3. **Use Appropriate Zoom Levels**: Show clusters at low zoom, details at high zoom
4. **Limit Pin Data**: Include only necessary information for pins
5. **Progressive Loading**: Load boundaries as users zoom in

### Mapping Considerations

1. **Coordinate Precision**: Use appropriate precision for zoom level
2. **Boundary Simplification**: Simplify complex boundaries for performance
3. **Visual Hierarchy**: Use different styles for different property types
4. **Interactive Features**: Enable click/hover for property details
5. **Mobile Optimization**: Ensure maps work well on mobile devices

### Data Management

1. **Update Frequency**: Property boundaries rarely change, cache aggressively
2. **Error Handling**: Handle missing boundary data gracefully
3. **Projection**: Ensure consistent coordinate reference systems
4. **Validation**: Validate polygon coordinates before API calls
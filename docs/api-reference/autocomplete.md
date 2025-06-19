# AutoComplete API

The AutoComplete API provides machine learning-powered address and location suggestions, similar to Google AutoComplete but specifically optimized for real estate applications. Free and unlimited for RealEstateAPI subscribers.

## Overview

AutoComplete API features:
- **Free unlimited usage** for subscribers
- Machine learning powered suggestions
- Real estate context awareness
- Multiple completion types
- Browser-friendly implementation
- Mobile-optimized responses

## Endpoints

### Full Address AutoComplete
```
GET /autocomplete/address
```

### City/State AutoComplete
```
GET /autocomplete/city-state
```

### County AutoComplete
```
GET /autocomplete/county
```

### Neighborhood AutoComplete
```
GET /autocomplete/neighborhood
```

### ZIP Code AutoComplete
```
GET /autocomplete/zip
```

### State AutoComplete
```
GET /autocomplete/state
```

### APN AutoComplete
```
GET /autocomplete/apn
```

## Full Address AutoComplete

The primary autocomplete endpoint for complete address suggestions.

### Request Parameters

```
GET /autocomplete/address?query=123+Main&limit=10&location_bias=Austin,TX
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Partial address input (minimum 3 characters) |
| `limit` | integer | No | Maximum suggestions (default: 10, max: 25) |
| `location_bias` | string | No | Geographic bias for suggestions |
| `bounds` | string | No | Geographic bounds (lat1,lng1,lat2,lng2) |
| `types` | string | No | Address types to include |
| `state` | string | No | Restrict to specific state |

### Response

```json
{
  "status": "success",
  "data": {
    "query": "123 Main",
    "suggestions": [
      {
        "place_id": "addr_123456",
        "description": "123 Main St, Austin, TX 78701",
        "structured_formatting": {
          "main_text": "123 Main St",
          "secondary_text": "Austin, TX 78701",
          "main_text_matched_substrings": [
            {
              "offset": 0,
              "length": 8
            }
          ]
        },
        "types": ["street_address", "establishment"],
        "distance_meters": 0,
        "confidence": 0.95,
        "components": {
          "street_number": "123",
          "route": "Main St",
          "locality": "Austin",
          "administrative_area_level_1": "TX",
          "postal_code": "78701",
          "country": "US"
        },
        "geometry": {
          "location": {
            "lat": 30.2672,
            "lng": -97.7431
          }
        },
        "property_context": {
          "has_property_data": true,
          "property_type": "single_family",
          "estimated_value": 425000
        }
      },
      {
        "place_id": "addr_123457",
        "description": "123 Main Ave, Austin, TX 78702",
        "structured_formatting": {
          "main_text": "123 Main Ave",
          "secondary_text": "Austin, TX 78702"
        },
        "types": ["street_address"],
        "distance_meters": 2300,
        "confidence": 0.88,
        "components": {
          "street_number": "123",
          "route": "Main Ave",
          "locality": "Austin",
          "administrative_area_level_1": "TX",
          "postal_code": "78702",
          "country": "US"
        },
        "geometry": {
          "location": {
            "lat": 30.2589,
            "lng": -97.7289
          }
        },
        "property_context": {
          "has_property_data": true,
          "property_type": "condo",
          "estimated_value": 385000
        }
      }
    ],
    "metadata": {
      "query_time_ms": 45,
      "suggestions_count": 2,
      "has_more": false
    }
  }
}
```

## City/State AutoComplete

### Request Parameters

```
GET /autocomplete/city-state?query=Aust&state=TX&limit=5
```

### Response

```json
{
  "status": "success",
  "data": {
    "query": "Aust",
    "suggestions": [
      {
        "place_id": "city_austin_tx",
        "description": "Austin, TX",
        "city": "Austin",
        "state": "TX",
        "state_code": "TX",
        "county": "Travis",
        "population": 978908,
        "area_sqmi": 320.8,
        "confidence": 0.98,
        "geometry": {
          "location": {
            "lat": 30.2672,
            "lng": -97.7431
          },
          "bounds": {
            "northeast": {"lat": 30.5168, "lng": -97.5684},
            "southwest": {"lat": 30.0986, "lng": -97.9383}
          }
        },
        "market_data": {
          "median_home_value": 525000,
          "market_trend": "rising",
          "total_properties": 325000
        }
      }
    ]
  }
}
```

## County AutoComplete

### Request Parameters

```
GET /autocomplete/county?query=Trav&state=TX
```

### Response

```json
{
  "status": "success",
  "data": {
    "suggestions": [
      {
        "place_id": "county_travis_tx",
        "description": "Travis County, TX",
        "county": "Travis",
        "state": "TX",
        "fips_code": "48453",
        "seat": "Austin",
        "population": 1290188,
        "area_sqmi": 1023.3,
        "confidence": 0.96,
        "geometry": {
          "location": {
            "lat": 30.3072,
            "lng": -97.7560
          }
        },
        "market_data": {
          "median_home_value": 485000,
          "total_properties": 475000,
          "major_cities": ["Austin", "Cedar Park", "Round Rock"]
        }
      }
    ]
  }
}
```

## Neighborhood AutoComplete

### Request Parameters

```
GET /autocomplete/neighborhood?query=East&city=Austin&state=TX
```

### Response

```json
{
  "status": "success",
  "data": {
    "suggestions": [
      {
        "place_id": "neighborhood_east_austin",
        "description": "East Austin, Austin, TX",
        "neighborhood": "East Austin",
        "city": "Austin",
        "state": "TX",
        "confidence": 0.92,
        "geometry": {
          "location": {
            "lat": 30.2584,
            "lng": -97.7089
          },
          "bounds": {
            "northeast": {"lat": 30.2901, "lng": -97.6874},
            "southwest": {"lat": 30.2267, "lng": -97.7304}
          }
        },
        "characteristics": {
          "type": "urban",
          "popularity": "trending",
          "walkability_score": 78,
          "median_income": 65000
        },
        "market_data": {
          "median_home_value": 425000,
          "price_trend_12m": 0.125,
          "total_properties": 15000
        }
      }
    ]
  }
}
```

## ZIP Code AutoComplete

### Request Parameters

```
GET /autocomplete/zip?query=787&state=TX
```

### Response

```json
{
  "status": "success",
  "data": {
    "suggestions": [
      {
        "place_id": "zip_78701",
        "description": "78701 - Downtown Austin, TX",
        "postal_code": "78701",
        "primary_city": "Austin",
        "state": "TX",
        "type": "standard",
        "confidence": 0.95,
        "geometry": {
          "location": {
            "lat": 30.2672,
            "lng": -97.7431
          }
        },
        "area_info": {
          "area_sqmi": 2.1,
          "population": 4200,
          "household_count": 2100,
          "businesses": 450
        },
        "market_data": {
          "median_home_value": 485000,
          "median_rent": 2200,
          "property_count": 2800
        }
      }
    ]
  }
}
```

## APN AutoComplete

For assessor's parcel number lookup:

### Request Parameters

```
GET /autocomplete/apn?query=123-45&county=Travis&state=TX
```

### Response

```json
{
  "status": "success",
  "data": {
    "suggestions": [
      {
        "place_id": "apn_123456789",
        "description": "123-456-789 - 123 Main St, Austin, TX",
        "apn": "123-456-789",
        "formatted_apn": "123-456-789",
        "county": "Travis",
        "state": "TX",
        "confidence": 0.97,
        "property_info": {
          "address": "123 Main St, Austin, TX 78701",
          "property_type": "single_family",
          "land_use": "residential",
          "owner": "John Doe"
        }
      }
    ]
  }
}
```

## Autocomplete Flavors

Configure autocomplete behavior for your application:

### Property-Focused Mode

```
GET /autocomplete/address?query=123+Main&flavor=property_focused
```

Optimizes for properties with existing data in the system.

### Investment Mode

```
GET /autocomplete/address?query=123+Main&flavor=investment
```

Emphasizes investment-relevant properties and areas.

### Residential Mode

```
GET /autocomplete/address?query=123+Main&flavor=residential
```

Focuses on residential properties and family-friendly areas.

### Commercial Mode

```
GET /autocomplete/address?query=123+Main&flavor=commercial
```

Emphasizes commercial properties and business districts.

## Browser Implementation

### JavaScript Integration

```javascript
class RealEstateAutocomplete {
  constructor(apiKey, inputElement) {
    this.apiKey = apiKey;
    this.input = inputElement;
    this.suggestionsContainer = null;
    this.debounceTimer = null;
    
    this.init();
  }
  
  init() {
    this.input.addEventListener('input', (e) => {
      this.handleInput(e.target.value);
    });
    
    this.createSuggestionsContainer();
  }
  
  handleInput(query) {
    clearTimeout(this.debounceTimer);
    
    if (query.length < 3) {
      this.hideSuggestions();
      return;
    }
    
    this.debounceTimer = setTimeout(() => {
      this.getSuggestions(query);
    }, 150);
  }
  
  async getSuggestions(query) {
    try {
      const response = await fetch(
        `https://api.realestateapi.com/v1/autocomplete/address?query=${encodeURIComponent(query)}&limit=8`,
        {
          headers: {
            'X-API-Key': this.apiKey
          }
        }
      );
      
      const data = await response.json();
      this.displaySuggestions(data.data.suggestions);
    } catch (error) {
      console.error('Autocomplete error:', error);
    }
  }
  
  displaySuggestions(suggestions) {
    this.suggestionsContainer.innerHTML = '';
    
    suggestions.forEach((suggestion, index) => {
      const item = document.createElement('div');
      item.className = 'autocomplete-item';
      item.innerHTML = `
        <div class="main-text">${suggestion.structured_formatting.main_text}</div>
        <div class="secondary-text">${suggestion.structured_formatting.secondary_text}</div>
        ${suggestion.property_context?.has_property_data ? 
          `<div class="property-info">
            ${suggestion.property_context.property_type} • 
            $${suggestion.property_context.estimated_value?.toLocaleString()}
          </div>` : ''}
      `;
      
      item.addEventListener('click', () => {
        this.selectSuggestion(suggestion);
      });
      
      this.suggestionsContainer.appendChild(item);
    });
    
    this.showSuggestions();
  }
  
  selectSuggestion(suggestion) {
    this.input.value = suggestion.description;
    this.hideSuggestions();
    
    // Trigger custom event
    this.input.dispatchEvent(new CustomEvent('address-selected', {
      detail: suggestion
    }));
  }
}

// Usage
const autocomplete = new RealEstateAutocomplete(
  'your-api-key',
  document.getElementById('address-input')
);

// Listen for selection
document.getElementById('address-input').addEventListener('address-selected', (e) => {
  const selectedAddress = e.detail;
  console.log('Selected:', selectedAddress);
  
  // Get property details if available
  if (selectedAddress.property_context?.has_property_data) {
    getPropertyDetails(selectedAddress.components);
  }
});
```

### React Component

```jsx
import React, { useState, useEffect, useRef } from 'react';

const AddressAutocomplete = ({ apiKey, onSelect, placeholder = "Enter address..." }) => {
  const [query, setQuery] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [selectedIndex, setSelectedIndex] = useState(-1);
  const debounceRef = useRef();
  
  useEffect(() => {
    if (query.length < 3) {
      setSuggestions([]);
      setShowSuggestions(false);
      return;
    }
    
    clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(async () => {
      try {
        const response = await fetch(
          `https://api.realestateapi.com/v1/autocomplete/address?query=${encodeURIComponent(query)}&limit=8`,
          {
            headers: { 'X-API-Key': apiKey }
          }
        );
        
        const data = await response.json();
        setSuggestions(data.data.suggestions);
        setShowSuggestions(true);
        setSelectedIndex(-1);
      } catch (error) {
        console.error('Autocomplete error:', error);
      }
    }, 150);
  }, [query, apiKey]);
  
  const handleKeyDown = (e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedIndex(prev => 
        prev < suggestions.length - 1 ? prev + 1 : prev
      );
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedIndex(prev => prev > 0 ? prev - 1 : -1);
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (selectedIndex >= 0) {
        selectSuggestion(suggestions[selectedIndex]);
      }
    } else if (e.key === 'Escape') {
      setShowSuggestions(false);
    }
  };
  
  const selectSuggestion = (suggestion) => {
    setQuery(suggestion.description);
    setShowSuggestions(false);
    onSelect?.(suggestion);
  };
  
  return (
    <div className="autocomplete-container">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={placeholder}
        className="autocomplete-input"
      />
      
      {showSuggestions && suggestions.length > 0 && (
        <div className="autocomplete-suggestions">
          {suggestions.map((suggestion, index) => (
            <div
              key={suggestion.place_id}
              className={`autocomplete-item ${index === selectedIndex ? 'selected' : ''}`}
              onClick={() => selectSuggestion(suggestion)}
            >
              <div className="main-text">
                {suggestion.structured_formatting.main_text}
              </div>
              <div className="secondary-text">
                {suggestion.structured_formatting.secondary_text}
              </div>
              {suggestion.property_context?.has_property_data && (
                <div className="property-info">
                  {suggestion.property_context.property_type} • 
                  ${suggestion.property_context.estimated_value?.toLocaleString()}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default AddressAutocomplete;
```

## Mobile Optimization

### Touch-Friendly Interface

```css
.autocomplete-item {
  min-height: 48px;
  padding: 12px 16px;
  border-bottom: 1px solid #eee;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.autocomplete-item:hover,
.autocomplete-item.selected {
  background-color: #f5f5f5;
}

@media (max-width: 768px) {
  .autocomplete-suggestions {
    max-height: 60vh;
    overflow-y: auto;
  }
  
  .autocomplete-item {
    min-height: 56px;
    padding: 16px;
  }
}
```

## Advanced Features

### Geocoding Integration

```javascript
async function getDetailedLocation(placeId) {
  const response = await fetch(
    `https://api.realestateapi.com/v1/autocomplete/details?place_id=${placeId}`,
    {
      headers: { 'X-API-Key': apiKey }
    }
  );
  
  const data = await response.json();
  return data.data;
}
```

### Custom Scoring

```javascript
// Customize autocomplete scoring
const customParams = {
  query: '123 Main',
  scoring: {
    property_data_weight: 0.3,
    distance_weight: 0.2,
    popularity_weight: 0.3,
    completeness_weight: 0.2
  }
};
```

## Best Practices

1. **Debouncing**: Always debounce user input (150-300ms)
2. **Minimum Query Length**: Require at least 3 characters
3. **Caching**: Cache recent results for better performance
4. **Error Handling**: Handle network errors gracefully
5. **Accessibility**: Support keyboard navigation
6. **Mobile Design**: Use touch-friendly interface elements
7. **Rate Limiting**: Respect API rate limits with proper debouncing
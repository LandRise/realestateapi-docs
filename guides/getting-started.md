# Getting Started with RealEstateAPI

Welcome to RealEstateAPI! This guide will help you get up and running with our comprehensive real estate data platform.

## Prerequisites

Before you begin, you'll need:
1. An active RealEstateAPI account
2. Your API key (available in your dashboard)
3. Basic knowledge of HTTP/REST APIs
4. A programming language or tool to make HTTP requests

## Quick Start in 5 Minutes

### Step 1: Get Your API Key

1. Sign up at [RealEstateAPI.com](https://www.realestateapi.com)
2. Navigate to your dashboard
3. Generate a new API key
4. Store it securely - you'll need it for all API requests

### Step 2: Make Your First Request

Here's a simple property search using cURL:

```bash
curl -X POST "https://api.realestateapi.com/v1/properties/search" \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "location": {
      "city": "Austin",
      "state": "TX"
    },
    "pagination": {
      "limit": 5
    }
  }'
```

### Step 3: Understanding the Response

A successful response will look like this:

```json
{
  "status": "success",
  "data": {
    "properties": [
      {
        "property_id": "PROP123456",
        "address": {
          "formatted": "123 Main St, Austin, TX 78701"
        },
        "price": 450000,
        "details": {
          "bedrooms": 3,
          "bathrooms": 2,
          "square_feet": 2200
        }
      }
    ],
    "pagination": {
      "total_results": 125,
      "has_more": true,
      "next_cursor": "eyJpZCI6MTIzfQ"
    }
  }
}
```

## Common Use Cases

### 1. Property Search Portal

Build a property search interface for your users:

```javascript
async function searchProperties(filters) {
  const response = await fetch('https://api.realestateapi.com/v1/properties/search', {
    method: 'POST',
    headers: {
      'X-API-Key': API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      location: filters.location,
      filters: {
        price: { min: filters.minPrice, max: filters.maxPrice },
        bedrooms: { min: filters.minBeds },
        property_type: filters.propertyTypes
      }
    })
  });
  
  return response.json();
}
```

### 2. Property Valuation Tool

Get instant property valuations:

```python
def get_property_value(address):
    response = requests.post(
        'https://api.realestateapi.com/v1/valuations/avm',
        headers={'X-API-Key': API_KEY},
        json={
            'property': {'address': address},
            'valuation_options': {
                'include_confidence_score': True,
                'include_comparables': True
            }
        }
    )
    
    valuation = response.json()['data']['valuation']
    return {
        'value': valuation['estimated_value'],
        'confidence': valuation['confidence_score'],
        'range': valuation['value_range']
    }
```

### 3. Lead Generation with Skip Trace

Find property owner contact information:

```php
function findPropertyOwner($address) {
    $response = makeApiRequest('POST', '/skip-trace/property-owner', [
        'property' => ['address' => $address],
        'options' => [
            'include_contact_info' => true
        ]
    ]);
    
    $owner = $response['data']['matches'][0];
    return [
        'name' => $owner['person']['full_name'],
        'phone' => $owner['contact_information']['phones'][0]['number'],
        'email' => $owner['contact_information']['emails'][0]['address']
    ];
}
```

## Best Practices

### 1. Error Handling

Always implement proper error handling:

```javascript
try {
  const response = await fetch(url, options);
  
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.error.message);
  }
  
  return response.json();
} catch (error) {
  console.error('API Error:', error);
  // Handle error appropriately
}
```

### 2. Rate Limiting

Respect rate limits to avoid service interruption:

```python
import time
from functools import wraps

def rate_limit(calls_per_minute=60):
    min_interval = 60.0 / calls_per_minute
    last_called = [0.0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_called[0] = time.time()
            return ret
        return wrapper
    return decorator

@rate_limit(calls_per_minute=60)
def call_api(endpoint, data):
    # Make API call
    pass
```

### 3. Caching

Implement caching to reduce API calls:

```javascript
const cache = new Map();
const CACHE_TTL = 3600000; // 1 hour

async function getCachedProperty(propertyId) {
  const cached = cache.get(propertyId);
  
  if (cached && Date.now() - cached.timestamp < CACHE_TTL) {
    return cached.data;
  }
  
  const data = await getPropertyDetails(propertyId);
  cache.set(propertyId, {
    data,
    timestamp: Date.now()
  });
  
  return data;
}
```

## Next Steps

1. **Explore the API Reference**: Deep dive into all available endpoints
2. **Review Code Examples**: Check out our examples in multiple languages
3. **Set Up Webhooks**: Get real-time updates for property changes
4. **Join the Community**: Connect with other developers

## Need Help?

- 📚 Browse our [full documentation](https://developer.realestateapi.com)
- 📧 Contact support at support@realestateapi.com
- 💬 Join our developer community

## Useful Resources

- [API Reference](../docs/api-reference/overview.md)
- [Authentication Guide](../docs/authentication/getting-started.md)
- [Code Examples](../examples/)
- [Postman Collection](https://www.postman.com/realestateapi/workspace)
- [Status Page](https://status.realestateapi.com)
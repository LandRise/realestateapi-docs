# Migration Guide: v2 to v3

This guide helps you migrate from RealEstateAPI v2 to v3. While v3 introduces breaking changes, we provide tools and strategies to make the transition smooth.

## Migration Timeline

- **Now - March 2025**: v3 Beta with parallel v2 support
- **April 2025**: v3 General Availability
- **April 2025 - December 2025**: v2 maintenance mode
- **January 2026**: v2 end-of-life

## Pre-Migration Checklist

- [ ] **Audit your current v2 usage** - Use our migration assessment tool
- [ ] **Review breaking changes** - Understand impacts on your application  
- [ ] **Test in v3 sandbox** - Validate your use cases
- [ ] **Update error handling** - Account for new error formats
- [ ] **Plan field mapping** - Map v2 fields to v3 equivalents

## Breaking Changes Overview

### 1. Authentication Changes

#### Multiple Authentication Methods
```javascript
// v2 - API Key only
const headers = {
  'X-API-Key': 'your-api-key'
};

// v3 - API Key OR OAuth 2.0
const headers = {
  'X-API-Key': 'your-api-key'      // Still supported
  // OR
  'Authorization': 'Bearer ' + oauthToken
};
```

### 2. Field Name Standardization

#### Property Fields
```javascript
// v2 Field Names → v3 Field Names
const fieldMapping = {
  // Basic Info
  'bedrooms' → 'bedroomCount',
  'bathrooms' → 'bathroomCount', 
  'squareFeet' → 'livingArea.squareFeet',
  'lotSize' → 'lot.area.squareFeet',
  'yearBuilt' → 'construction.yearBuilt',
  
  // Pricing
  'lastSaleDate' → 'lastSale.date',
  'lastSaleAmount' → 'lastSale.price',
  'estimatedValue' → 'valuation.estimate',
  
  // Location
  'latitude' → 'location.coordinates.latitude',
  'longitude' → 'location.coordinates.longitude',
  'address' → 'location.address.formatted',
  
  // Owner Info
  'owner1FirstName' → 'ownership.primary.firstName',
  'owner1LastName' → 'ownership.primary.lastName',
  'ownerOccupied' → 'ownership.isOwnerOccupied'
};
```

### 3. Response Structure Changes

#### Flat to Nested Objects
```json
// v2 Response
{
  "id": "prop_123",
  "bedrooms": 3,
  "bathrooms": 2.5,
  "squareFeet": 1500,
  "latitude": 40.7128,
  "longitude": -74.0060,
  "lastSaleDate": "2023-01-15",
  "lastSaleAmount": 450000
}

// v3 Response
{
  "id": "prop_123",
  "bedroomCount": 3,
  "bathroomCount": 2.5,
  "livingArea": {
    "squareFeet": 1500,
    "squareMeters": 139.35
  },
  "location": {
    "coordinates": {
      "latitude": 40.7128,
      "longitude": -74.0060
    },
    "address": {
      "formatted": "123 Main St, New York, NY 10001",
      "street": "123 Main St",
      "city": "New York",
      "state": "NY",
      "zipCode": "10001"
    }
  },
  "lastSale": {
    "date": "2023-01-15T00:00:00Z",
    "price": 450000,
    "pricePerSqFt": 300,
    "documentType": "Warranty Deed"
  }
}
```

### 4. Date Format Changes

```javascript
// v2 - Date strings
"lastSaleDate": "2023-01-15"

// v3 - ISO 8601 timestamps
"lastSale": {
  "date": "2023-01-15T00:00:00Z"
}
```

## Migration Strategies

### Strategy 1: Gradual Migration (Recommended)

1. **Phase 1**: Add v3 support alongside v2
2. **Phase 2**: Route new features to v3
3. **Phase 3**: Migrate existing functionality
4. **Phase 4**: Remove v2 dependencies

```javascript
// Adapter Pattern Example
class PropertyAdapter {
  static v2ToV3(v2Property) {
    return {
      id: v2Property.id,
      bedroomCount: v2Property.bedrooms,
      bathroomCount: v2Property.bathrooms,
      livingArea: {
        squareFeet: v2Property.squareFeet
      },
      location: {
        coordinates: {
          latitude: v2Property.latitude,
          longitude: v2Property.longitude
        }
      },
      lastSale: {
        date: new Date(v2Property.lastSaleDate).toISOString(),
        price: v2Property.lastSaleAmount
      }
    };
  }
}
```

### Strategy 2: Direct Migration

Complete migration in one update cycle using our migration tools.

## Migration Tools

### 1. Field Mapping Helper

```javascript
import { RealEstateAPIv3, createV2Adapter } from '@realestateapi/sdk-v3';

// Create adapter for seamless v2 → v3 transition
const api = new RealEstateAPIv3({
  apiKey: 'your-api-key',
  adapter: createV2Adapter() // Automatically maps v2 responses to v3 format
});

// Your existing v2 code continues working
const properties = await api.searchProperties({
  bedrooms: 3,  // Automatically mapped to bedroomCount
  bathrooms: 2  // Automatically mapped to bathroomCount
});
```

### 2. Migration Assessment Tool

```bash
npx @realestateapi/migrate-v2-v3 --analyze ./src
```

### 3. Code Generator

```bash
npx @realestateapi/migrate-v2-v3 --convert ./src --output ./src-v3
```

## Updated Error Handling

### v2 Error Format
```json
{
  "error": {
    "message": "Invalid request",
    "code": 400
  }
}
```

### v3 Error Format
```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid property search parameters",
    "details": [
      {
        "field": "bedroomCount",
        "issue": "Value must be between 0 and 20",
        "provided": "25"
      }
    ],
    "documentation": "https://docs.realestateapi.com/v3/errors/validation"
  }
}
```

### Updated Error Handling Code
```javascript
// v2 Error Handling
try {
  const response = await api.searchProperties(params);
} catch (error) {
  console.log('Error:', error.message);
}

// v3 Error Handling
try {
  const response = await api.searchProperties(params);
} catch (error) {
  if (error.code === 'VALIDATION_ERROR') {
    error.details.forEach(detail => {
      console.log(`Field ${detail.field}: ${detail.issue}`);
    });
  }
  console.log('Documentation:', error.documentation);
}
```

## Testing Your Migration

### 1. Parallel Testing

```javascript
const apiV2 = new RealEstateAPIv2({ apiKey: 'your-key' });
const apiV3 = new RealEstateAPIv3({ apiKey: 'your-key' });

const testParams = { bedrooms: 3, city: 'Austin' };

// Compare responses
const [v2Response, v3Response] = await Promise.all([
  apiV2.searchProperties(testParams),
  apiV3.searchProperties({ bedroomCount: 3, location: { city: 'Austin' } })
]);

// Validate data consistency
validateMigration(v2Response, v3Response);
```

### 2. Sandbox Environment

Test your v3 integration in our sandbox:
```
https://sandbox-api.realestateapi.com/v3/
```

## Performance Considerations

### Enhanced Caching in v3
```javascript
// v3 includes automatic caching headers
const response = await api.searchProperties(params);
console.log(response.meta.cache); // Cache information
```

### Batch Processing Improvements
```javascript
// v2 - Max 1,000 properties
const properties = await api.bulkPropertyDetails({ ids: propertyIds.slice(0, 1000) });

// v3 - Max 5,000 properties
const properties = await api.bulkPropertyDetails({ ids: propertyIds.slice(0, 5000) });
```

## Common Migration Issues

### 1. Date Parsing
```javascript
// Fix date parsing for v3
const parseDate = (dateString) => {
  return new Date(dateString).toISOString();
};
```

### 2. Nested Field Access
```javascript
// v2
const bedrooms = property.bedrooms;

// v3 - Use optional chaining
const bedrooms = property.bedroomCount;
const sqft = property.livingArea?.squareFeet;
```

### 3. Error Handling
```javascript
// Create error handler for v3 format
const handleAPIError = (error) => {
  if (error.details) {
    // v3 format
    return error.details.map(d => `${d.field}: ${d.issue}`).join(', ');
  }
  return error.message; // Fallback
};
```

## Getting Help

### Migration Support
- **Email**: migration@realestateapi.com
- **Discord**: #v3-migration channel
- **Office Hours**: Tuesdays 2-4 PM EST

### Resources
- [v3 API Reference](../api-reference/overview.md)
- [SDK Documentation](https://github.com/realestateapi/sdk-v3)
- [Migration Examples](https://github.com/realestateapi/v3-migration-examples)

### Migration Assistance Program

We offer free migration assistance for:
- Code review and recommendations
- Custom migration scripts
- Performance optimization
- 1:1 developer consultations

Contact migration@realestateapi.com to get started.
# API Reference Overview - v3

The RealEstateAPI v3 provides enhanced RESTful endpoints with improved performance, new features, and modernized data structures. All API requests should be made to:

```
https://api.realestateapi.com/v3/
```

## What's New in v3

### 🚀 Performance Improvements
- **50% faster response times** through optimized data processing
- **Improved caching** with edge-based CDN distribution
- **Batch processing enhancements** supporting up to 5,000 properties per request
- **Streaming responses** for large datasets

### 📊 Enhanced Data Models
- **Normalized property schemas** with consistent field naming
- **Extended property metadata** including sustainability ratings and smart home features
- **Real-time market trends** integrated into property responses
- **Enhanced MLS data** with agent contact verification

### 🔒 Security & Authentication
- **OAuth 2.0 support** alongside API key authentication
- **Granular permissions** with scope-based access control
- **Enhanced rate limiting** with burst allowances
- **Request signing** for high-security applications

### 🤖 AI & Machine Learning
- **PropGPT v3** with improved natural language understanding
- **Predictive analytics** for property value forecasting
- **Smart recommendations** based on search patterns
- **Automated property categorization** with ML classification

## Breaking Changes from v2

⚠️ **Important**: v3 introduces breaking changes that require code updates.

### Field Name Changes
```json
// v2 Response
{
  "bedrooms": 3,
  "bathrooms": 2.5,
  "squareFeet": 1500,
  "lastSaleDate": "2023-01-15"
}

// v3 Response  
{
  "bedroomCount": 3,
  "bathroomCount": 2.5,
  "livingArea": {
    "squareFeet": 1500,
    "squareMeters": 139.35
  },
  "lastSale": {
    "date": "2023-01-15T00:00:00Z",
    "price": 450000,
    "pricePerSqFt": 300
  }
}
```

### Response Structure
- **Nested objects** replace flat field structures
- **ISO 8601 timestamps** replace date strings
- **Metric conversions** included by default
- **Consistent error codes** across all endpoints

### Authentication Headers
```javascript
// v2
headers: {
  'X-API-Key': 'your-api-key'
}

// v3 (both supported)
headers: {
  'X-API-Key': 'your-api-key',        // Still supported
  'Authorization': 'Bearer token'      // New OAuth option
}
```

## Response Format

All API responses follow a consistent structure:

```json
{
  "status": "success",
  "version": "3.0",
  "data": {
    // Response data with enhanced structure
  },
  "meta": {
    "requestId": "req_123456789",
    "timestamp": "2024-12-19T15:30:00Z",
    "processingTime": "0.045s",
    "rateLimit": {
      "remaining": 995,
      "resetAt": "2024-12-19T16:00:00Z"
    }
  },
  "pagination": {
    // Present for paginated responses
    "page": 1,
    "perPage": 50,
    "total": 1250,
    "hasMore": true,
    "nextCursor": "eyJpZCI6MTIzNDU2fQ=="
  }
}
```

## Error Responses

Enhanced error responses with detailed troubleshooting:

```json
{
  "status": "error",
  "version": "3.0",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid property search parameters",
    "details": [
      {
        "field": "bedrooms",
        "issue": "Value must be between 0 and 20",
        "provided": "25"
      }
    ],
    "documentation": "https://docs.realestateapi.com/v3/errors/validation",
    "suggestion": "Adjust bedroom count to be within valid range"
  },
  "meta": {
    "requestId": "req_123456789",
    "timestamp": "2024-12-19T15:30:00Z"
  }
}
```

## Migration from v2

See our [Migration Guide](../migration/v2-to-v3.md) for detailed steps to upgrade from v2 to v3.

## Backwards Compatibility

- **v2 endpoints** remain supported until December 2025
- **Gradual migration** tools available
- **Side-by-side testing** environments provided
- **Migration assistance** from our developer success team

## Rate Limits

v3 introduces enhanced rate limiting:

| Tier | Requests/Hour | Burst Allowance | Concurrent Requests |
|------|---------------|-----------------|-------------------|
| Developer | 1,000 | 50 | 5 |
| Professional | 10,000 | 200 | 25 |
| Enterprise | 100,000 | 1,000 | 100 |
| Enterprise+ | Custom | Custom | Custom |

## SDKs and Tools

New SDKs available for v3:
- **JavaScript/TypeScript** - Full-featured with TypeScript definitions
- **Python** - Async/await support with type hints
- **PHP** - PSR-compliant with modern PHP features
- **Go** - High-performance with context support
- **C#** - .NET Standard 2.0+ compatible

## Support

- 📚 **Documentation**: [developer.realestateapi.com/v3](https://developer.realestateapi.com/v3)
- 💬 **Developer Discord**: Join our v3 early access channel
- 📧 **Email Support**: v3-support@realestateapi.com
- 🎯 **Migration Support**: migration@realestateapi.com
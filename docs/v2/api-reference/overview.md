# API Reference Overview

The RealEstateAPI provides RESTful endpoints for accessing comprehensive real estate data. All API requests should be made to:

```
https://api.realestateapi.com/v1/
```

## Response Format

All API responses are returned in JSON format with consistent structure:

```json
{
  "status": "success",
  "data": {
    // Response data
  },
  "meta": {
    "request_id": "uuid",
    "timestamp": "2024-01-01T00:00:00Z",
    "version": "1.0"
  }
}
```

## Error Responses

Error responses follow a consistent format:

```json
{
  "status": "error",
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      // Additional error context
    }
  }
}
```

## Common HTTP Status Codes

- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request parameters
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Access denied
- `404 Not Found` - Resource not found
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server error

## Pagination

List endpoints support pagination using cursor-based pagination:

```
GET /properties/search?cursor=eyJpZCI6MTIzfQ&limit=50
```

Parameters:
- `cursor`: Pagination cursor from previous response
- `limit`: Number of results per page (max: 100)

Response includes pagination metadata:

```json
{
  "data": [...],
  "pagination": {
    "next_cursor": "eyJpZCI6MTczfQ",
    "has_more": true,
    "total": 500
  }
}
```

## Data Formats

### Dates
All dates are in ISO 8601 format: `YYYY-MM-DDTHH:mm:ssZ`

### Coordinates
Latitude and longitude use decimal degrees:
```json
{
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

### Money
Monetary values are represented in cents as integers:
```json
{
  "price": 50000000,  // $500,000.00
  "currency": "USD"
}
```

## Request Headers

Required headers for all requests:
- `X-API-Key`: Your API authentication key
- `Content-Type`: `application/json` (for POST/PUT requests)

Optional headers:
- `X-Request-ID`: Client-generated request ID for tracking
- `Accept-Encoding`: `gzip` for compressed responses
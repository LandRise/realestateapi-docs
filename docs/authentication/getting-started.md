# Authentication

RealEstateAPI uses API keys to authenticate requests. You can obtain your API key from your dashboard after signing up.

## Getting Your API Key

1. Sign up at [RealEstateAPI.com](https://www.realestateapi.com)
2. Navigate to your dashboard
3. Generate a new API key
4. Store your API key securely

## Using Your API Key

Include your API key in the request headers:

```
X-API-Key: YOUR_API_KEY
```

### Example Request

```bash
curl -X GET "https://api.realestateapi.com/v1/properties/search" \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Security Best Practices

1. **Never expose your API key in client-side code**
2. **Use environment variables** to store API keys
3. **Rotate keys regularly**
4. **Use IP whitelisting** when available
5. **Monitor usage** through your dashboard

## Rate Limiting

API requests are subject to rate limiting based on your plan:
- Free tier: 100 requests/day
- Starter: 1,000 requests/day
- Growth: 10,000 requests/day
- Enterprise: Custom limits

Rate limit information is included in response headers:
- `X-RateLimit-Limit`: Maximum requests allowed
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Time when limit resets

## Error Handling

Authentication errors return appropriate HTTP status codes:
- `401 Unauthorized`: Invalid or missing API key
- `403 Forbidden`: Valid key but insufficient permissions
- `429 Too Many Requests`: Rate limit exceeded

### Example Error Response

```json
{
  "error": {
    "code": "INVALID_API_KEY",
    "message": "The provided API key is invalid",
    "documentation": "https://developer.realestateapi.com/docs/authentication"
  }
}
```
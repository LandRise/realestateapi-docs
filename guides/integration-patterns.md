# Integration Patterns

This guide covers common integration patterns and best practices for building applications with RealEstateAPI.

## Architecture Patterns

### 1. Direct Integration

Best for: Simple applications, prototypes, internal tools

```
Client App → RealEstateAPI
```

**Pros:**
- Simple implementation
- Direct access to all features
- Minimal infrastructure

**Cons:**
- API key exposed to client (if frontend)
- Rate limits apply per key
- No caching layer

**Implementation:**
```javascript
// Backend service
class RealEstateService {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = 'https://api.realestateapi.com/v1';
  }
  
  async searchProperties(criteria) {
    return this.makeRequest('POST', '/properties/search', criteria);
  }
  
  async makeRequest(method, endpoint, data) {
    const response = await fetch(this.baseUrl + endpoint, {
      method,
      headers: {
        'X-API-Key': this.apiKey,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    
    return response.json();
  }
}
```

### 2. Backend Proxy Pattern

Best for: Production applications, multi-tenant systems

```
Client App → Your Backend → RealEstateAPI
```

**Pros:**
- API key security
- Add caching layer
- Custom rate limiting
- Request/response transformation

**Implementation:**
```python
# Flask backend proxy
from flask import Flask, request, jsonify
import requests
from functools import lru_cache
import redis

app = Flask(__name__)
cache = redis.Redis()

@app.route('/api/properties/search', methods=['POST'])
def search_properties():
    # Add authentication/authorization
    user = authenticate_user(request)
    
    # Transform request if needed
    search_criteria = transform_search_criteria(request.json)
    
    # Check cache
    cache_key = generate_cache_key(search_criteria)
    cached_result = cache.get(cache_key)
    if cached_result:
        return jsonify(json.loads(cached_result))
    
    # Call RealEstateAPI
    response = requests.post(
        'https://api.realestateapi.com/v1/properties/search',
        headers={'X-API-Key': API_KEY},
        json=search_criteria
    )
    
    # Cache result
    cache.setex(cache_key, 3600, response.text)
    
    return jsonify(response.json())
```

### 3. Event-Driven Architecture

Best for: Real-time applications, complex workflows

```
Client → Your Backend → Message Queue → Workers → RealEstateAPI
                     ↓
                  Database
```

**Implementation:**
```javascript
// Worker process
const Queue = require('bull');
const propertyQueue = new Queue('property-processing');

propertyQueue.process(async (job) => {
  const { type, data } = job.data;
  
  switch (type) {
    case 'SEARCH':
      const results = await searchProperties(data);
      await saveResults(results);
      await notifyUser(data.userId, results);
      break;
      
    case 'VALUATION':
      const valuation = await getValuation(data.address);
      await updatePropertyValue(data.propertyId, valuation);
      break;
  }
});

// API endpoint
app.post('/properties/search', async (req, res) => {
  const job = await propertyQueue.add('SEARCH', {
    type: 'SEARCH',
    data: req.body,
    userId: req.user.id
  });
  
  res.json({ jobId: job.id, status: 'processing' });
});
```

## Data Synchronization Patterns

### 1. Real-time Sync with Webhooks

Keep your data in sync with property changes:

```javascript
// Webhook handler
app.post('/webhooks/property-updates', (req, res) => {
  const { event, data } = req.body;
  
  switch (event) {
    case 'property.price_changed':
      updatePropertyPrice(data.property_id, data.new_price);
      notifyWatchingUsers(data.property_id);
      break;
      
    case 'property.status_changed':
      updatePropertyStatus(data.property_id, data.new_status);
      if (data.new_status === 'sold') {
        removeFromActiveListings(data.property_id);
      }
      break;
  }
  
  res.sendStatus(200);
});
```

### 2. Batch Synchronization

For large datasets, use batch processing:

```python
import asyncio
from datetime import datetime, timedelta

async def sync_properties():
    # Get properties updated in last 24 hours
    last_sync = await get_last_sync_time()
    
    # Paginate through results
    cursor = None
    while True:
        response = await api.get_updated_properties(
            since=last_sync,
            cursor=cursor,
            limit=100
        )
        
        # Process batch
        await process_property_batch(response['properties'])
        
        cursor = response.get('next_cursor')
        if not cursor:
            break
    
    await set_last_sync_time(datetime.now())

# Run daily
schedule.every().day.at("02:00").do(sync_properties)
```

### 3. Incremental Updates

Track changes efficiently:

```javascript
class PropertySyncService {
  async syncProperty(propertyId) {
    const local = await db.getProperty(propertyId);
    const remote = await api.getPropertyDetails(propertyId);
    
    const changes = this.detectChanges(local, remote);
    
    if (changes.length > 0) {
      await db.updateProperty(propertyId, changes);
      await this.notifyChanges(propertyId, changes);
    }
    
    return changes;
  }
  
  detectChanges(local, remote) {
    const changes = [];
    
    // Compare each field
    for (const field of TRACKED_FIELDS) {
      if (local[field] !== remote[field]) {
        changes.push({
          field,
          oldValue: local[field],
          newValue: remote[field]
        });
      }
    }
    
    return changes;
  }
}
```

## Performance Optimization

### 1. Intelligent Caching

```javascript
class CacheManager {
  constructor(redis) {
    this.redis = redis;
    this.ttls = {
      'property_details': 3600,      // 1 hour
      'property_search': 300,        // 5 minutes
      'valuation': 86400,           // 24 hours
      'demographics': 604800        // 1 week
    };
  }
  
  async get(key, fetcher, type = 'default') {
    const cached = await this.redis.get(key);
    if (cached) return JSON.parse(cached);
    
    const data = await fetcher();
    const ttl = this.ttls[type] || 3600;
    
    await this.redis.setex(key, ttl, JSON.stringify(data));
    return data;
  }
}

// Usage
const property = await cache.get(
  `property:${id}`,
  () => api.getPropertyDetails(id),
  'property_details'
);
```

### 2. Request Batching

Combine multiple requests:

```python
class BatchProcessor:
    def __init__(self, api, batch_size=50, wait_time=100):
        self.api = api
        self.batch_size = batch_size
        self.wait_time = wait_time
        self.pending = []
        self.results = {}
        
    async def get_property(self, property_id):
        future = asyncio.Future()
        self.pending.append((property_id, future))
        
        if len(self.pending) >= self.batch_size:
            await self._process_batch()
        else:
            asyncio.create_task(self._wait_and_process())
            
        return await future
        
    async def _process_batch(self):
        if not self.pending:
            return
            
        batch = self.pending[:self.batch_size]
        self.pending = self.pending[self.batch_size:]
        
        property_ids = [item[0] for item in batch]
        results = await self.api.get_properties_bulk(property_ids)
        
        for (prop_id, future), result in zip(batch, results):
            future.set_result(result)
```

### 3. Parallel Processing

Process multiple requests concurrently:

```javascript
async function enrichProperties(properties) {
  const BATCH_SIZE = 10;
  const results = [];
  
  for (let i = 0; i < properties.length; i += BATCH_SIZE) {
    const batch = properties.slice(i, i + BATCH_SIZE);
    
    const enriched = await Promise.all(
      batch.map(async (property) => {
        const [valuation, demographics, schools] = await Promise.all([
          api.getValuation(property.address),
          api.getDemographics(property.coordinates),
          api.getNearbySchools(property.coordinates)
        ]);
        
        return {
          ...property,
          valuation,
          demographics,
          schools
        };
      })
    );
    
    results.push(...enriched);
  }
  
  return results;
}
```

## Error Handling & Resilience

### 1. Retry Logic

```javascript
async function apiCallWithRetry(fn, maxRetries = 3) {
  let lastError;
  
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error;
      
      // Don't retry on client errors
      if (error.status >= 400 && error.status < 500) {
        throw error;
      }
      
      // Exponential backoff
      const delay = Math.pow(2, i) * 1000;
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
  
  throw lastError;
}
```

### 2. Circuit Breaker

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failures = 0
        self.last_failure = None
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN
        
    async def call(self, fn):
        if self.state == 'OPEN':
            if time.time() - self.last_failure > self.timeout:
                self.state = 'HALF_OPEN'
            else:
                raise Exception('Circuit breaker is OPEN')
                
        try:
            result = await fn()
            if self.state == 'HALF_OPEN':
                self.state = 'CLOSED'
                self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            self.last_failure = time.time()
            
            if self.failures >= self.failure_threshold:
                self.state = 'OPEN'
                
            raise e
```

### 3. Fallback Strategies

```javascript
class PropertyService {
  async getPropertyWithFallback(propertyId) {
    try {
      // Try to get fresh data
      return await this.api.getProperty(propertyId);
    } catch (error) {
      console.error('API call failed:', error);
      
      // Try cache even if expired
      const cached = await this.cache.get(propertyId, { includeExpired: true });
      if (cached) {
        return { ...cached, stale: true };
      }
      
      // Return from local database
      const local = await this.db.getProperty(propertyId);
      if (local) {
        return { ...local, source: 'local' };
      }
      
      // Return partial data
      return {
        id: propertyId,
        error: 'Data temporarily unavailable',
        partial: true
      };
    }
  }
}
```

## Security Best Practices

### 1. API Key Management

```javascript
// Environment-based configuration
class ApiConfig {
  constructor() {
    this.apiKey = process.env.REALESTATEAPI_KEY;
    this.environment = process.env.NODE_ENV || 'development';
    
    if (!this.apiKey) {
      throw new Error('REALESTATEAPI_KEY environment variable is required');
    }
  }
  
  getHeaders() {
    return {
      'X-API-Key': this.apiKey,
      'X-Client-Version': process.env.npm_package_version,
      'X-Environment': this.environment
    };
  }
}
```

### 2. Request Validation

```python
from marshmallow import Schema, fields, validate

class PropertySearchSchema(Schema):
    location = fields.Dict(required=True)
    filters = fields.Dict()
    sort = fields.Dict()
    pagination = fields.Dict()
    
    # Validate specific fields
    @validates('location')
    def validate_location(self, value):
        if not any(k in value for k in ['city', 'zip', 'coordinates']):
            raise ValidationError('Location must include city, zip, or coordinates')

# Usage
def search_properties(request_data):
    schema = PropertySearchSchema()
    validated_data = schema.load(request_data)
    return api.search_properties(validated_data)
```

### 3. Rate Limiting Your Users

```javascript
const rateLimit = require('express-rate-limit');

// Different limits for different endpoints
const searchLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many searches, please try again later'
});

const detailsLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 500, // More lenient for details
  keyGenerator: (req) => req.user.id // Per user
});

app.use('/api/search', searchLimiter);
app.use('/api/property/:id', detailsLimiter);
```

## Monitoring & Observability

### 1. Request Logging

```javascript
class ApiLogger {
  logRequest(method, endpoint, duration, status, error = null) {
    const log = {
      timestamp: new Date().toISOString(),
      method,
      endpoint,
      duration_ms: duration,
      status,
      success: status < 400,
      error: error?.message
    };
    
    if (status >= 500) {
      console.error('API Error:', log);
      // Send to error tracking service
    } else {
      console.log('API Request:', log);
    }
    
    // Send to metrics service
    metrics.histogram('api.request.duration', duration, {
      endpoint,
      status
    });
  }
}
```

### 2. Health Checks

```python
async def health_check():
    checks = {
        'api': await check_api_health(),
        'database': await check_db_health(),
        'cache': await check_cache_health()
    }
    
    overall_health = all(check['healthy'] for check in checks.values())
    
    return {
        'healthy': overall_health,
        'timestamp': datetime.now().isoformat(),
        'checks': checks
    }

async def check_api_health():
    try:
        start = time.time()
        response = await api.get('/health')
        duration = time.time() - start
        
        return {
            'healthy': response.status == 200,
            'response_time_ms': duration * 1000
        }
    except Exception as e:
        return {
            'healthy': False,
            'error': str(e)
        }
```
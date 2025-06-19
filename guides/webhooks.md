# Webhooks Guide

Webhooks allow you to receive real-time notifications when events occur in RealEstateAPI. Instead of polling for changes, webhooks push data to your application as it happens.

## Overview

Webhooks are HTTP callbacks that RealEstateAPI sends to your specified endpoint URL when certain events occur. This enables you to:

- React to property status changes in real-time
- Update your database when property prices change
- Get notified about new listings matching saved searches
- Track MLS listing updates
- Monitor valuation changes

## Setting Up Webhooks

### 1. Create a Webhook Endpoint

First, create an endpoint in your application to receive webhook events:

```javascript
// Express.js example
const express = require('express');
const crypto = require('crypto');
const app = express();

// Middleware to capture raw body for signature verification
app.use('/webhooks', express.raw({ type: 'application/json' }));

app.post('/webhooks/realestateapi', (req, res) => {
  // Verify webhook signature
  const signature = req.headers['x-realestateapi-signature'];
  const timestamp = req.headers['x-realestateapi-timestamp'];
  
  if (!verifyWebhookSignature(req.body, signature, timestamp)) {
    return res.status(401).send('Invalid signature');
  }
  
  // Parse the event
  const event = JSON.parse(req.body);
  
  // Process the event
  processWebhookEvent(event);
  
  // Always respond quickly
  res.status(200).send('OK');
});

function verifyWebhookSignature(payload, signature, timestamp) {
  const secret = process.env.WEBHOOK_SECRET;
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(`${timestamp}.${payload}`)
    .digest('hex');
    
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}
```

### 2. Register Your Webhook

Register your webhook endpoint with RealEstateAPI:

```bash
curl -X POST "https://api.realestateapi.com/v1/webhooks" \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://your-app.com/webhooks/realestateapi",
    "events": [
      "property.price_changed",
      "property.status_changed",
      "listing.new",
      "listing.updated",
      "valuation.completed"
    ],
    "active": true
  }'
```

### 3. Configure Webhook Filters

You can filter which events you receive:

```json
{
  "url": "https://your-app.com/webhooks/realestateapi",
  "events": ["property.price_changed"],
  "filters": {
    "location": {
      "state": "TX",
      "cities": ["Austin", "Houston", "Dallas"]
    },
    "price_range": {
      "min": 200000,
      "max": 1000000
    },
    "property_types": ["single_family", "condo"]
  }
}
```

## Event Types

### Property Events

#### property.price_changed
Triggered when a property's price changes.

```json
{
  "id": "evt_1234567890",
  "type": "property.price_changed",
  "created": "2024-01-15T10:30:00Z",
  "data": {
    "property_id": "PROP123456",
    "address": "123 Main St, Austin, TX 78701",
    "old_price": 450000,
    "new_price": 425000,
    "change_amount": -25000,
    "change_percent": -5.56,
    "price_per_sqft": 193.18,
    "reason": "price_reduction"
  }
}
```

#### property.status_changed
Triggered when a property's listing status changes.

```json
{
  "id": "evt_1234567891",
  "type": "property.status_changed",
  "created": "2024-01-15T14:45:00Z",
  "data": {
    "property_id": "PROP123456",
    "address": "123 Main St, Austin, TX 78701",
    "old_status": "active",
    "new_status": "pending",
    "days_on_market": 15,
    "listing_id": "MLS123456"
  }
}
```

### MLS Listing Events

#### listing.new
Triggered when a new listing matches your criteria.

```json
{
  "id": "evt_1234567892",
  "type": "listing.new",
  "created": "2024-01-15T09:00:00Z",
  "data": {
    "mls_number": "MLS789012",
    "property_id": "PROP789012",
    "address": "456 Oak Ave, Austin, TX 78704",
    "list_price": 550000,
    "property_type": "single_family",
    "bedrooms": 4,
    "bathrooms": 3,
    "square_feet": 2800,
    "list_date": "2024-01-15",
    "agent": {
      "name": "Jane Smith",
      "phone": "512-555-0123",
      "email": "jane@realty.com"
    }
  }
}
```

#### listing.updated
Triggered when listing details change.

```json
{
  "id": "evt_1234567893",
  "type": "listing.updated",
  "created": "2024-01-15T11:20:00Z",
  "data": {
    "mls_number": "MLS789012",
    "property_id": "PROP789012",
    "changes": [
      {
        "field": "description",
        "old_value": "Beautiful home...",
        "new_value": "Beautiful updated home..."
      },
      {
        "field": "virtual_tour_url",
        "old_value": null,
        "new_value": "https://tours.example.com/MLS789012"
      }
    ]
  }
}
```

### Valuation Events

#### valuation.completed
Triggered when a property valuation is completed.

```json
{
  "id": "evt_1234567894",
  "type": "valuation.completed",
  "created": "2024-01-15T16:00:00Z",
  "data": {
    "valuation_id": "VAL123456",
    "property_id": "PROP123456",
    "address": "123 Main St, Austin, TX 78701",
    "estimated_value": 475000,
    "confidence_score": 0.92,
    "value_range": {
      "low": 451250,
      "high": 498750
    },
    "previous_value": 465000,
    "change_percent": 2.15
  }
}
```

## Handling Webhooks

### Processing Events Asynchronously

Don't process webhooks synchronously in your endpoint:

```python
from celery import Celery
from flask import Flask, request

app = Flask(__name__)
celery = Celery(app.name, broker='redis://localhost:6379')

@app.route('/webhooks/realestateapi', methods=['POST'])
def webhook_handler():
    # Verify signature
    if not verify_signature(request):
        return '', 401
    
    # Queue for async processing
    process_webhook.delay(request.json)
    
    # Respond immediately
    return '', 200

@celery.task
def process_webhook(event):
    event_type = event['type']
    
    if event_type == 'property.price_changed':
        handle_price_change(event['data'])
    elif event_type == 'property.status_changed':
        handle_status_change(event['data'])
    elif event_type == 'listing.new':
        handle_new_listing(event['data'])
```

### Idempotency

Handle duplicate events gracefully:

```javascript
class WebhookProcessor {
  async processEvent(event) {
    // Check if we've already processed this event
    const processed = await this.db.get(`webhook:${event.id}`);
    if (processed) {
      console.log(`Duplicate event ${event.id}, skipping`);
      return;
    }
    
    // Process the event
    await this.handleEvent(event);
    
    // Mark as processed with TTL
    await this.db.setex(`webhook:${event.id}`, 86400, '1');
  }
}
```

### Error Handling

Implement proper error handling and retries:

```python
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
async def process_webhook_with_retry(event):
    try:
        await process_webhook(event)
    except Exception as e:
        logger.error(f"Failed to process webhook {event['id']}: {e}")
        raise

async def handle_webhook_failure(event, error):
    # Log to monitoring system
    logger.error(f"Webhook processing failed after retries", extra={
        'event_id': event['id'],
        'event_type': event['type'],
        'error': str(error)
    })
    
    # Store failed event for manual review
    await store_failed_webhook(event, error)
    
    # Send alert if critical
    if event['type'] in CRITICAL_EVENTS:
        await send_alert(f"Critical webhook failed: {event['type']}")
```

## Webhook Security

### 1. Signature Verification

Always verify webhook signatures:

```javascript
const crypto = require('crypto');

function verifyWebhookSignature(payload, signature, timestamp, secret) {
  // Prevent replay attacks
  const currentTime = Math.floor(Date.now() / 1000);
  if (currentTime - parseInt(timestamp) > 300) { // 5 minutes
    return false;
  }
  
  // Compute expected signature
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(`${timestamp}.${payload}`)
    .digest('hex');
  
  // Compare signatures
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}
```

### 2. IP Whitelisting

Restrict webhook sources:

```python
ALLOWED_IPS = [
    '54.123.45.0/24',  # RealEstateAPI webhook servers
    '54.123.46.0/24'
]

def verify_webhook_source(request):
    client_ip = request.remote_addr
    
    for allowed_range in ALLOWED_IPS:
        if ip_address(client_ip) in ip_network(allowed_range):
            return True
    
    return False
```

### 3. HTTPS Only

Always use HTTPS for webhook endpoints:

```nginx
server {
    listen 443 ssl;
    server_name api.yourapp.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location /webhooks/realestateapi {
        proxy_pass http://localhost:3000;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Testing Webhooks

### 1. Local Development

Use ngrok for local webhook testing:

```bash
# Install ngrok
npm install -g ngrok

# Start your local server
node server.js

# In another terminal, expose your local server
ngrok http 3000

# Use the ngrok URL for webhook registration
# https://abc123.ngrok.io/webhooks/realestateapi
```

### 2. Test Events

Send test webhook events:

```bash
curl -X POST "https://api.realestateapi.com/v1/webhooks/test" \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "webhook_id": "webhook_123",
    "event_type": "property.price_changed"
  }'
```

### 3. Webhook Logs

View webhook delivery logs:

```bash
curl -X GET "https://api.realestateapi.com/v1/webhooks/webhook_123/logs" \
  -H "X-API-Key: YOUR_API_KEY"
```

## Monitoring Webhooks

### 1. Delivery Metrics

Track webhook performance:

```javascript
class WebhookMetrics {
  constructor(metrics) {
    this.metrics = metrics;
  }
  
  recordDelivery(event, success, duration) {
    this.metrics.increment('webhooks.delivered', {
      event_type: event.type,
      success: success.toString()
    });
    
    this.metrics.histogram('webhooks.processing_time', duration, {
      event_type: event.type
    });
    
    if (!success) {
      this.metrics.increment('webhooks.failures', {
        event_type: event.type
      });
    }
  }
}
```

### 2. Health Checks

Monitor webhook endpoint health:

```python
@app.route('/health/webhooks')
def webhook_health():
    checks = {
        'endpoint_reachable': True,
        'last_received': get_last_webhook_time(),
        'queue_size': get_webhook_queue_size(),
        'error_rate': get_webhook_error_rate()
    }
    
    healthy = (
        checks['queue_size'] < 1000 and
        checks['error_rate'] < 0.05 and
        time.time() - checks['last_received'] < 3600
    )
    
    return jsonify({
        'healthy': healthy,
        'checks': checks
    }), 200 if healthy else 503
```

## Best Practices

1. **Respond Quickly**: Return 200 OK immediately and process asynchronously
2. **Handle Retries**: RealEstateAPI retries failed deliveries with exponential backoff
3. **Verify Signatures**: Always verify webhook signatures before processing
4. **Be Idempotent**: Handle duplicate events gracefully
5. **Monitor Performance**: Track delivery success rates and processing times
6. **Set Up Alerts**: Alert on high failure rates or processing delays
7. **Document Dependencies**: Keep webhook handling code well-documented
8. **Test Thoroughly**: Test all event types in staging before production
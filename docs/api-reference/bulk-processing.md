# Bulk Processing APIs

The Bulk Processing APIs enable efficient handling of large datasets with batch operations, asynchronous processing, and webhook-based notifications for high-volume real estate data operations.

## Overview

Bulk Processing features:
- **Asynchronous Processing** - Handle up to 10,000 records per batch
- **Webhook Notifications** - Real-time status updates
- **Progress Tracking** - Monitor job completion status
- **Error Handling** - Detailed error reporting per record
- **Optimized Performance** - Parallel processing for speed

## Endpoints

### Bulk Property Search
```
POST /bulk/property-search
```

### Bulk Property Details
```
POST /bulk/property-details
```

### Bulk Skip Tracing
```
POST /bulk/skip-trace
```

### Bulk Address Verification
```
POST /bulk/address-verification
```

### Bulk Valuations
```
POST /bulk/valuations
```

### Job Status & Results
```
GET /bulk/jobs/{job_id}
GET /bulk/jobs/{job_id}/results
```

## Bulk Property Details

Process multiple property detail requests in a single operation.

### Request Body

```json
{
  "job_name": "Q1 2024 Portfolio Analysis",
  "properties": [
    {
      "id": "prop1",
      "address": "123 Main St, Austin, TX 78701"
    },
    {
      "id": "prop2",
      "property_id": "PROP123456"
    },
    {
      "id": "prop3",
      "apn": "456-789-012",
      "county": "Travis",
      "state": "TX"
    }
  ],
  "options": {
    "include": ["ownership", "tax", "sales", "valuation", "demographics"],
    "format": "json",
    "delivery_method": "webhook"
  },
  "webhook": {
    "url": "https://your-app.com/webhooks/bulk-results",
    "events": ["job_completed", "job_failed", "progress_update"]
  }
}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `job_name` | string | No | Descriptive name for the job |
| `properties` | array | Yes | Array of property identifiers (max: 1,000) |
| `options` | object | No | Processing options |
| `webhook` | object | No | Webhook configuration |

### Response

```json
{
  "status": "success",
  "data": {
    "job_id": "job_abc123",
    "status": "queued",
    "created_at": "2024-01-15T10:30:00Z",
    "total_records": 1000,
    "estimated_completion": "2024-01-15T10:45:00Z",
    "credits_estimated": 1000,
    "webhook_configured": true
  }
}
```

## Bulk Skip Tracing

### Asynchronous Bulk Skip Trace

```
POST /bulk/skip-trace/async
```

#### Request Body

```json
{
  "job_name": "Q1 Lead Generation",
  "records": [
    {
      "id": "lead1",
      "property_address": "123 Oak St, Dallas, TX 75201"
    },
    {
      "id": "lead2",
      "name": {
        "first": "John",
        "last": "Smith"
      },
      "address": {
        "street": "456 Pine Ave",
        "city": "Houston",
        "state": "TX"
      }
    },
    {
      "id": "lead3",
      "phone": "214-555-0123"
    }
  ],
  "options": {
    "include_relatives": true,
    "include_property_history": true,
    "compliance_mode": "fcra"
  },
  "webhook": {
    "url": "https://your-app.com/webhooks/skip-trace-results",
    "events": ["batch_completed", "record_processed"]
  }
}
```

### Synchronous Bulk Skip Trace

For smaller batches (up to 100 records):

```
POST /bulk/skip-trace/sync
```

#### Response

```json
{
  "status": "success",
  "data": {
    "results": [
      {
        "id": "lead1",
        "status": "success",
        "data": {
          // Skip trace results
        }
      },
      {
        "id": "lead2",
        "status": "partial",
        "data": {
          // Partial results
        },
        "warnings": ["Phone number not verified"]
      },
      {
        "id": "lead3",
        "status": "failed",
        "error": {
          "code": "INSUFFICIENT_DATA",
          "message": "Not enough information to perform skip trace"
        }
      }
    ],
    "summary": {
      "total": 3,
      "successful": 1,
      "partial": 1,
      "failed": 1,
      "credits_used": 2
    }
  }
}
```

## Bulk Address Verification

```
POST /bulk/address-verification
```

### Request Body

```json
{
  "job_name": "Mailing List Cleanup",
  "addresses": [
    {
      "id": "addr1",
      "street": "123 Main Street",
      "city": "Austin",
      "state": "TX",
      "zip": "78701"
    },
    {
      "id": "addr2",
      "full_address": "456 Oak Ave, Dallas, TX 75201"
    }
  ],
  "options": {
    "standardize": true,
    "geocode": true,
    "validate_deliverability": true,
    "return_suggestions": true
  }
}
```

## Bulk Valuations

```
POST /bulk/valuations
```

### Request Body

```json
{
  "job_name": "Portfolio Valuation Update",
  "properties": [
    {
      "id": "val1",
      "address": "123 Main St, Austin, TX 78701"
    },
    {
      "id": "val2",
      "property_id": "PROP123456"
    }
  ],
  "valuation_options": {
    "include_confidence_score": true,
    "include_comparables": true,
    "include_rental_estimate": true
  }
}
```

## Job Status Tracking

### Get Job Status

```
GET /bulk/jobs/{job_id}
```

#### Response

```json
{
  "status": "success",
  "data": {
    "job_id": "job_abc123",
    "job_name": "Q1 2024 Portfolio Analysis",
    "status": "processing",
    "created_at": "2024-01-15T10:30:00Z",
    "started_at": "2024-01-15T10:31:00Z",
    "progress": {
      "total_records": 1000,
      "processed": 650,
      "successful": 620,
      "failed": 30,
      "percent_complete": 65
    },
    "estimated_completion": "2024-01-15T10:42:00Z",
    "credits_used": 620,
    "last_updated": "2024-01-15T10:38:30Z"
  }
}
```

### Get Job Results

```
GET /bulk/jobs/{job_id}/results?page=1&limit=100
```

#### Response

```json
{
  "status": "success",
  "data": {
    "job_id": "job_abc123",
    "status": "completed",
    "results": [
      {
        "id": "prop1",
        "status": "success",
        "data": {
          // Property details
        }
      },
      {
        "id": "prop2",
        "status": "failed",
        "error": {
          "code": "PROPERTY_NOT_FOUND",
          "message": "Property not found in database"
        }
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 100,
      "total_results": 1000,
      "has_more": true
    },
    "summary": {
      "total_records": 1000,
      "successful": 950,
      "failed": 50,
      "success_rate": 0.95,
      "total_credits_used": 950
    }
  }
}
```

## Webhook Integration

### Webhook Events

#### Job Progress Update

```json
{
  "event": "progress_update",
  "job_id": "job_abc123",
  "timestamp": "2024-01-15T10:35:00Z",
  "data": {
    "progress": {
      "processed": 500,
      "total": 1000,
      "percent_complete": 50
    },
    "estimated_completion": "2024-01-15T10:45:00Z"
  }
}
```

#### Job Completed

```json
{
  "event": "job_completed",
  "job_id": "job_abc123",
  "timestamp": "2024-01-15T10:42:00Z",
  "data": {
    "status": "completed",
    "summary": {
      "total_records": 1000,
      "successful": 950,
      "failed": 50,
      "credits_used": 950
    },
    "results_url": "https://api.realestateapi.com/v1/bulk/jobs/job_abc123/results"
  }
}
```

#### Job Failed

```json
{
  "event": "job_failed",
  "job_id": "job_abc123",
  "timestamp": "2024-01-15T10:35:00Z",
  "data": {
    "error": {
      "code": "PROCESSING_ERROR",
      "message": "Job failed due to system error"
    },
    "processed_records": 245,
    "credits_used": 245
  }
}
```

## Error Handling

### Record-Level Errors

```json
{
  "id": "prop1",
  "status": "failed",
  "error": {
    "code": "INVALID_ADDRESS",
    "message": "Address format is invalid",
    "details": {
      "field": "street",
      "issue": "Missing street number"
    }
  }
}
```

### Job-Level Errors

```json
{
  "status": "error",
  "error": {
    "code": "QUOTA_EXCEEDED",
    "message": "Insufficient credits to process job",
    "details": {
      "required_credits": 1000,
      "available_credits": 750
    }
  }
}
```

## Implementation Examples

### Node.js Bulk Processing

```javascript
class BulkProcessor {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = 'https://api.realestateapi.com/v1';
  }
  
  async submitBulkJob(type, data, options = {}) {
    const response = await fetch(`${this.baseUrl}/bulk/${type}`, {
      method: 'POST',
      headers: {
        'X-API-Key': this.apiKey,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        ...data,
        webhook: {
          url: options.webhookUrl || 'https://your-app.com/webhooks/bulk',
          events: ['job_completed', 'job_failed', 'progress_update']
        }
      })
    });
    
    const result = await response.json();
    return result.data.job_id;
  }
  
  async pollJobStatus(jobId, callback) {
    const poll = async () => {
      try {
        const response = await fetch(`${this.baseUrl}/bulk/jobs/${jobId}`, {
          headers: { 'X-API-Key': this.apiKey }
        });
        
        const data = await response.json();
        const job = data.data;
        
        callback(job);
        
        if (job.status === 'processing' || job.status === 'queued') {
          setTimeout(poll, 5000); // Poll every 5 seconds
        }
      } catch (error) {
        console.error('Error polling job status:', error);
      }
    };
    
    poll();
  }
  
  async getJobResults(jobId, options = {}) {
    const { page = 1, limit = 100 } = options;
    
    const response = await fetch(
      `${this.baseUrl}/bulk/jobs/${jobId}/results?page=${page}&limit=${limit}`,
      {
        headers: { 'X-API-Key': this.apiKey }
      }
    );
    
    return response.json();
  }
}

// Usage
const processor = new BulkProcessor('your-api-key');

// Submit bulk property details job
const jobId = await processor.submitBulkJob('property-details', {
  job_name: 'Portfolio Analysis',
  properties: propertyList
});

// Monitor progress
processor.pollJobStatus(jobId, (job) => {
  console.log(`Job ${job.job_id}: ${job.progress.percent_complete}% complete`);
  
  if (job.status === 'completed') {
    console.log('Job completed successfully!');
    // Get results
    processor.getJobResults(jobId).then(results => {
      console.log(`Retrieved ${results.data.results.length} results`);
    });
  }
});
```

### Python Async Processing

```python
import asyncio
import aiohttp
from typing import List, Dict, Any

class AsyncBulkProcessor:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://api.realestateapi.com/v1'
        
    async def submit_bulk_job(self, job_type: str, data: Dict[str, Any]) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{self.base_url}/bulk/{job_type}',
                headers={'X-API-Key': self.api_key},
                json=data
            ) as response:
                result = await response.json()
                return result['data']['job_id']
    
    async def wait_for_completion(self, job_id: str, poll_interval: int = 5) -> Dict[str, Any]:
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(
                    f'{self.base_url}/bulk/jobs/{job_id}',
                    headers={'X-API-Key': self.api_key}
                ) as response:
                    result = await response.json()
                    job = result['data']
                    
                    print(f"Job {job_id}: {job['progress']['percent_complete']}% complete")
                    
                    if job['status'] in ['completed', 'failed']:
                        return job
                    
                    await asyncio.sleep(poll_interval)
    
    async def get_all_results(self, job_id: str) -> List[Dict[str, Any]]:
        all_results = []
        page = 1
        
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(
                    f'{self.base_url}/bulk/jobs/{job_id}/results?page={page}&limit=100',
                    headers={'X-API-Key': self.api_key}
                ) as response:
                    result = await response.json()
                    
                    all_results.extend(result['data']['results'])
                    
                    if not result['data']['pagination']['has_more']:
                        break
                    
                    page += 1
        
        return all_results

# Usage
async def process_bulk_data():
    processor = AsyncBulkProcessor('your-api-key')
    
    # Submit job
    job_id = await processor.submit_bulk_job('property-details', {
        'job_name': 'Bulk Property Analysis',
        'properties': property_list
    })
    
    # Wait for completion
    job = await processor.wait_for_completion(job_id)
    
    if job['status'] == 'completed':
        # Get all results
        results = await processor.get_all_results(job_id)
        print(f"Retrieved {len(results)} results")
        return results
    else:
        print(f"Job failed: {job.get('error', 'Unknown error')}")

# Run
results = asyncio.run(process_bulk_data())
```

## Best Practices

### Performance Optimization

1. **Batch Size**: Use optimal batch sizes (100-1,000 records)
2. **Webhook Processing**: Handle webhooks asynchronously
3. **Result Pagination**: Use pagination for large result sets
4. **Error Handling**: Implement retry logic for failed records
5. **Progress Monitoring**: Track job progress for user feedback

### Cost Management

1. **Estimate Credits**: Use job estimation before submission
2. **Filter Records**: Remove duplicates and invalid records
3. **Incremental Processing**: Process only new/changed records
4. **Monitor Usage**: Track credit consumption patterns

### Reliability

1. **Webhook Redundancy**: Implement webhook retry mechanisms
2. **Status Polling**: Use polling as backup to webhooks
3. **Data Validation**: Validate input data before submission
4. **Error Recovery**: Implement strategies for partial failures
# Property Portfolio Management APIs

The Property Portfolio Management APIs allow you to create, manage, and execute saved property searches. Perfect for tracking specific market segments, monitoring investment opportunities, or setting up automated property alerts.

## Overview

Portfolio Management enables:
- Save complex search criteria for reuse
- Track property market changes over time
- Set up automated monitoring
- Organize searches by investment strategy
- Share searches across team members

## Endpoints

### Create Saved Search
```
POST /portfolio/searches
```

### Get All Saved Searches
```
GET /portfolio/searches
```

### Get Specific Saved Search
```
GET /portfolio/searches/{search_id}
```

### Update Saved Search
```
PUT /portfolio/searches/{search_id}
```

### Delete Saved Search
```
DELETE /portfolio/searches/{search_id}
```

### Execute Saved Search
```
POST /portfolio/searches/{search_id}/execute
```

## Create Saved Search

### Request Body

```json
{
  "name": "Austin Investment Properties",
  "description": "Single family homes in Austin with good rental potential",
  "search_criteria": {
    "location": {
      "city": "Austin",
      "state": "TX",
      "radius_miles": 15
    },
    "filters": {
      "property_type": ["single_family"],
      "price": {
        "min": 200000,
        "max": 400000
      },
      "bedrooms": {
        "min": 3
      },
      "year_built": {
        "min": 1990
      },
      "rental_estimate": {
        "exists": true
      },
      "cap_rate": {
        "min": 0.06
      }
    },
    "sort": {
      "field": "cap_rate",
      "order": "desc"
    }
  },
  "alerts": {
    "enabled": true,
    "frequency": "daily",
    "email": "investor@example.com",
    "webhook_url": "https://your-app.com/webhooks/property-alerts"
  },
  "tags": ["investment", "austin", "rental"],
  "shared": false
}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Descriptive name for the search |
| `description` | string | No | Detailed description |
| `search_criteria` | object | Yes | Property search parameters |
| `alerts` | object | No | Alert configuration |
| `tags` | array | No | Organizational tags |
| `shared` | boolean | No | Whether search is shared with team |

### Response

```json
{
  "status": "success",
  "data": {
    "search_id": "search_12345",
    "name": "Austin Investment Properties",
    "description": "Single family homes in Austin with good rental potential",
    "search_criteria": {
      // ... search criteria
    },
    "alerts": {
      "enabled": true,
      "frequency": "daily",
      "email": "investor@example.com"
    },
    "tags": ["investment", "austin", "rental"],
    "shared": false,
    "created_date": "2024-01-15T10:30:00Z",
    "last_executed": null,
    "total_results": null,
    "status": "active"
  }
}
```

## Get All Saved Searches

### Request Parameters

```
GET /portfolio/searches?tags=investment&status=active&limit=20&offset=0
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `tags` | string | Filter by tags (comma-separated) |
| `status` | string | Filter by status (active, paused, deleted) |
| `shared` | boolean | Filter by shared status |
| `limit` | integer | Number of results (max: 100) |
| `offset` | integer | Pagination offset |

### Response

```json
{
  "status": "success",
  "data": {
    "searches": [
      {
        "search_id": "search_12345",
        "name": "Austin Investment Properties",
        "description": "Single family homes in Austin with good rental potential",
        "tags": ["investment", "austin", "rental"],
        "created_date": "2024-01-15T10:30:00Z",
        "last_executed": "2024-01-20T08:00:00Z",
        "total_results": 47,
        "new_results_count": 3,
        "status": "active",
        "alerts_enabled": true
      },
      {
        "search_id": "search_12346",
        "name": "Dallas Fix and Flip",
        "description": "Distressed properties under $150k",
        "tags": ["flip", "dallas", "distressed"],
        "created_date": "2024-01-10T14:20:00Z",
        "last_executed": "2024-01-19T09:15:00Z",
        "total_results": 23,
        "new_results_count": 1,
        "status": "active",
        "alerts_enabled": false
      }
    ],
    "pagination": {
      "total": 15,
      "limit": 20,
      "offset": 0,
      "has_more": false
    }
  }
}
```

## Execute Saved Search

Run a saved search and get current results:

### Request Body

```json
{
  "options": {
    "include_new_only": false,
    "max_results": 100,
    "include_comparisons": true
  }
}
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `include_new_only` | boolean | Return only new results since last execution |
| `max_results` | integer | Maximum results to return |
| `include_comparisons` | boolean | Include comparison with previous execution |

### Response

```json
{
  "status": "success",
  "data": {
    "search_id": "search_12345",
    "execution_id": "exec_67890",
    "executed_at": "2024-01-20T15:30:00Z",
    "results": {
      "total_count": 52,
      "new_count": 5,
      "removed_count": 2,
      "properties": [
        {
          "property_id": "PROP123456",
          "status": "new",
          "address": {
            "formatted": "123 Oak St, Austin, TX 78704"
          },
          "price": 350000,
          "rental_estimate": 2800,
          "cap_rate": 0.078,
          "first_seen": "2024-01-20T15:30:00Z"
        }
      ]
    },
    "comparison": {
      "previous_execution": "2024-01-19T08:00:00Z",
      "price_trends": {
        "median_price_change": 2.3,
        "average_days_on_market_change": -1.2
      },
      "new_properties": 5,
      "sold_properties": 2,
      "price_changes": 3
    }
  }
}
```

## Update Saved Search

### Request Body

```json
{
  "name": "Austin Investment Properties - Updated",
  "search_criteria": {
    "location": {
      "city": "Austin",
      "state": "TX",
      "radius_miles": 20
    },
    "filters": {
      "property_type": ["single_family", "townhouse"],
      "price": {
        "min": 250000,
        "max": 450000
      },
      "cap_rate": {
        "min": 0.07
      }
    }
  },
  "alerts": {
    "enabled": true,
    "frequency": "twice_daily"
  },
  "tags": ["investment", "austin", "rental", "updated"]
}
```

## Alert Configuration

### Alert Frequencies

- `immediate` - Real-time notifications
- `hourly` - Every hour
- `twice_daily` - Morning and evening
- `daily` - Once per day
- `weekly` - Once per week
- `monthly` - Once per month

### Alert Types

```json
{
  "alerts": {
    "enabled": true,
    "frequency": "daily",
    "types": {
      "new_properties": true,
      "price_changes": true,
      "status_changes": true,
      "removed_properties": false
    },
    "filters": {
      "min_price_change_percent": 5,
      "only_price_decreases": true
    },
    "delivery": {
      "email": "investor@example.com",
      "webhook_url": "https://your-app.com/webhooks/alerts",
      "sms": "+1234567890"
    }
  }
}
```

## Search Templates

Pre-built search templates for common use cases:

### Investment Property Templates

```json
{
  "template": "rental_property",
  "location": {
    "city": "Austin",
    "state": "TX"
  },
  "investment_criteria": {
    "min_cap_rate": 0.08,
    "max_price_to_rent_ratio": 150,
    "min_cash_flow": 300
  }
}
```

### Fix and Flip Template

```json
{
  "template": "fix_and_flip",
  "location": {
    "city": "Dallas",
    "state": "TX"
  },
  "flip_criteria": {
    "max_price": 200000,
    "min_arv": 300000,
    "max_renovation_estimate": 50000,
    "target_profit_margin": 0.20
  }
}
```

### Wholesale Template

```json
{
  "template": "wholesale",
  "location": {
    "state": "TX"
  },
  "wholesale_criteria": {
    "equity_percentage": {"min": 0.4},
    "distressed_indicators": true,
    "motivated_seller_signs": true
  }
}
```

## Search Analytics

Get analytics for saved searches:

### Request

```
GET /portfolio/searches/{search_id}/analytics?period=30d
```

### Response

```json
{
  "status": "success",
  "data": {
    "search_id": "search_12345",
    "period": "30d",
    "analytics": {
      "execution_count": 30,
      "total_properties_found": 1247,
      "average_properties_per_execution": 41.6,
      "new_properties_trend": {
        "daily_average": 2.3,
        "weekly_trend": "increasing",
        "peak_day": "Tuesday"
      },
      "price_trends": {
        "median_price_change": 3.2,
        "average_price_change": 2.8,
        "price_volatility": "low"
      },
      "market_insights": {
        "inventory_trend": "decreasing",
        "competition_level": "high",
        "seasonal_patterns": "spring_uptick"
      }
    }
  }
}
```

## Bulk Operations

### Create Multiple Searches

```
POST /portfolio/searches/bulk
```

```json
{
  "searches": [
    {
      "name": "Houston SFH Investment",
      "search_criteria": {
        // ... search criteria
      }
    },
    {
      "name": "Dallas Multifamily",
      "search_criteria": {
        // ... search criteria
      }
    }
  ]
}
```

### Execute Multiple Searches

```
POST /portfolio/searches/bulk-execute
```

```json
{
  "search_ids": ["search_12345", "search_12346", "search_12347"],
  "options": {
    "include_new_only": true,
    "async": true
  }
}
```

## Team Collaboration

### Share Searches

```json
{
  "shared": true,
  "permissions": {
    "team_members": [
      {
        "email": "teammate@example.com",
        "role": "viewer"
      },
      {
        "email": "manager@example.com", 
        "role": "editor"
      }
    ],
    "public_link": false
  }
}
```

### Search Folders

Organize searches into folders:

```json
{
  "folder": {
    "name": "Texas Markets",
    "description": "All Texas-based investment searches",
    "searches": ["search_12345", "search_12346"],
    "shared": true
  }
}
```

## Integration Examples

### Webhook Handler for Alerts

```javascript
app.post('/webhooks/property-alerts', (req, res) => {
  const { search_id, alert_type, properties } = req.body;
  
  switch (alert_type) {
    case 'new_properties':
      // Send notifications to interested parties
      notifyInvestors(search_id, properties);
      break;
      
    case 'price_changes':
      // Analyze price trends
      analyzePriceChanges(search_id, properties);
      break;
      
    case 'market_update':
      // Update market analytics
      updateMarketData(search_id, properties);
      break;
  }
  
  res.sendStatus(200);
});
```

### Daily Search Execution

```python
import schedule
import time

def execute_daily_searches():
    searches = api.get_saved_searches(status='active')
    
    for search in searches['data']['searches']:
        if search['alerts_enabled']:
            results = api.execute_saved_search(
                search['search_id'],
                options={'include_new_only': True}
            )
            
            if results['data']['results']['new_count'] > 0:
                send_alert_email(search, results)

schedule.every().day.at("08:00").do(execute_daily_searches)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Portfolio Dashboard

```javascript
class PortfolioDashboard {
  async loadDashboard() {
    const searches = await api.getPortfolioSearches();
    const analytics = await this.getSearchAnalytics(searches);
    
    return {
      total_searches: searches.length,
      active_searches: searches.filter(s => s.status === 'active').length,
      total_properties_tracked: analytics.total_properties,
      new_properties_today: analytics.new_today,
      market_trends: analytics.trends
    };
  }
  
  async getSearchAnalytics(searches) {
    const analytics = await Promise.all(
      searches.map(s => api.getSearchAnalytics(s.search_id, '7d'))
    );
    
    return this.aggregateAnalytics(analytics);
  }
}
```

## Best Practices

1. **Use Descriptive Names**: Make searches easy to identify
2. **Tag Strategically**: Use consistent tagging for organization
3. **Set Appropriate Alerts**: Avoid notification fatigue
4. **Monitor Performance**: Track search analytics regularly
5. **Archive Old Searches**: Keep active portfolio manageable
6. **Share Strategically**: Collaborate without overwhelming team
7. **Regular Review**: Update criteria based on market changes
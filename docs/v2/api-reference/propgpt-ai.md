# PropGPT AI API

PropGPT is RealEstateAPI's revolutionary natural language property search powered by Large Language Models (LLMs). It allows users to search for properties using plain English queries, making property data accessible to non-technical users.

## Overview

PropGPT transforms natural language queries into structured Property Search API calls, enabling:
- Conversational property search
- Complex criteria expressed in plain English
- AI-powered property recommendations
- Natural language market analysis

## Endpoint

```
POST /ai/propgpt/search
```

## Request Body

```json
{
  "query": "Find me properties in Arlington, VA with 3-5 bedrooms and 4-6 bathrooms under $800,000",
  "options": {
    "model": "gpt-4",
    "include_reasoning": true,
    "max_results": 20,
    "location_context": {
      "state": "VA",
      "radius_miles": 25
    }
  }
}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Natural language property search query |
| `model` | string | No | LLM model to use (gpt-4, gpt-3.5-turbo, claude-3) |
| `include_reasoning` | boolean | No | Include AI reasoning in response |
| `max_results` | integer | No | Maximum properties to return (default: 10) |
| `location_context` | object | No | Geographic context for ambiguous locations |

## Response

```json
{
  "status": "success",
  "data": {
    "query": {
      "original": "Find me properties in Arlington, VA with 3-5 bedrooms and 4-6 bathrooms under $800,000",
      "interpreted": {
        "location": "Arlington, VA",
        "bedrooms": "3-5",
        "bathrooms": "4-6",
        "max_price": "$800,000",
        "property_type": "residential"
      }
    },
    "search_parameters": {
      "location": {
        "city": "Arlington",
        "state": "VA"
      },
      "filters": {
        "bedrooms": {
          "min": 3,
          "max": 5
        },
        "bathrooms": {
          "min": 4,
          "max": 6
        },
        "price": {
          "max": 800000
        },
        "property_type": ["single_family", "condo", "townhouse"]
      }
    },
    "properties": [
      {
        "property_id": "PROP123456",
        "address": {
          "formatted": "123 Main St, Arlington, VA 22201"
        },
        "price": 750000,
        "details": {
          "bedrooms": 4,
          "bathrooms": 5,
          "square_feet": 3200
        },
        "match_score": 0.95,
        "ai_summary": "Excellent match - 4 bedrooms and 5 bathrooms in your target range, well under budget"
      }
    ],
    "ai_insights": {
      "reasoning": "I interpreted your query as looking for residential properties in Arlington, Virginia. I set the bedroom range to 3-5 and bathroom range to 4-6 as specified. The price filter was set to a maximum of $800,000.",
      "market_summary": "Arlington, VA is a competitive market with median home prices around $650,000. Your criteria should yield good results in this area.",
      "recommendations": [
        "Consider expanding to nearby areas like Falls Church or Alexandria for more options",
        "Properties with 4+ bathrooms are less common, you might find more options with 3+ bathrooms"
      ]
    },
    "total_results": 15,
    "model_used": "gpt-4"
  }
}
```

## Natural Language Query Examples

### Basic Searches

```javascript
// Simple location and criteria
const queries = [
  "3 bedroom homes in Austin under $500k",
  "Condos in downtown Miami with parking",
  "Houses with pools in Phoenix Arizona",
  "Investment properties in Atlanta with high rental yield"
];
```

### Complex Criteria

```javascript
// Advanced natural language queries
const complexQueries = [
  "Find me a 4-bedroom house in a good school district in Plano, Texas with a big backyard and updated kitchen under $650,000",
  "I need a condo in Seattle or Portland with 2+ bedrooms, in-unit washer/dryer, and pet-friendly building under $400k",
  "Looking for a fixer-upper single family home in Denver suburbs with at least 3 beds, 2 baths, and good bones under $450k",
  "Find waterfront properties in Florida with 3+ bedrooms, boat dock, and hurricane impact windows between $800k-1.2M"
];
```

### Investment-Focused Queries

```javascript
// Investment property searches
const investmentQueries = [
  "Show me rental properties in college towns with cap rates over 8%",
  "Find distressed properties in up-and-coming neighborhoods in Nashville",
  "Multi-family properties in Texas with positive cash flow under $300k",
  "Properties that sold recently below market value in Phoenix"
];
```

## Model Options

### Available Models

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| `gpt-4` | Slower | Highest | Complex queries, detailed analysis |
| `gpt-3.5-turbo` | Fast | High | Simple searches, quick responses |
| `claude-3` | Medium | High | Balanced performance |

### Model Selection Example

```json
{
  "query": "Find luxury homes in Beverly Hills with guest houses",
  "options": {
    "model": "gpt-4",
    "include_reasoning": true
  }
}
```

## Advanced Features

### Context-Aware Searches

PropGPT maintains conversation context for follow-up queries:

```javascript
// Initial query
const firstQuery = {
  "query": "Find 3-bedroom houses in Austin under $500k"
};

// Follow-up query with context
const followupQuery = {
  "query": "Show me only ones with pools from those results",
  "context": {
    "previous_search_id": "search_123456"
  }
};
```

### Location Disambiguation

When locations are ambiguous, PropGPT asks for clarification:

```json
{
  "query": "Houses in Springfield with 3 bedrooms",
  "response": {
    "clarification_needed": true,
    "message": "I found multiple Springfields. Which one did you mean?",
    "options": [
      "Springfield, IL",
      "Springfield, MO", 
      "Springfield, MA",
      "Springfield, OH"
    ]
  }
}
```

### Market Analysis Integration

```json
{
  "query": "Is now a good time to buy in Austin?",
  "response": {
    "analysis": {
      "market_trend": "Seller's market with high competition",
      "price_trend": "Prices increased 8% year-over-year",
      "inventory": "Low inventory, 1.2 months supply",
      "recommendation": "Consider expanding search radius or increasing budget"
    }
  }
}
```

## Error Handling

### Ambiguous Queries

```json
{
  "query": "Find me a house",
  "error": {
    "code": "INSUFFICIENT_CRITERIA",
    "message": "Please provide more specific criteria like location, price range, or property features",
    "suggestions": [
      "Specify a city or area",
      "Include price range or budget",
      "Mention bedroom/bathroom requirements"
    ]
  }
}
```

### Invalid Locations

```json
{
  "query": "Houses in Atlantis under $200k",
  "error": {
    "code": "LOCATION_NOT_FOUND",
    "message": "Could not find location 'Atlantis'",
    "suggestions": [
      "Check spelling",
      "Try nearby cities",
      "Include state for disambiguation"
    ]
  }
}
```

## Integration Examples

### Chatbot Integration

```javascript
class PropertyChatbot {
  async processUserMessage(message, sessionId) {
    try {
      const response = await api.post('/ai/propgpt/search', {
        query: message,
        options: {
          model: 'gpt-3.5-turbo',
          include_reasoning: true
        },
        session_id: sessionId
      });
      
      return this.formatChatResponse(response.data);
    } catch (error) {
      return this.handleError(error);
    }
  }
  
  formatChatResponse(data) {
    const { properties, ai_insights } = data;
    
    if (properties.length === 0) {
      return {
        text: "I couldn't find any properties matching your criteria. " + 
              ai_insights.recommendations.join(' '),
        suggestions: ["Expand search area", "Increase budget", "Adjust criteria"]
      };
    }
    
    return {
      text: `I found ${properties.length} properties matching your search.`,
      properties: properties.slice(0, 3),
      insights: ai_insights.reasoning
    };
  }
}
```

### Voice Search Integration

```javascript
class VoicePropertySearch {
  async processVoiceQuery(audioBlob) {
    // Convert speech to text
    const transcript = await this.speechToText(audioBlob);
    
    // Process with PropGPT
    const results = await api.post('/ai/propgpt/search', {
      query: transcript,
      options: {
        model: 'gpt-4',
        include_reasoning: true
      }
    });
    
    // Convert response to speech
    const audioResponse = await this.textToSpeech(
      results.data.ai_insights.reasoning
    );
    
    return {
      transcript,
      results: results.data.properties,
      audio_response: audioResponse
    };
  }
}
```

## Best Practices

### Query Optimization

1. **Be Specific**: Include location, price range, and key features
2. **Use Natural Language**: Write as you would speak
3. **Provide Context**: Mention your use case (investment, primary residence, etc.)
4. **Ask Follow-ups**: Build on previous searches for refinement

### Performance Tips

1. **Choose Appropriate Model**: Use GPT-3.5 for speed, GPT-4 for complexity
2. **Cache Results**: Store AI interpretations for similar queries
3. **Batch Processing**: Group multiple queries when possible
4. **Set Reasonable Limits**: Use max_results to control response size

### User Experience

1. **Show AI Reasoning**: Help users understand the interpretation
2. **Provide Suggestions**: Offer alternative searches
3. **Handle Ambiguity**: Ask clarifying questions
4. **Progressive Refinement**: Allow iterative search improvement

## Rate Limits

PropGPT API has separate rate limits:
- **GPT-4**: 10 requests/minute
- **GPT-3.5-turbo**: 60 requests/minute  
- **Claude-3**: 30 requests/minute

## Pricing

PropGPT usage is billed separately:
- **GPT-4**: $0.10 per query
- **GPT-3.5-turbo**: $0.02 per query
- **Claude-3**: $0.05 per query

Includes property search execution at no additional cost.
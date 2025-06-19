#!/bin/bash

# RealEstateAPI cURL Examples
# Replace YOUR_API_KEY with your actual API key

API_KEY="YOUR_API_KEY"
BASE_URL="https://api.realestateapi.com/v1"

echo "RealEstateAPI cURL Examples"
echo "=========================="

# Example 1: Search for properties
echo -e "\n1. Search for properties in Austin, TX"
echo "--------------------------------------"

curl -X POST "$BASE_URL/properties/search" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "location": {
      "city": "Austin",
      "state": "TX",
      "radius_miles": 5
    },
    "filters": {
      "price": {
        "min": 300000,
        "max": 500000
      },
      "property_type": ["single_family"],
      "bedrooms": {
        "min": 3
      }
    },
    "sort": {
      "field": "price",
      "order": "asc"
    },
    "pagination": {
      "limit": 5
    }
  }' | jq '.'

# Example 2: Verify an address
echo -e "\n\n2. Verify an address"
echo "--------------------"

curl -X POST "$BASE_URL/addresses/verify" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "address": {
      "street": "123 Main St",
      "city": "Austin",
      "state": "TX",
      "zip": "78701"
    },
    "options": {
      "standardize": true,
      "geocode": true
    }
  }' | jq '.'

# Example 3: Get property details
echo -e "\n\n3. Get property details (replace PROP123456 with actual ID)"
echo "-----------------------------------------------------------"

curl -X GET "$BASE_URL/properties/PROP123456?include=ownership,tax,valuation" \
  -H "X-API-Key: $API_KEY" | jq '.'

# Example 4: Get property valuation (AVM)
echo -e "\n\n4. Get property valuation"
echo "-------------------------"

curl -X POST "$BASE_URL/valuations/avm" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "property": {
      "address": "123 Main St, Austin, TX 78701"
    },
    "valuation_options": {
      "include_confidence_score": true,
      "include_value_range": true
    }
  }' | jq '.'

# Example 5: Search MLS listings
echo -e "\n\n5. Search active MLS listings"
echo "-----------------------------"

curl -X POST "$BASE_URL/mls/search" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "location": {
      "city": "Austin",
      "state": "TX"
    },
    "filters": {
      "status": ["active"],
      "price": {
        "min": 400000,
        "max": 600000
      },
      "property_type": ["single_family", "condo"],
      "days_on_market": {
        "max": 30
      }
    },
    "sort": {
      "field": "list_date",
      "order": "desc"
    },
    "pagination": {
      "limit": 5
    }
  }' | jq '.'

# Example 6: Autocomplete address
echo -e "\n\n6. Autocomplete address"
echo "-----------------------"

curl -X GET "$BASE_URL/addresses/autocomplete?query=123%20Main&limit=5" \
  -H "X-API-Key: $API_KEY" | jq '.'

# Example 7: Get comparable properties
echo -e "\n\n7. Get comparable properties"
echo "----------------------------"

curl -X POST "$BASE_URL/valuations/comps" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "subject_property": {
      "address": "123 Main St, Austin, TX 78701"
    },
    "comp_criteria": {
      "radius_miles": 1.0,
      "property_type_match": true,
      "min_similarity_score": 0.7,
      "max_comps": 5,
      "sale_recency_days": 180
    }
  }' | jq '.'

# Example 8: Bulk address verification
echo -e "\n\n8. Bulk address verification"
echo "----------------------------"

curl -X POST "$BASE_URL/addresses/verify/bulk" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "addresses": [
      {
        "id": "addr1",
        "street": "123 Main St",
        "city": "Austin",
        "state": "TX",
        "zip": "78701"
      },
      {
        "id": "addr2",
        "street": "456 Oak Ave",
        "city": "Houston",
        "state": "TX",
        "zip": "77001"
      }
    ],
    "options": {
      "standardize": true,
      "geocode": true
    }
  }' | jq '.'

# Example 9: Get rental estimate
echo -e "\n\n9. Get rental estimate"
echo "----------------------"

curl -X POST "$BASE_URL/valuations/rental-estimate" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "property": {
      "address": "123 Main St, Austin, TX 78701"
    },
    "rental_options": {
      "include_comps": true,
      "include_market_analysis": true,
      "lease_term_months": 12
    }
  }' | jq '.'

# Example 10: Skip trace property owner (requires appropriate permissions)
echo -e "\n\n10. Skip trace property owner"
echo "------------------------------"

curl -X POST "$BASE_URL/skip-trace/property-owner" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "property": {
      "address": "123 Main St, Austin, TX 78701"
    },
    "options": {
      "include_contact_info": true,
      "include_ownership_history": true
    }
  }' | jq '.'

echo -e "\n\nExamples completed!"
// RealEstateAPI v3 JavaScript Quick Start Example

const axios = require('axios');

// Configuration
const API_KEY = 'YOUR_API_KEY';
const BASE_URL = 'https://api.realestateapi.com/v3';

// Create axios instance with default config
const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'X-API-Key': API_KEY,
    'Content-Type': 'application/json',
    'User-Agent': 'RealEstateAPI-v3-Example/1.0'
  }
});

// Enhanced error handling for v3
const handleAPIError = (error) => {
  if (error.response?.data?.error) {
    const apiError = error.response.data.error;
    console.error(`API Error [${apiError.code}]: ${apiError.message}`);
    
    if (apiError.details) {
      apiError.details.forEach(detail => {
        console.error(`  - ${detail.field}: ${detail.issue}`);
      });
    }
    
    if (apiError.documentation) {
      console.error(`  Documentation: ${apiError.documentation}`);
    }
  } else {
    console.error('Request failed:', error.message);
  }
};

// Example 1: Enhanced Property Search with v3 features
async function searchPropertiesV3() {
  try {
    const searchParams = {
      location: {
        city: 'Austin',
        state: 'TX'
      },
      criteria: {
        bedroomCount: { min: 3, max: 5 },
        bathroomCount: { min: 2 },
        livingArea: {
          squareFeet: { min: 1500, max: 3000 }
        },
        priceRange: {
          min: 300000,
          max: 600000
        }
      },
      features: {
        hasPool: true,
        hasGarage: true
      },
      sort: [
        { field: 'lastSale.price', order: 'asc' },
        { field: 'livingArea.squareFeet', order: 'desc' }
      ],
      pagination: {
        page: 1,
        perPage: 25
      }
    };

    const response = await api.post('/properties/search', searchParams);
    
    console.log('✅ Property Search Results:');
    console.log(`Found ${response.data.meta.pagination.total} properties`);
    console.log(`Processing time: ${response.data.meta.processingTime}`);
    
    response.data.data.forEach((property, index) => {
      console.log(`\n${index + 1}. ${property.location.address.formatted}`);
      console.log(`   Bedrooms: ${property.bedroomCount} | Bathrooms: ${property.bathroomCount}`);
      console.log(`   Size: ${property.livingArea.squareFeet} sq ft`);
      console.log(`   Last Sale: $${property.lastSale?.price?.toLocaleString() || 'N/A'}`);
      console.log(`   Estimated Value: $${property.valuation?.estimate?.toLocaleString() || 'N/A'}`);
    });

    return response.data;
  } catch (error) {
    handleAPIError(error);
    throw error;
  }
}

// Example 2: PropGPT v3 - AI-Powered Natural Language Search
async function propGPTSearch() {
  try {
    const aiSearchParams = {
      query: "Find me investment properties in Dallas with good cash flow potential, preferably duplexes or small multifamily under $400k",
      context: {
        investmentFocus: true,
        includeRentalEstimates: true,
        includeCashFlowAnalysis: true
      },
      limit: 10
    };

    const response = await api.post('/ai/propgpt/search', aiSearchParams);
    
    console.log('\n🤖 PropGPT AI Search Results:');
    console.log(`AI Understanding: ${response.data.meta.aiAnalysis.queryInterpretation}`);
    console.log(`Search Strategy: ${response.data.meta.aiAnalysis.strategy}`);
    
    response.data.data.forEach((property, index) => {
      console.log(`\n${index + 1}. ${property.location.address.formatted}`);
      console.log(`   Type: ${property.propertyType} | Units: ${property.unitCount || 1}`);
      console.log(`   Price: $${property.lastSale?.price?.toLocaleString()}`);
      console.log(`   Est. Rent: $${property.rentalEstimate?.monthlyRent?.toLocaleString() || 'N/A'}/month`);
      console.log(`   Cash Flow: $${property.investment?.monthlyCashFlow || 'N/A'}/month`);
      console.log(`   AI Score: ${property.aiAnalysis?.investmentScore}/10`);
    });

    return response.data;
  } catch (error) {
    handleAPIError(error);
    throw error;
  }
}

// Example 3: Bulk Property Details with v3 enhancements
async function getBulkPropertyDetails() {
  try {
    const propertyIds = [
      'prop_123456789',
      'prop_987654321',
      'prop_456789123'
    ];

    const bulkParams = {
      propertyIds: propertyIds,
      includeDetails: {
        ownership: true,
        taxHistory: true,
        mortgageHistory: true,
        marketAnalysis: true,
        neighborhoodData: true,
        sustainabilityRating: true // New in v3
      },
      format: 'enhanced' // v3 enhanced format
    };

    const response = await api.post('/properties/bulk-details', bulkParams);
    
    console.log('\n📊 Bulk Property Details:');
    console.log(`Retrieved ${response.data.data.length} property details`);
    
    response.data.data.forEach((property, index) => {
      console.log(`\n${index + 1}. Property ID: ${property.id}`);
      console.log(`   Address: ${property.location.address.formatted}`);
      console.log(`   Owner: ${property.ownership?.primary?.name || 'N/A'}`);
      console.log(`   Tax Assessment: $${property.tax?.assessedValue?.toLocaleString() || 'N/A'}`);
      console.log(`   Sustainability: ${property.sustainability?.rating || 'N/A'} (${property.sustainability?.features?.join(', ') || 'N/A'})`);
      console.log(`   Market Trend: ${property.marketAnalysis?.trend || 'N/A'} (${property.marketAnalysis?.confidence || 'N/A'}% confidence)`);
    });

    return response.data;
  } catch (error) {
    handleAPIError(error);
    throw error;
  }
}

// Example 4: Advanced Property Valuation with ML predictions
async function getPropertyValuation() {
  try {
    const valuationParams = {
      propertyId: 'prop_123456789',
      valuationType: 'comprehensive', // Basic, standard, comprehensive
      includeComparables: true,
      includeForecast: true, // New in v3 - ML-powered price predictions
      forecastPeriod: '12-months',
      marketConditions: 'current'
    };

    const response = await api.post('/properties/valuation', valuationParams);
    
    console.log('\n💰 Property Valuation Results:');
    const valuation = response.data.data;
    
    console.log(`Current Estimate: $${valuation.currentValue.toLocaleString()}`);
    console.log(`Confidence: ${valuation.confidence}%`);
    console.log(`Value Range: $${valuation.lowEstimate.toLocaleString()} - $${valuation.highEstimate.toLocaleString()}`);
    
    if (valuation.forecast) {
      console.log(`\n📈 12-Month Forecast:`);
      console.log(`Predicted Value: $${valuation.forecast.predictedValue.toLocaleString()}`);
      console.log(`Expected Change: ${valuation.forecast.expectedChange > 0 ? '+' : ''}${valuation.forecast.expectedChange}%`);
      console.log(`Market Factors: ${valuation.forecast.marketFactors.join(', ')}`);
    }
    
    if (valuation.comparables?.length) {
      console.log(`\n🏠 Comparable Properties:`);
      valuation.comparables.slice(0, 3).forEach((comp, index) => {
        console.log(`${index + 1}. ${comp.address} - $${comp.salePrice.toLocaleString()} (${comp.daysAgo} days ago)`);
      });
    }

    return response.data;
  } catch (error) {
    handleAPIError(error);
    throw error;
  }
}

// Example 5: Real-time Market Analytics
async function getMarketAnalytics() {
  try {
    const marketParams = {
      area: {
        city: 'Austin',
        state: 'TX',
        zipCodes: ['78701', '78702', '78703'] // Optional specific zip codes
      },
      timeframe: '6-months',
      metrics: [
        'averagePricePerSqFt',
        'medianSalePrice',
        'daysOnMarket',
        'inventoryLevels',
        'priceAppreciation',
        'marketVelocity' // New in v3
      ],
      segmentation: {
        byPropertyType: true,
        byPriceRange: true,
        byNeighborhood: true
      }
    };

    const response = await api.post('/market/analytics', marketParams);
    
    console.log('\n📊 Market Analytics:');
    const analytics = response.data.data;
    
    console.log(`Market Summary for ${analytics.area.description}:`);
    console.log(`Median Sale Price: $${analytics.metrics.medianSalePrice.toLocaleString()}`);
    console.log(`Avg Price/SqFt: $${analytics.metrics.averagePricePerSqFt}`);
    console.log(`Avg Days on Market: ${analytics.metrics.daysOnMarket}`);
    console.log(`Market Velocity: ${analytics.metrics.marketVelocity} (${analytics.metrics.velocityTrend})`);
    console.log(`Price Appreciation (YoY): ${analytics.metrics.priceAppreciation}%`);
    
    if (analytics.trends?.length) {
      console.log(`\n📈 Market Trends:`);
      analytics.trends.forEach(trend => {
        console.log(`- ${trend.description}: ${trend.direction} (${trend.strength})`);
      });
    }

    return response.data;
  } catch (error) {
    handleAPIError(error);
    throw error;
  }
}

// Main execution function
async function main() {
  console.log('🏠 RealEstateAPI v3 JavaScript Examples\n');
  
  try {
    // Run examples
    await searchPropertiesV3();
    await propGPTSearch();
    await getBulkPropertyDetails();
    await getPropertyValuation();
    await getMarketAnalytics();
    
    console.log('\n✅ All examples completed successfully!');
  } catch (error) {
    console.error('\n❌ Example execution failed:', error.message);
  }
}

// Rate limiting helper (v3 includes rate limit info in responses)
api.interceptors.response.use(
  response => {
    if (response.data.meta?.rateLimit) {
      const rateLimit = response.data.meta.rateLimit;
      console.log(`Rate Limit: ${rateLimit.remaining} requests remaining, resets at ${rateLimit.resetAt}`);
    }
    return response;
  },
  error => {
    return Promise.reject(error);
  }
);

// Export functions for use in other modules
module.exports = {
  searchPropertiesV3,
  propGPTSearch,
  getBulkPropertyDetails,
  getPropertyValuation,
  getMarketAnalytics
};

// Run examples if this file is executed directly
if (require.main === module) {
  main();
}
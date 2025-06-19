"""
RealEstateAPI v3 Python Quick Start Example
Enhanced with v3 features including async support, improved error handling, and new endpoints
"""

import asyncio
import aiohttp
import json
from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

# Configuration
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api.realestateapi.com/v3'

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RealEstateAPIv3:
    """Enhanced RealEstateAPI v3 client with async support"""
    
    def __init__(self, api_key: str, base_url: str = BASE_URL):
        self.api_key = api_key
        self.base_url = base_url
        self.session = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            headers={
                'X-API-Key': self.api_key,
                'Content-Type': 'application/json',
                'User-Agent': 'RealEstateAPI-v3-Python/1.0'
            }
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    def _handle_api_error(self, error_data: Dict[str, Any]) -> None:
        """Enhanced error handling for v3 API responses"""
        if 'error' in error_data:
            error = error_data['error']
            logger.error(f"API Error [{error.get('code')}]: {error.get('message')}")
            
            if 'details' in error:
                for detail in error['details']:
                    logger.error(f"  - {detail.get('field')}: {detail.get('issue')}")
            
            if 'documentation' in error:
                logger.error(f"  Documentation: {error['documentation']}")
                
            raise Exception(f"API Error: {error.get('message')}")
    
    async def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make API request with enhanced error handling"""
        url = f"{self.base_url}{endpoint}"
        
        async with self.session.request(method, url, json=data) as response:
            response_data = await response.json()
            
            # Log rate limit information if available
            if 'meta' in response_data and 'rateLimit' in response_data['meta']:
                rate_limit = response_data['meta']['rateLimit']
                logger.info(f"Rate Limit: {rate_limit.get('remaining')} requests remaining")
            
            if response.status >= 400:
                self._handle_api_error(response_data)
            
            return response_data

async def search_properties_v3(api: RealEstateAPIv3) -> Dict[str, Any]:
    """Enhanced Property Search with v3 features"""
    search_params = {
        'location': {
            'city': 'Austin',
            'state': 'TX'
        },
        'criteria': {
            'bedroomCount': {'min': 3, 'max': 5},
            'bathroomCount': {'min': 2},
            'livingArea': {
                'squareFeet': {'min': 1500, 'max': 3000}
            },
            'priceRange': {
                'min': 300000,
                'max': 600000
            }
        },
        'features': {
            'hasPool': True,
            'hasGarage': True
        },
        'sort': [
            {'field': 'lastSale.price', 'order': 'asc'},
            {'field': 'livingArea.squareFeet', 'order': 'desc'}
        ],
        'pagination': {
            'page': 1,
            'perPage': 25
        }
    }
    
    response = await api._make_request('POST', '/properties/search', search_params)
    
    logger.info('✅ Property Search Results:')
    logger.info(f"Found {response['meta']['pagination']['total']} properties")
    logger.info(f"Processing time: {response['meta']['processingTime']}")
    
    for idx, property_data in enumerate(response['data'], 1):
        logger.info(f"\n{idx}. {property_data['location']['address']['formatted']}")
        logger.info(f"   Bedrooms: {property_data['bedroomCount']} | Bathrooms: {property_data['bathroomCount']}")
        logger.info(f"   Size: {property_data['livingArea']['squareFeet']} sq ft")
        
        last_sale = property_data.get('lastSale', {})
        last_price = last_sale.get('price', 'N/A')
        if isinstance(last_price, (int, float)):
            last_price = f"${last_price:,}"
        logger.info(f"   Last Sale: {last_price}")
        
        valuation = property_data.get('valuation', {})
        estimate = valuation.get('estimate', 'N/A')
        if isinstance(estimate, (int, float)):
            estimate = f"${estimate:,}"
        logger.info(f"   Estimated Value: {estimate}")
    
    return response

async def propgpt_search(api: RealEstateAPIv3) -> Dict[str, Any]:
    """PropGPT v3 - AI-Powered Natural Language Search"""
    ai_search_params = {
        'query': "Find me investment properties in Dallas with good cash flow potential, preferably duplexes or small multifamily under $400k",
        'context': {
            'investmentFocus': True,
            'includeRentalEstimates': True,
            'includeCashFlowAnalysis': True
        },
        'limit': 10
    }
    
    response = await api._make_request('POST', '/ai/propgpt/search', ai_search_params)
    
    logger.info('\n🤖 PropGPT AI Search Results:')
    ai_analysis = response['meta']['aiAnalysis']
    logger.info(f"AI Understanding: {ai_analysis['queryInterpretation']}")
    logger.info(f"Search Strategy: {ai_analysis['strategy']}")
    
    for idx, property_data in enumerate(response['data'], 1):
        logger.info(f"\n{idx}. {property_data['location']['address']['formatted']}")
        logger.info(f"   Type: {property_data['propertyType']} | Units: {property_data.get('unitCount', 1)}")
        
        last_sale = property_data.get('lastSale', {})
        price = last_sale.get('price')
        price_str = f"${price:,}" if price else 'N/A'
        logger.info(f"   Price: {price_str}")
        
        rental_estimate = property_data.get('rentalEstimate', {})
        monthly_rent = rental_estimate.get('monthlyRent', 'N/A')
        if isinstance(monthly_rent, (int, float)):
            monthly_rent = f"${monthly_rent:,}/month"
        logger.info(f"   Est. Rent: {monthly_rent}")
        
        investment = property_data.get('investment', {})
        cash_flow = investment.get('monthlyCashFlow', 'N/A')
        if isinstance(cash_flow, (int, float)):
            cash_flow = f"${cash_flow}/month"
        logger.info(f"   Cash Flow: {cash_flow}")
        
        ai_analysis = property_data.get('aiAnalysis', {})
        score = ai_analysis.get('investmentScore', 'N/A')
        logger.info(f"   AI Score: {score}/10")
    
    return response

async def get_bulk_property_details(api: RealEstateAPIv3) -> Dict[str, Any]:
    """Bulk Property Details with v3 enhancements"""
    property_ids = [
        'prop_123456789',
        'prop_987654321',
        'prop_456789123'
    ]
    
    bulk_params = {
        'propertyIds': property_ids,
        'includeDetails': {
            'ownership': True,
            'taxHistory': True,
            'mortgageHistory': True,
            'marketAnalysis': True,
            'neighborhoodData': True,
            'sustainabilityRating': True  # New in v3
        },
        'format': 'enhanced'  # v3 enhanced format
    }
    
    response = await api._make_request('POST', '/properties/bulk-details', bulk_params)
    
    logger.info('\n📊 Bulk Property Details:')
    logger.info(f"Retrieved {len(response['data'])} property details")
    
    for idx, property_data in enumerate(response['data'], 1):
        logger.info(f"\n{idx}. Property ID: {property_data['id']}")
        logger.info(f"   Address: {property_data['location']['address']['formatted']}")
        
        ownership = property_data.get('ownership', {}).get('primary', {})
        owner_name = ownership.get('name', 'N/A')
        logger.info(f"   Owner: {owner_name}")
        
        tax = property_data.get('tax', {})
        assessed_value = tax.get('assessedValue')
        assessed_str = f"${assessed_value:,}" if assessed_value else 'N/A'
        logger.info(f"   Tax Assessment: {assessed_str}")
        
        sustainability = property_data.get('sustainability', {})
        rating = sustainability.get('rating', 'N/A')
        features = sustainability.get('features', [])
        features_str = ', '.join(features) if features else 'N/A'
        logger.info(f"   Sustainability: {rating} ({features_str})")
        
        market_analysis = property_data.get('marketAnalysis', {})
        trend = market_analysis.get('trend', 'N/A')
        confidence = market_analysis.get('confidence', 'N/A')
        logger.info(f"   Market Trend: {trend} ({confidence}% confidence)")
    
    return response

async def get_property_valuation(api: RealEstateAPIv3) -> Dict[str, Any]:
    """Advanced Property Valuation with ML predictions"""
    valuation_params = {
        'propertyId': 'prop_123456789',
        'valuationType': 'comprehensive',  # Basic, standard, comprehensive
        'includeComparables': True,
        'includeForecast': True,  # New in v3 - ML-powered price predictions
        'forecastPeriod': '12-months',
        'marketConditions': 'current'
    }
    
    response = await api._make_request('POST', '/properties/valuation', valuation_params)
    
    logger.info('\n💰 Property Valuation Results:')
    valuation = response['data']
    
    current_value = valuation['currentValue']
    logger.info(f"Current Estimate: ${current_value:,}")
    logger.info(f"Confidence: {valuation['confidence']}%")
    
    low_est = valuation['lowEstimate']
    high_est = valuation['highEstimate']
    logger.info(f"Value Range: ${low_est:,} - ${high_est:,}")
    
    if 'forecast' in valuation:
        forecast = valuation['forecast']
        predicted_value = forecast['predictedValue']
        logger.info(f"\n📈 12-Month Forecast:")
        logger.info(f"Predicted Value: ${predicted_value:,}")
        
        change = forecast['expectedChange']
        change_str = f"+{change}" if change > 0 else str(change)
        logger.info(f"Expected Change: {change_str}%")
        
        factors = ', '.join(forecast['marketFactors'])
        logger.info(f"Market Factors: {factors}")
    
    if valuation.get('comparables'):
        logger.info(f"\n🏠 Comparable Properties:")
        for idx, comp in enumerate(valuation['comparables'][:3], 1):
            sale_price = comp['salePrice']
            logger.info(f"{idx}. {comp['address']} - ${sale_price:,} ({comp['daysAgo']} days ago)")
    
    return response

async def get_market_analytics(api: RealEstateAPIv3) -> Dict[str, Any]:
    """Real-time Market Analytics"""
    market_params = {
        'area': {
            'city': 'Austin',
            'state': 'TX',
            'zipCodes': ['78701', '78702', '78703']  # Optional specific zip codes
        },
        'timeframe': '6-months',
        'metrics': [
            'averagePricePerSqFt',
            'medianSalePrice',
            'daysOnMarket',
            'inventoryLevels',
            'priceAppreciation',
            'marketVelocity'  # New in v3
        ],
        'segmentation': {
            'byPropertyType': True,
            'byPriceRange': True,
            'byNeighborhood': True
        }
    }
    
    response = await api._make_request('POST', '/market/analytics', market_params)
    
    logger.info('\n📊 Market Analytics:')
    analytics = response['data']
    
    area_desc = analytics['area']['description']
    logger.info(f"Market Summary for {area_desc}:")
    
    metrics = analytics['metrics']
    median_price = metrics['medianSalePrice']
    logger.info(f"Median Sale Price: ${median_price:,}")
    logger.info(f"Avg Price/SqFt: ${metrics['averagePricePerSqFt']}")
    logger.info(f"Avg Days on Market: {metrics['daysOnMarket']}")
    
    velocity = metrics['marketVelocity']
    velocity_trend = metrics['velocityTrend']
    logger.info(f"Market Velocity: {velocity} ({velocity_trend})")
    logger.info(f"Price Appreciation (YoY): {metrics['priceAppreciation']}%")
    
    if analytics.get('trends'):
        logger.info(f"\n📈 Market Trends:")
        for trend in analytics['trends']:
            description = trend['description']
            direction = trend['direction']
            strength = trend['strength']
            logger.info(f"- {description}: {direction} ({strength})")
    
    return response

async def main():
    """Main execution function"""
    logger.info('🏠 RealEstateAPI v3 Python Examples\n')
    
    async with RealEstateAPIv3(API_KEY) as api:
        try:
            # Run examples
            await search_properties_v3(api)
            await propgpt_search(api)
            await get_bulk_property_details(api)
            await get_property_valuation(api)
            await get_market_analytics(api)
            
            logger.info('\n✅ All examples completed successfully!')
        except Exception as error:
            logger.error(f'\n❌ Example execution failed: {error}')

# Example of synchronous wrapper for non-async environments
def run_example(example_function):
    """Wrapper to run async examples in sync environments"""
    async def wrapper():
        async with RealEstateAPIv3(API_KEY) as api:
            return await example_function(api)
    
    return asyncio.run(wrapper())

if __name__ == '__main__':
    asyncio.run(main())
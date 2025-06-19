"""
RealEstateAPI Python Quick Start Example
"""

import requests
import json
from typing import Dict, List, Optional

# Configuration
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api.realestateapi.com/v1'

# Create session with default headers
session = requests.Session()
session.headers.update({
    'X-API-Key': API_KEY,
    'Content-Type': 'application/json'
})


def search_properties(city: str, state: str, min_price: int = None, 
                     max_price: int = None, property_types: List[str] = None) -> Dict:
    """
    Search for properties based on location and filters
    
    Args:
        city: City name
        state: Two-letter state code
        min_price: Minimum price filter
        max_price: Maximum price filter
        property_types: List of property types to include
        
    Returns:
        Dictionary containing search results
    """
    payload = {
        'location': {
            'city': city,
            'state': state,
            'radius_miles': 5
        },
        'filters': {},
        'sort': {
            'field': 'price',
            'order': 'asc'
        },
        'pagination': {
            'limit': 10
        }
    }
    
    # Add price filter if provided
    if min_price or max_price:
        payload['filters']['price'] = {}
        if min_price:
            payload['filters']['price']['min'] = min_price
        if max_price:
            payload['filters']['price']['max'] = max_price
    
    # Add property type filter if provided
    if property_types:
        payload['filters']['property_type'] = property_types
    
    try:
        response = session.post(f'{BASE_URL}/properties/search', json=payload)
        response.raise_for_status()
        
        data = response.json()
        properties = data['data']['properties']
        total_results = data['data']['pagination']['total_results']
        
        print(f"Found {total_results} properties")
        
        # Display first property if available
        if properties:
            first = properties[0]
            print("\nFirst property:")
            print(f"Address: {first['address']['formatted']}")
            print(f"Price: ${first['price']:,}")
            print(f"Bedrooms: {first['details']['bedrooms']}")
            print(f"Bathrooms: {first['details']['bathrooms']}")
            print(f"Square Feet: {first['details']['square_feet']:,}")
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error searching properties: {e}")
        if hasattr(e.response, 'json'):
            print(f"API Error: {e.response.json()}")
        return None


def get_property_details(property_id: str, includes: List[str] = None) -> Dict:
    """
    Get detailed information about a specific property
    
    Args:
        property_id: Unique property identifier
        includes: List of additional data to include
        
    Returns:
        Dictionary containing property details
    """
    params = {}
    if includes:
        params['include'] = ','.join(includes)
    
    try:
        response = session.get(f'{BASE_URL}/properties/{property_id}', params=params)
        response.raise_for_status()
        
        property_data = response.json()['data']
        
        print("\nProperty Details:")
        print(f"Address: {property_data['address']['formatted']}")
        print(f"Property Type: {property_data['property_type']}")
        print(f"Year Built: {property_data['characteristics']['year_built']}")
        
        if 'ownership' in property_data:
            owners = property_data['ownership']['current']['owner_names']
            print(f"Owner(s): {', '.join(owners)}")
        
        if 'valuation' in property_data:
            value = property_data['valuation']['estimated_value']
            print(f"Estimated Value: ${value:,}")
        
        return property_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error getting property details: {e}")
        return None


def verify_address(street: str, city: str, state: str, zip_code: str = None) -> Dict:
    """
    Verify and standardize an address
    
    Args:
        street: Street address
        city: City name
        state: Two-letter state code
        zip_code: ZIP code (optional)
        
    Returns:
        Dictionary containing verification results
    """
    payload = {
        'address': {
            'street': street,
            'city': city,
            'state': state
        },
        'options': {
            'standardize': True,
            'geocode': True
        }
    }
    
    if zip_code:
        payload['address']['zip'] = zip_code
    
    try:
        response = session.post(f'{BASE_URL}/addresses/verify', json=payload)
        response.raise_for_status()
        
        result = response.json()['data']
        
        print("\nAddress Verification:")
        print(f"Valid: {result['is_valid']}")
        print(f"Confidence Score: {result['confidence_score']}")
        print(f"Standardized: {result['standardized_address']['formatted']}")
        
        if 'geocode' in result:
            lat = result['geocode']['latitude']
            lon = result['geocode']['longitude']
            print(f"Coordinates: {lat}, {lon}")
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"Error verifying address: {e}")
        return None


def get_property_valuation(address: str) -> Dict:
    """
    Get automated valuation (AVM) for a property
    
    Args:
        address: Full property address
        
    Returns:
        Dictionary containing valuation data
    """
    payload = {
        'property': {
            'address': address
        },
        'valuation_options': {
            'include_confidence_score': True,
            'include_value_range': True,
            'include_comparables': True
        }
    }
    
    try:
        response = session.post(f'{BASE_URL}/valuations/avm', json=payload)
        response.raise_for_status()
        
        valuation_data = response.json()['data']['valuation']
        
        print("\nProperty Valuation:")
        print(f"Estimated Value: ${valuation_data['estimated_value']:,}")
        print(f"Confidence Score: {valuation_data['confidence_score']}")
        
        value_range = valuation_data['value_range']
        print(f"Value Range: ${value_range['low']:,} - ${value_range['high']:,}")
        
        return valuation_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error getting valuation: {e}")
        return None


def search_mls_listings(city: str, state: str, status: List[str] = None,
                       min_price: int = None, max_price: int = None) -> Dict:
    """
    Search active MLS listings
    
    Args:
        city: City name
        state: Two-letter state code
        status: List of listing statuses to include
        min_price: Minimum list price
        max_price: Maximum list price
        
    Returns:
        Dictionary containing MLS search results
    """
    payload = {
        'location': {
            'city': city,
            'state': state
        },
        'filters': {
            'status': status or ['active']
        },
        'sort': {
            'field': 'list_date',
            'order': 'desc'
        },
        'pagination': {
            'limit': 10
        }
    }
    
    # Add price filter
    if min_price or max_price:
        payload['filters']['price'] = {}
        if min_price:
            payload['filters']['price']['min'] = min_price
        if max_price:
            payload['filters']['price']['max'] = max_price
    
    try:
        response = session.post(f'{BASE_URL}/mls/search', json=payload)
        response.raise_for_status()
        
        data = response.json()
        listings = data['data']['listings']
        
        print(f"\nFound {len(listings)} MLS listings")
        
        # Display first listing
        if listings:
            first = listings[0]
            print(f"\nFirst listing:")
            print(f"MLS #: {first['mls_number']}")
            print(f"Address: {first['address']['street']}, {first['address']['city']}")
            print(f"List Price: ${first['price']['list_price']:,}")
            print(f"Status: {first['status']}")
            print(f"Days on Market: {first['days_on_market']}")
            print(f"Bedrooms: {first['property']['bedrooms']}")
            print(f"Bathrooms: {first['property']['bathrooms']}")
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error searching MLS: {e}")
        return None


def main():
    """Run example API calls"""
    print("RealEstateAPI Python Examples")
    print("=" * 50)
    
    # Example 1: Search for properties
    print("\n1. Searching for properties in Austin, TX...")
    search_properties(
        city='Austin',
        state='TX',
        min_price=300000,
        max_price=500000,
        property_types=['single_family']
    )
    
    # Example 2: Verify an address
    print("\n2. Verifying an address...")
    verify_address(
        street='123 Main St',
        city='Austin',
        state='TX',
        zip_code='78701'
    )
    
    # Example 3: Get property valuation
    print("\n3. Getting property valuation...")
    get_property_valuation('123 Main St, Austin, TX 78701')
    
    # Example 4: Search MLS listings
    print("\n4. Searching MLS listings...")
    search_mls_listings(
        city='Austin',
        state='TX',
        status=['active'],
        min_price=400000,
        max_price=600000
    )
    
    # Note: Uncomment to test with a real property ID
    # get_property_details('PROP123456', includes=['ownership', 'tax', 'valuation'])


if __name__ == '__main__':
    main()
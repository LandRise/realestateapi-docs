// RealEstateAPI JavaScript Quick Start Example

const axios = require('axios');

// Configuration
const API_KEY = 'YOUR_API_KEY';
const BASE_URL = 'https://api.realestateapi.com/v1';

// Create axios instance with default config
const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'X-API-Key': API_KEY,
    'Content-Type': 'application/json'
  }
});

// Example 1: Search for properties
async function searchProperties() {
  try {
    const response = await api.post('/properties/search', {
      location: {
        city: 'Austin',
        state: 'TX',
        radius_miles: 5
      },
      filters: {
        price: {
          min: 300000,
          max: 500000
        },
        property_type: ['single_family'],
        bedrooms: {
          min: 3
        }
      },
      sort: {
        field: 'price',
        order: 'asc'
      },
      pagination: {
        limit: 10
      }
    });

    console.log(`Found ${response.data.data.pagination.total_results} properties`);
    
    // Display first property
    const firstProperty = response.data.data.properties[0];
    console.log('\nFirst property:');
    console.log(`Address: ${firstProperty.address.formatted}`);
    console.log(`Price: $${firstProperty.price.toLocaleString()}`);
    console.log(`Bedrooms: ${firstProperty.details.bedrooms}`);
    console.log(`Bathrooms: ${firstProperty.details.bathrooms}`);
    console.log(`Square Feet: ${firstProperty.details.square_feet}`);

    return response.data.data.properties;
  } catch (error) {
    console.error('Error searching properties:', error.response?.data || error.message);
  }
}

// Example 2: Get property details
async function getPropertyDetails(propertyId) {
  try {
    const response = await api.get(`/properties/${propertyId}`, {
      params: {
        include: ['ownership', 'tax', 'sales', 'valuation']
      }
    });

    const property = response.data.data;
    console.log('\nProperty Details:');
    console.log(`Address: ${property.address.formatted}`);
    console.log(`Property Type: ${property.property_type}`);
    console.log(`Year Built: ${property.characteristics.year_built}`);
    console.log(`Owner: ${property.ownership.current.owner_names.join(', ')}`);
    console.log(`Estimated Value: $${property.valuation.estimated_value.toLocaleString()}`);

    return property;
  } catch (error) {
    console.error('Error getting property details:', error.response?.data || error.message);
  }
}

// Example 3: Verify an address
async function verifyAddress(street, city, state, zip) {
  try {
    const response = await api.post('/addresses/verify', {
      address: {
        street,
        city,
        state,
        zip
      },
      options: {
        standardize: true,
        geocode: true
      }
    });

    const result = response.data.data;
    console.log('\nAddress Verification:');
    console.log(`Valid: ${result.is_valid}`);
    console.log(`Standardized: ${result.standardized_address.formatted}`);
    console.log(`Coordinates: ${result.geocode.latitude}, ${result.geocode.longitude}`);

    return result;
  } catch (error) {
    console.error('Error verifying address:', error.response?.data || error.message);
  }
}

// Example 4: Get property valuation (AVM)
async function getPropertyValuation(address) {
  try {
    const response = await api.post('/valuations/avm', {
      property: {
        address
      },
      valuation_options: {
        include_confidence_score: true,
        include_value_range: true,
        include_comparables: true
      }
    });

    const valuation = response.data.data.valuation;
    console.log('\nProperty Valuation:');
    console.log(`Estimated Value: $${valuation.estimated_value.toLocaleString()}`);
    console.log(`Confidence Score: ${valuation.confidence_score}`);
    console.log(`Value Range: $${valuation.value_range.low.toLocaleString()} - $${valuation.value_range.high.toLocaleString()}`);

    return valuation;
  } catch (error) {
    console.error('Error getting valuation:', error.response?.data || error.message);
  }
}

// Example 5: Skip trace property owner
async function skipTraceOwner(address) {
  try {
    const response = await api.post('/skip-trace/property-owner', {
      property: {
        address
      },
      options: {
        include_contact_info: true,
        include_ownership_history: true
      }
    });

    const owner = response.data.data.matches[0];
    console.log('\nProperty Owner Information:');
    console.log(`Name: ${owner.person.full_name}`);
    console.log(`Phone: ${owner.contact_information.phones[0]?.number || 'Not available'}`);
    console.log(`Email: ${owner.contact_information.emails[0]?.address || 'Not available'}`);

    return owner;
  } catch (error) {
    console.error('Error skip tracing:', error.response?.data || error.message);
  }
}

// Run examples
async function runExamples() {
  console.log('RealEstateAPI JavaScript Examples\n');
  console.log('================================\n');

  // Search properties
  await searchProperties();

  // Verify an address
  await verifyAddress('123 Main St', 'Austin', 'TX', '78701');

  // Get property valuation
  await getPropertyValuation('123 Main St, Austin, TX 78701');

  // Note: Uncomment to test with a real property ID
  // await getPropertyDetails('PROP123456');
  
  // Note: Skip trace requires appropriate permissions
  // await skipTraceOwner('123 Main St, Austin, TX 78701');
}

// Run the examples
runExamples();

// Export functions for use in other modules
module.exports = {
  searchProperties,
  getPropertyDetails,
  verifyAddress,
  getPropertyValuation,
  skipTraceOwner
};
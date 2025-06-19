<?php
/**
 * RealEstateAPI PHP Quick Start Example
 */

// Configuration
define('API_KEY', 'YOUR_API_KEY');
define('BASE_URL', 'https://api.realestateapi.com/v1');

/**
 * Make API request
 */
function makeApiRequest($method, $endpoint, $data = null) {
    $url = BASE_URL . $endpoint;
    
    $headers = [
        'X-API-Key: ' . API_KEY,
        'Content-Type: application/json'
    ];
    
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    
    if ($method === 'POST') {
        curl_setopt($ch, CURLOPT_POST, true);
        if ($data) {
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        }
    }
    
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    if ($httpCode >= 200 && $httpCode < 300) {
        return json_decode($response, true);
    } else {
        throw new Exception("API request failed with status $httpCode: $response");
    }
}

/**
 * Example 1: Search for properties
 */
function searchProperties($city, $state, $minPrice = null, $maxPrice = null) {
    echo "\n1. Searching for properties in $city, $state...\n";
    
    $payload = [
        'location' => [
            'city' => $city,
            'state' => $state,
            'radius_miles' => 5
        ],
        'filters' => [
            'property_type' => ['single_family']
        ],
        'sort' => [
            'field' => 'price',
            'order' => 'asc'
        ],
        'pagination' => [
            'limit' => 10
        ]
    ];
    
    // Add price filter if provided
    if ($minPrice || $maxPrice) {
        $payload['filters']['price'] = [];
        if ($minPrice) {
            $payload['filters']['price']['min'] = $minPrice;
        }
        if ($maxPrice) {
            $payload['filters']['price']['max'] = $maxPrice;
        }
    }
    
    try {
        $response = makeApiRequest('POST', '/properties/search', $payload);
        $properties = $response['data']['properties'];
        $totalResults = $response['data']['pagination']['total_results'];
        
        echo "Found $totalResults properties\n";
        
        // Display first property
        if (!empty($properties)) {
            $first = $properties[0];
            echo "\nFirst property:\n";
            echo "Address: " . $first['address']['formatted'] . "\n";
            echo "Price: $" . number_format($first['price']) . "\n";
            echo "Bedrooms: " . $first['details']['bedrooms'] . "\n";
            echo "Bathrooms: " . $first['details']['bathrooms'] . "\n";
            echo "Square Feet: " . number_format($first['details']['square_feet']) . "\n";
        }
        
        return $response;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
        return null;
    }
}

/**
 * Example 2: Verify an address
 */
function verifyAddress($street, $city, $state, $zip = null) {
    echo "\n2. Verifying address...\n";
    
    $payload = [
        'address' => [
            'street' => $street,
            'city' => $city,
            'state' => $state
        ],
        'options' => [
            'standardize' => true,
            'geocode' => true
        ]
    ];
    
    if ($zip) {
        $payload['address']['zip'] = $zip;
    }
    
    try {
        $response = makeApiRequest('POST', '/addresses/verify', $payload);
        $result = $response['data'];
        
        echo "Valid: " . ($result['is_valid'] ? 'Yes' : 'No') . "\n";
        echo "Confidence Score: " . $result['confidence_score'] . "\n";
        echo "Standardized: " . $result['standardized_address']['formatted'] . "\n";
        
        if (isset($result['geocode'])) {
            echo "Coordinates: " . $result['geocode']['latitude'] . ", " . 
                 $result['geocode']['longitude'] . "\n";
        }
        
        return $result;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
        return null;
    }
}

/**
 * Example 3: Get property details
 */
function getPropertyDetails($propertyId, $includes = []) {
    echo "\n3. Getting property details...\n";
    
    $endpoint = "/properties/$propertyId";
    if (!empty($includes)) {
        $endpoint .= "?include=" . implode(',', $includes);
    }
    
    try {
        $response = makeApiRequest('GET', $endpoint);
        $property = $response['data'];
        
        echo "Address: " . $property['address']['formatted'] . "\n";
        echo "Property Type: " . $property['property_type'] . "\n";
        echo "Year Built: " . $property['characteristics']['year_built'] . "\n";
        
        if (isset($property['ownership'])) {
            $owners = $property['ownership']['current']['owner_names'];
            echo "Owner(s): " . implode(', ', $owners) . "\n";
        }
        
        if (isset($property['valuation'])) {
            echo "Estimated Value: $" . 
                 number_format($property['valuation']['estimated_value']) . "\n";
        }
        
        return $property;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
        return null;
    }
}

/**
 * Example 4: Get property valuation (AVM)
 */
function getPropertyValuation($address) {
    echo "\n4. Getting property valuation...\n";
    
    $payload = [
        'property' => [
            'address' => $address
        ],
        'valuation_options' => [
            'include_confidence_score' => true,
            'include_value_range' => true,
            'include_comparables' => true
        ]
    ];
    
    try {
        $response = makeApiRequest('POST', '/valuations/avm', $payload);
        $valuation = $response['data']['valuation'];
        
        echo "Estimated Value: $" . number_format($valuation['estimated_value']) . "\n";
        echo "Confidence Score: " . $valuation['confidence_score'] . "\n";
        echo "Value Range: $" . number_format($valuation['value_range']['low']) . 
             " - $" . number_format($valuation['value_range']['high']) . "\n";
        
        return $valuation;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
        return null;
    }
}

/**
 * Example 5: Search MLS listings
 */
function searchMLSListings($city, $state, $minPrice = null, $maxPrice = null) {
    echo "\n5. Searching MLS listings...\n";
    
    $payload = [
        'location' => [
            'city' => $city,
            'state' => $state
        ],
        'filters' => [
            'status' => ['active'],
            'property_type' => ['single_family', 'condo']
        ],
        'sort' => [
            'field' => 'list_date',
            'order' => 'desc'
        ],
        'pagination' => [
            'limit' => 5
        ]
    ];
    
    // Add price filter
    if ($minPrice || $maxPrice) {
        $payload['filters']['price'] = [];
        if ($minPrice) {
            $payload['filters']['price']['min'] = $minPrice;
        }
        if ($maxPrice) {
            $payload['filters']['price']['max'] = $maxPrice;
        }
    }
    
    try {
        $response = makeApiRequest('POST', '/mls/search', $payload);
        $listings = $response['data']['listings'];
        
        echo "Found " . count($listings) . " MLS listings\n";
        
        // Display first listing
        if (!empty($listings)) {
            $first = $listings[0];
            echo "\nFirst listing:\n";
            echo "MLS #: " . $first['mls_number'] . "\n";
            echo "Address: " . $first['address']['street'] . ", " . 
                 $first['address']['city'] . "\n";
            echo "List Price: $" . number_format($first['price']['list_price']) . "\n";
            echo "Status: " . $first['status'] . "\n";
            echo "Days on Market: " . $first['days_on_market'] . "\n";
        }
        
        return $response;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
        return null;
    }
}

/**
 * Example 6: Autocomplete address
 */
function autocompleteAddress($query) {
    echo "\n6. Autocompleting address...\n";
    
    try {
        $endpoint = '/addresses/autocomplete?' . http_build_query([
            'query' => $query,
            'limit' => 5
        ]);
        
        $response = makeApiRequest('GET', $endpoint);
        $suggestions = $response['data']['suggestions'];
        
        echo "Found " . count($suggestions) . " suggestions:\n";
        foreach ($suggestions as $suggestion) {
            echo "- " . $suggestion['address'] . 
                 " (confidence: " . $suggestion['confidence'] . ")\n";
        }
        
        return $suggestions;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
        return null;
    }
}

/**
 * Main function to run examples
 */
function main() {
    echo "RealEstateAPI PHP Examples\n";
    echo "==========================\n";
    
    // Example 1: Search properties
    searchProperties('Austin', 'TX', 300000, 500000);
    
    // Example 2: Verify address
    verifyAddress('123 Main St', 'Austin', 'TX', '78701');
    
    // Example 3: Property valuation
    getPropertyValuation('123 Main St, Austin, TX 78701');
    
    // Example 4: Search MLS
    searchMLSListings('Austin', 'TX', 400000, 600000);
    
    // Example 5: Autocomplete
    autocompleteAddress('123 Main');
    
    // Note: Uncomment to test with real property ID
    // getPropertyDetails('PROP123456', ['ownership', 'tax', 'valuation']);
    
    echo "\nExamples completed!\n";
}

// Run the examples
main();
?>
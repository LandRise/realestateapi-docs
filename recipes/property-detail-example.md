---
title: Property Detail Example
description: Obtain the full property record for any property in the U.S.
hidden: false
recipe:
  color: '#d2c046'
  icon: 🏡
---
```javascript JavaScript
//By address parts
async function searchPropertyDetailByAddressParts(address_parts) {
  try {
    
    let { house, street, city, state, zip } = address_parts;
    
    let search_options = {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': '<<apiKey>>'
      },
      data: {
        house: house,
        street: street,
        city: city,
        state: state,
        zip: zip
      }
    };
    
    const response = await fetch('https://api.realestateapi.com/v2/PropertyDetail', search_options)
        
		const data = await response.json();
   
    return data;
    
  } catch(e) {
    console.error(e);
  }
}

//By full address
async function searchPropertyDetailByFullAddress(full_address) {
  try {
    let search_options = {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': '<<apiKey>>'
      },
      data: {
        address: full_address
      }
    };
    
    
    const response = await fetch('https://api.realestateapi.com/v2/PropertyDetail', search_options)
     
    const data = await response.json();

    return data;
    
  } catch(e) {
    console.error(e);
  }
}


//By property id
async function searchPropertyDetailById(property_id) {
  try {
     
    let search_options = {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': '<<apiKey>>'
      },
      data: {
      	id: property_id
      }
    };
    
    
    const response = await fetch('https://api.realestateapi.com/v2/PropertyDetail', search_options)
    
    const data = await response.json();
    
    return data;
    
  } catch(e) {
    console.error(e);
  }
}
```

```json Response Example
{"success":true}
```

# Searching with Address Parts

<!-- javascript@1-32 -->

To search an address, break it down into its different parts and provide that as the request body.

# Searching with a Property ID

<!-- javascript@62-88 -->

If you are using the Property Detail API to further enrich a single Property Search API result, then you can use the "id" property on that object to search it in this data set.

# Searching with Full Address

<!-- javascript@34-59 -->

If you have a regularly formatted address then you can search this endpoint with it. Missing pieces may lead to lower match rates, so ensure you use the proper validations.

E.g. 123 Main St, Arlington VA 22205
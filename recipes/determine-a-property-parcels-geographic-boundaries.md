---
title: Determine a Property Parcel's Geographic Boundaries
description: >-
  Get the geographic boundaries for the provided property. The results from this
  endpoint will help you overlay properties on Google Maps and other map
  interfaces in your applications
hidden: false
recipe:
  color: '#fde758'
  icon: 🛰️
---
```javascript JavaScript
const axios = require('axios');

async function findPropertyBoundaryByAddressParts(api_input) {
  try {
    
   let url = 'https://api.realestateapi.com/v1/PropertyParcel';
    
   let headers = {
     "Accept": 'application/json',
     "Content-Type": 'application/json',
     "x-api-key": '<Your API Key>'
   }
    
   let { data } = await axios.post(url, input, {headers})
        
   const json = JSON.stringify(data, null, 2);

   return json;
    
  } catch(e) {
    throw e;
  }
}

async function findPropertyBoundaryByFullAddress() {
  try {
    
    
  } catch(e) {
    throw e;
  }
}

async function findPropertyBoundaryByPropertyId() {
  try {
    
    
  } catch(e) {
    throw e;
  }
}


(async () => {
  try {
    
    let input = {
      house: "17",
      street: "Topeka Pass",
      city: "Willingboro",
      state: "NJ",
      zip: "08046"
    }
    
    //let input2 = {
		//	address: '17 Topeka Pass, Willingboro NJ 08046'
    //}
    
    //let input3 = {
    //  id: '<Any "id" value from Property Search API response objects>'
    //}
    
    await findPropertyBoundary(input);
    
    
    
   
  } catch(e) {
    console.error(e);
    
  }
})();
```

# Step 1: Prepare the API Input



There are 3 different ways to call the Property Boundary API: full formatted address, address parts, and property ID.

If you are mapping Property Search API results onto a Google Map or similar interface in an app, then you should use the property "id" field to get their respective latitude/longitude polygon boundaries.

# Step 2: Grab the Important Response Properties



The two most notable fields on this response are latitude, longitude, location, and geometry.

Latitude & Longitude are of type "double" (commonly known as decimals) with 5 digits are precision.

Location represents a GeoPoint object in the format: POINT(-74.875428 40.007765)

The Geometry property represents a GeoPolygon object. This value should be the most helpful in highlighting a specific region with defined boundaries on a map UI inside an application. The format for the polygon is: POLYGON((-74.8752287002844 40.0078993719293, -74.8753018687224 40.0079162935166, -74.8754901445418 40.0079687891152, -74.8756425603638 40.0076462306847, -74.8753422135154 40.0075623549745, -74.8752287002844 40.0078993719293))

# What's Next?



After you are able to retrieve boundaries for your properties from this endpoint, the next step for application developers is to learn how to Drop Pins on a map for these properties or how to Draw Polygons on a map for the boundaries of a property or county.
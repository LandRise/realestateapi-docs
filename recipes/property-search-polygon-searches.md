---
title: 'Property Search: Polygon Searches'
description: Recipe Description
hidden: true
recipe:
  color: '#018FF4'
  icon: 🦉
---
```javascript JavaScript
const axios = require('axios');

async function polygonSearch(coords) {
	try {
    
    let input = [
      { lat: '', lon: '' },
      { lat: '', lon: '' },
      { lat: '', lon: '' },
      { lat: '', lon: '' } 
    ]
    
    //pull back the polygons and geopolygons for the coordinate pairs provided
    axios.post('https://api.realestateapi.com/v2/PropertySearch', body)
    	.then((res) => {
      	//process results
      
      	//example output
      	/*
        	{
          	
          
          
          }
        */
    	})
 
    
  } catch(e) {
    
  }
}
}

async function multiPolygonSearch() {
 	try {
    
  } catch(e) {
    
  }
}




```

```json Response Example
{"success":true}
```

# Single Polygon Search



1. Create an array of objects with latitude and longitude properties named 'lat' and 'lon' respectively.
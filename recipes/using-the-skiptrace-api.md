---
title: Using the SkipTrace API
description: >-
  Need to find contact info for your prospects? This API returns phone numbers,
  emails, social media profiles, and more!
hidden: false
recipe:
  color: '#0efbcc'
  icon: 📞
---
```javascript JavaScript
const axios = require('axios');

async function runSkipTraceSearch(input) {
  try {
    
   let headers = {
   	"Accept": 'application/json',
   	"Content-Type": 'application/json',
   	"x-api-key": '<Your API Key>'
   }
    
   let { data } = await axios.post('https://api.realestateapi.com/v1/SkipTrace', input, {headers})
        
   const json = JSON.stringify(data, null, 2);

   return json;
    
  } catch(e) {
    throw e;
  }
}

(async () => {
  try {
    
    let input = {
    	first_name: '',
    	last_name: '',
    	address: '6806 19th Rd N',
    	city: 'Arlington',
    	state: 'VA',
    	zip: '22205'
    }
    
    await runSkipTraceSearch(input);
    
  } catch(e) {
    console.error(e);
  }
})();
```

```json Response Example
{
  test: true
  
  
}
```

# Step 1: Prepare the Input

<!-- javascript@26-33 -->

The two main components of the SkipTrace API input are the Name & Address. 

The first_name and last_name fields are required. Be careful how your names are formatted, adding initials after the name or providing LLCs in the name fields significantly lowers your chances of an accurate match. 

For the Address component of the input, you can provide either address, city, state, and zip fields together or mail_address, mail_city, mail_state, mail_zip together. You can provide both, but only 1 set of them is required in order to not get a 400 Bad Request error code

# Step 2: Decide on Single or Bulk



If you have more than one Name + Address combination, you can hit this endpoint repeatedly, but as your volume increases you may need to step up and use the Bulk SkipTrace API. But there is additional setup including setting up a webhook to receive responses, so this endpoint is less technically difficult to get up and running.

# What's Next?



Depending on the type of application you are building, you can do different things with the data from this endpoint's responses. 

You can enrich contacts in your CRM, enrich list builder leads with phones and emails, and more.

The responses include phones and emails so they are perfect for B2C communications platforms or data enrichment platforms.

Social media profile links are provided when available. These are perfect for applications focusing on digital marketing and social media ad targeting.
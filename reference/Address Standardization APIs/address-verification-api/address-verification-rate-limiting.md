---
title: Address Verification Rate Limiting
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Address Verification can be used to validate huge lists of addresses, which means you'll need to batch your requests to RealEstateAPI to avoid getting 429 Too Many Requests errors.

Every Address Verification API call can contain up to 100 addresses per call. 

By **x-api-key**: 10 requests / second (up to 1,000 addresses / second )

By **x-user-id**: 3 requests / second (up to 300 addresses / second per x-user-id, if specified)

```
const axios = require('axios');

let url = 'https://api.realestateapi.com/v2/AddressVerification";

let addressVerifyBatches = [
  {
    addresses: [
      { 
        "key": 0,
        "street": "2505 NW 28th Street",
        "city": "Oklahoma City",
        "state": "OK",
        "zip": "73107"
      },
      ...99 more
    ]
	},
  {
    addresses: [
      { 
        "key": 101,
        "street": "2504 NW 28th Street",
        "city": "Oklahoma City",
        "state": "OK",
        "zip": "7310"
      },
      ...99 more
    ] 
  },
  ...998 more (for a total of 1000 batches of 100 addresses)
]

let headers = {
  'x-api-key': "<<Your-API-Key>>",
  //'x-user-id': "testUserId" (only rate limited by if specified)
}


let counter = 0;



setInterval( async () => {
  
  for (let i = 0; i<10; i++) {
    let body = { 
      addresses: addressVerifyBatches[counter].addresses
    }
  
  	let runVerify = await axios.post(url, body, {headers});
    
  	counter++;
  }
  
}, 1000)//in milliseconds 1000ms = 1 second







```

Without observing the rate limits, your batch jobs will start getting response codes such as below. You will get intermittent 429s until your rate window gets clogged up, and then you will receive only 429s.

![](https://files.readme.io/1083d50-Screen_Shot_2023-06-08_at_7.17.18_PM.png)

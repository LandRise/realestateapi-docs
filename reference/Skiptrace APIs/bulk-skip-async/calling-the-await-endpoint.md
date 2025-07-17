---
title: Calling the Await Endpoint
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
```
const axios = require('axios');

(async () => {

    let url = 'https://api.realestateapi.com/v1/SkipTraceBatchAwait';

		let body = {
        skips: [
            {
                "key": "5060072",
                "first_name": "Kathryn",
                "last_name": "King",
                "address": "12013 Stuart Ridge Dr",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "16189301",
                "first_name": "Dorothea",
                "last_name": "Valle",
                "address": "414 Patrick Ln",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "2679105",
                "first_name": "Otmaro",
                "last_name": "Aguirre",
                "address": "1217 Springtide Pl",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "15705054",
                "first_name": "Sandeep",
                "last_name": "Phulluke",
                "address": "1361 Dominion Ridge Ln",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "14572038",
                "first_name": "Gustavo",
                "last_name": "Rivera",
                "address": "1225 Magnolia Ln",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "1961029",
                "first_name": "Christopher",
                "last_name": "Reuter",
                "address": "507 Alabama Dr",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "4845822",
                "first_name": "Gajendra",
                "last_name": "Saud",
                "address": "734 Cordell Way",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "19337352",
                "first_name": "Brian",
                "last_name": "Plunkett",
                "address": "370 Juniper Ct",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "28868422",
                "first_name": "Isam",
                "last_name": "Estwani",
                "address": "12615 Fantasia Dr",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            },
            {
                "key": "21676597",
                "first_name": "Mahabobur",
                "last_name": "Rahman",
                "address": "429 Old Dominion Ave",
                "city": "Herndon",
                "state": "VA",
                "zip": "20170"
            }
        ]
	}
    
  const headers = { "x-api-key": "<Your-API-Key>" };

  const { data } = await axios.post(url, body, { headers });

  const json = JSON.stringify(data, null, 2);

  console.log(json);

})().catch(e => { console.error(e.response.data)});
```

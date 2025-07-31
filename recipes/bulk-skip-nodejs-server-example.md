---
title: Bulk Skip - Node.js Server Example
description: >-
  Node.js/Express.js backend setup including how to call the Bulk SkipTrace API
  and receive your data via a Webhook Server Endpoint that we will post your
  results to as they become available.
hidden: true
recipe:
  color: '#1a1414'
  icon: 🎯
---
```javascript Node.js Server
/*
	Project Structure
		/api
    	/routes
      	/skip
        	index.js
      /webhooks
      	socket.service.js
        
  	package.json (dependencies: express, socket.io)
		server.js
*/


/*
	server.js
*/

//Add Express to your Server
const express = require('express');
const app = express();

//Add Webhook Listener to Server
const server = require('http').Server(app);
const io = require('socket.io')(server, {
    cors: {
        origin: [
            "http://localhost:3000",
            "https://reirail-mobile.herokuapp.com",
            "https://reirail-mobile-next.herokuapp.com",
            "https://reirail-mobile-testing.herokuapp.com",
            "https://reirail-mobile-staging.herokuapp.com",
            "https://reirail-mobile-sockets.herokuapp.com",
            "https://virtual.reirail.com",
            "*"
        ],
        methods: ["GET", "POST"],
        allowedHeaders: ["*"],
        credentials: true
    }
});
const sockets = require('./api/services/sockets.service').init(io);

(async () => {
  	//Basic Express Middleware
  	app.use(express.urlencoded({ limit: '50mb', extended: true }));
    app.use(express.json({ limit: '50mb' }));
  
  	app.use('/api/webhookRouter', require('./api/routes/webhookRouter.router'));
  
  
  	
})();
```

```json Response Example
{"success":true}
```

# Before You Get Started...

<!-- javascript@1-12 -->

This example will be a walkthrough of a simple Node.js app. This app can exist standalone and talk to your main application, but if you are looking to show users results in real time, you'll want to add this setup in order to send them to your UI once they are returned.

# server.js





# Step 2:




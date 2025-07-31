---
title: Bulk SkipTrace Await API
excerpt: >-
  Need to call the Bulk SkipTrace API and don't want to sweat the Webhook setup
  or need to return results directly to the calling thread? Use this endpoint to
  get the identity and demographic data you need and call it via 'await'
  keywords in programming languages that support such syntax.
api:
  file: skiptrace-apis.json
  operationId: bulk-skip-async
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: endpoint
      slug: calling-the-await-endpoint
      title: Calling the Await Endpoint
---
### No Webhooks? No Problem.

The Bulk SkipTrace Await API is built for those who don't want to go through the trouble of setting up a dedicated server that accepts webhook requests or don't want responses returned to a separate thread in their application, but rather directly back to the caller function.

This endpoint has significant performance boosts to calling the single SkipTrace API in a loop, partially due to the number of total network requests your app must make to enrich your data and partially to do with allowing us to still use the critical pieces of our Bulk Skip architecture that make the job most performant.

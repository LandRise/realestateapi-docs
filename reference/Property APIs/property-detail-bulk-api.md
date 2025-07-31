---
title: Property Detail Bulk API
excerpt: >-
  For retrieving of up to 1000 properties at once.  Can be used standalone, but
  it's designed to work together with the Property Search API.  Use this API for
  quickly exporting lists, or bulk search requests for analytics.  Pass in
  addresses, or a list of ID's returned from the Property Search API.
api:
  file: property-apis.json
  operationId: property-detail-bulk-api
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
<HTMLBlock>{`
<div>
  <p style="padding-left: 18px">When running the Property Search API, you can retrieve a count of how many properties fit a certain criteria or by specifying count to be 'false', you can receive a list of those properties. On those property objects, you will find a property with the name "id". The input to this endpoint is an array of at least length 1 (max 1000) of these ids returned from our Property Search API.</p>
</div>

<style></style>
`}</HTMLBlock>

<TutorialTile backgroundColor="#579e86" emoji="🏘️" id="6260990d6fc98e0171e0a10c" link="https://beta.realestateapi.com/v1.0/recipes/its-as-easy-as-two-api-calls" slug="its-as-easy-as-two-api-calls" title="It's as Easy as Two API Calls" />

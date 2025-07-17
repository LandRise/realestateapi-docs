---
title: MLS Number Search
excerpt: Find a specific listing by its unique MLS Number identifier
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
```
{
  mls_number: "123456789"
}
```

**Note**: the "mlsNumber" is different than the "listingId". "mlsNumber" is the official number assigned to a listing by the MLS, our "listingId" is RealEstateAPI's unique ID for the listing. And "id" is the unique ID from the PUBLIC RECORD dataset (Property Detail/Property Search)

All listings from the MLS APIs will have an "mlsNumber" and "listingId" populated, but won't always necessarily have an "id" (when there's no matching county record for a listing address)

This type of search will only return 1 record. You'll see this reflected in the response in the ".data" array only containing 1 object and responseCount equaling 1.
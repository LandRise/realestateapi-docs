---
title: Rate Limiting
excerpt: Usage windows defined Midnight to Midnight UTC
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Property Data APIs Daily Rate Limits

| Endpoint                               | Window Interval | Max Requests      |
| :------------------------------------- | :-------------- | :---------------- |
| Property Search\*                      | 24hrs           | 1,000,000 credits |
| Property Detail / Property Detail Bulk | 24hrs           | 500,000 credits   |

\*doesn't include "count" or "ids\_only" calls

For example, one Property Search API request can bring back up to 250 property record addresses per request. To get to 1,000,000 credits this would take 4,000 requests at the max size. At a "size" of 10 (typical for end user interactive sites), it would be 100,000 requests.

In practice, these limits usually only come up for our Enterprise customers. If you need a higher throughput of request for any reason, contact us at [dev@realestateapi.com](mailto:dev@realestateapi.com) & we can help!

<br />

# Rate Limiting Errors

* if you exceed our rate limits you'll see an error such as:

```
{
  statusCode: 429,
  error: "Too Many Requests",
  message: "You have reached your daily credit limit for this endpoint, please try again later."
}
```

<br />

# SkipTrace APIs Rate Limits

| Endpoint        | Window Interval | Max Requests                      |
| :-------------- | :-------------- | :-------------------------------- |
| /SkipTrace      | 1 second        | 10                                |
| /SkipTraceBatch | 1 second        | 20 (up to 1000 skips per request) |

---
title: Getting More Specific with the SkipTrace API
description: >-
  Step by step walkthrough of the different match settings you can set on the
  SkipTrace and Bulk SkipTrace APIs
hidden: true
recipe:
  color: '#8baac1'
  icon: 🦉
---
```javascript JavaScript

```

```json Response Example
{"success":true}
```

# Step 1: "match_requirements" Schema



If you do not provide a "match_requirements" property on your input to the SkipTrace API, the endpoint will assume that only "phones" is set to true, meaning a given input will only return a match: true if phone numbers are found, excluding any results that only had emails, etc.

The match requirements specified here indicate that I want matches returned when the results

# Step 2: The Operator Field



The difference between "input" and "input2" is the operator field value switching from 'and' to 'or'.

When the value of "operator" is 'and', the SkipTrace API will return a request with match:true if and only if the record we found has both phones AND emails.

When the value of "operator" is 'or', the SkipTrace API will return a request with match:true if the record we found has phones and no emails, emails and no phones, or emails and phones.

# What's Next?



Once you learn how to toggle the match_requirements flags and operator field for the use case of your application, then you'll be able to better filter out the results you want based on what customers are asking for. 

If you have any suggestions for additional match_requirements that would help you build quicker (it can be anything returned in the "Output" of the response), let us know in the Discord!
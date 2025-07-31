---
title: Agent Searches by Email, Phone or AgentID
excerpt: >-
  Use the MLS Search API to find listings for a specific agent based on their
  email address. The API supports searches on both Listing & Seller Agent
  Emails.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Search for Listings by Listing Agent Email

```json
{
  listing_agent_email: "example@gmail.com"
}
```

<br />

## Search for Listings by Selling Agent Email

```json
{
  selling_agent_email: "example@gmail.com"
}
```

<br />

<br />

## Search for Listings by Listing Agent ID

```json
{
  listing_agent_id: "1234567"
}
```

## Search for Listings by Selling Agent ID

```json
{
  selling_agent_id: "1234567"
}
```

<br />

<br />

## Search for Listings by Listing Agent Phone

```json
{
	listing_agent_phone: "5551234567"
}

```

<br />

## Search for Listings by Selling Agent Phone

```json
{
  selling_agent_phone: "5551234567"
}
```
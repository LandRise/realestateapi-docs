# Zapier Integration

Connect RealEstateAPI with thousands of apps using our official Zapier integration. Automate your real estate workflows without writing code.

## Overview

The RealEstateAPI Zapier integration enables you to:

- Automatically import new listings into your CRM
- Send notifications when property prices change
- Create tasks when properties match specific criteria
- Update spreadsheets with property valuations
- Sync property data across multiple platforms

## Available Triggers

### 1. New Property Listing
Triggers when a new property listing matches your criteria.

**Trigger Fields:**
- Location (City, State, ZIP)
- Price Range
- Property Type
- Bedrooms/Bathrooms
- Square Footage
- Features (Pool, Garage, etc.)

**Output Data:**
- Property ID
- Address
- Price
- Property Details
- Listing Date
- Agent Information
- Images

### 2. Property Price Changed
Triggers when a property's price changes.

**Trigger Fields:**
- Specific Property ID (optional)
- Location Filter
- Minimum Price Change
- Change Direction (Increased/Decreased)

**Output Data:**
- Property ID
- Address
- Old Price
- New Price
- Change Amount
- Change Percentage
- Date of Change

### 3. Property Status Changed
Triggers when a property's listing status changes.

**Trigger Fields:**
- Status Types to Monitor
- Location Filter
- Property Types

**Output Data:**
- Property ID
- Address
- Previous Status
- New Status
- Days on Market
- Current Price

### 4. New Valuation Available
Triggers when a new property valuation is completed.

**Output Data:**
- Property ID
- Address
- Estimated Value
- Confidence Score
- Value Range
- Comparable Properties

## Available Actions

### 1. Search Properties
Search for properties based on criteria.

**Input Fields:**
- Location (Required)
- Price Range
- Property Type
- Bedrooms/Bathrooms
- Additional Filters

**Output:**
- List of matching properties
- Total results count

### 2. Get Property Details
Retrieve detailed information about a specific property.

**Input Fields:**
- Property ID or Address (Required)
- Include Options (Ownership, Tax, Sales History)

**Output:**
- Complete property information
- Ownership details
- Tax information
- Sales history

### 3. Get Property Valuation
Get an automated valuation for a property.

**Input Fields:**
- Property Address (Required)
- Include Comparables
- Include Confidence Score

**Output:**
- Estimated Value
- Value Range
- Confidence Score
- Comparable Properties

### 4. Verify Address
Validate and standardize an address.

**Input Fields:**
- Street Address (Required)
- City
- State
- ZIP Code

**Output:**
- Standardized Address
- Validation Status
- Geocode Coordinates
- Delivery Information

### 5. Skip Trace Property Owner
Find property owner contact information.

**Input Fields:**
- Property Address (Required)
- Include Contact Info
- Include Ownership History

**Output:**
- Owner Name
- Phone Numbers
- Email Addresses
- Mailing Address

## Common Zapier Workflows

### 1. CRM Integration

**New Listing → Create CRM Contact**
```
Trigger: New Property Listing (RealEstateAPI)
├── Filter: Price between $300k-$500k
├── Action: Create Contact (HubSpot)
│   ├── Name: Property Address
│   ├── Phone: Agent Phone
│   └── Custom Fields: Property Details
└── Action: Create Deal (HubSpot)
    ├── Deal Name: Property Address
    ├── Amount: List Price
    └── Stage: New Listing
```

### 2. Email Notifications

**Price Change → Send Email**
```
Trigger: Property Price Changed (RealEstateAPI)
├── Filter: Price decreased by >5%
└── Action: Send Email (Gmail)
    ├── To: your@email.com
    ├── Subject: Price Drop Alert: {{address}}
    └── Body: Price reduced from ${{old_price}} to ${{new_price}}
```

### 3. Spreadsheet Tracking

**New Listing → Add to Sheet**
```
Trigger: New Property Listing (RealEstateAPI)
├── Action: Add Row (Google Sheets)
│   ├── Address: {{address}}
│   ├── Price: {{price}}
│   ├── Bedrooms: {{bedrooms}}
│   ├── Bathrooms: {{bathrooms}}
│   └── Date Listed: {{list_date}}
└── Action: Get Property Valuation (RealEstateAPI)
    └── Action: Update Row (Google Sheets)
        └── Estimated Value: {{estimated_value}}
```

### 4. Multi-Platform Sync

**Property Update → Sync Everywhere**
```
Trigger: Property Status Changed (RealEstateAPI)
├── Path A: Status = "Sold"
│   ├── Action: Update Record (Airtable)
│   └── Action: Create Activity (Salesforce)
└── Path B: Status = "Pending"
    ├── Action: Send Slack Message
    └── Action: Create Task (Asana)
```

### 5. Lead Generation

**New Contact → Property Match**
```
Trigger: New Contact (CRM)
├── Action: Search Properties (RealEstateAPI)
│   ├── Location: {{contact.city}}
│   ├── Max Price: {{contact.budget}}
│   └── Bedrooms: {{contact.bedrooms_needed}}
└── Action: Send Email (with matches)
```

## Setting Up the Integration

### Step 1: Connect Your Account

1. Go to [Zapier RealEstateAPI Integration](https://zapier.com/apps/realestateapi)
2. Click "Connect RealEstateAPI"
3. Enter your API Key when prompted
4. Test the connection

### Step 2: Create Your First Zap

1. Click "Make a Zap"
2. Choose RealEstateAPI as your trigger app
3. Select a trigger event
4. Configure trigger settings
5. Test the trigger
6. Add your action app
7. Map the fields
8. Test and turn on your Zap

### Step 3: Advanced Configuration

**Using Filters:**
```
Only continue if...
- Price: (Number) Less than 500000
- Property Type: (Text) Exactly matches: single_family
- Days on Market: (Number) Less than 7
```

**Using Formatter:**
```
Format Currency:
- Input: {{price}}
- To Format: Currency
- Currency: USD

Format Address:
- Input: {{address.street}}, {{address.city}}, {{address.state}}
- Transform: Capitalize Words
```

## Tips and Best Practices

### 1. Optimize Trigger Frequency

- Set appropriate location filters to reduce noise
- Use price ranges to focus on relevant properties
- Configure property type filters

### 2. Handle Rate Limits

- RealEstateAPI Zapier integration handles rate limiting automatically
- For high-volume Zaps, consider using filters to reduce operations
- Batch operations when possible

### 3. Data Formatting

```javascript
// Format price for display
Formatter by Zapier: Number Format
Input: {{price}}
Format: Currency
Decimal Places: 0

// Create property URL
Formatter by Zapier: Text
Transform: Replace
Input: {{property_id}}
Find: PROP
Replace: https://app.realestateapi.com/property/PROP
```

### 4. Error Handling

Set up error notifications:
```
Add Error Handler
├── Send Email on Error
├── Log to Google Sheet
└── Create Support Ticket
```

### 5. Testing Zaps

- Use test data before going live
- Monitor Zap history regularly
- Set up Zapier notifications for failures

## Common Use Cases by Industry

### Real Estate Agents
- Import new listings to CRM
- Alert clients about matching properties
- Track competitor listings
- Generate property reports

### Property Investors
- Monitor price changes in target areas
- Track distressed properties
- Analyze market trends
- Calculate ROI automatically

### Property Managers
- Update property information across platforms
- Track maintenance based on property age
- Monitor rental market rates
- Generate tenant reports

### Mortgage Brokers
- Get property valuations for applications
- Verify property addresses
- Track property sales in service areas
- Generate market reports

## Troubleshooting

### Common Issues

**1. Authentication Failed**
- Verify your API key is correct
- Check if API key has required permissions
- Ensure account is active

**2. No Trigger Data**
- Broaden your search criteria
- Check location spelling
- Verify filter settings

**3. Missing Fields**
- Some fields may be optional
- Use Zapier's default values
- Check field mapping

**4. Rate Limit Errors**
- Reduce Zap frequency
- Add delays between actions
- Contact support for limit increase

## Support

- **Zapier Support**: [help.zapier.com](https://help.zapier.com)
- **RealEstateAPI Support**: support@realestateapi.com
- **Integration Issues**: Include Zap ID in support requests
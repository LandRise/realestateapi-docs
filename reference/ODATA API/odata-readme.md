# Real Estate API OData

An OData to Elasticsearch DSL translator for Real Estate Property Search API. This service allows RESO/OData-compatible clients to query property data stored in Elasticsearch using standard OData syntax.

📖 **For API Users:** See the complete [Developer Guide](./DEVELOPER_GUIDE.md) for detailed integration instructions, authentication, and advanced examples.

## Features

- ✅ **OData Query Support**: $filter, $top, $skip, $orderby, $count
- ✅ **API Key Authentication**: Secure access with x-api-key header
- ✅ **Field Validation**: Validates queries against Elasticsearch index mapping
- ✅ **Advanced Operators**: Supports eq, ne, gt, gte, lt, lte, and, or, not
- ✅ **ODATA Support**: Supports eq, ne, gt, gte, lt, lte, and, or, not
- ✅ **Error Handling**: Verbose 400 responses for invalid fields
- ✅ **RESO Compatibility**: Compatible with RESO/OData clients
- ✅ **Elasticsearch Integration**: Full power of Elasticsearch queries
- ✅ **Response Formatting**: OData-compliant JSON responses

## Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Environment
Copy `.env.example` to `.env` and configure your Elasticsearch settings:

```bash
cp .env.example .env
```

Edit `.env`:
```env
ELASTIC_URL=https://your-elasticsearch-cluster.com:9200
ELASTIC_API_KEY=your-api-key-here
PROPERTY_DETAIL_INDEX=property_detail_v12
VALID_API_KEYS=api-key-1,api-key-2,api-key-3
PORT=3000
NODE_ENV=development
```

### 3. Start the Server
```bash
npm start
```

The API will be available at: `http://localhost:3000`

## Authentication

All API requests require an `x-api-key` header:

```bash
curl -H "x-api-key: your-api-key-here" \
  "http://localhost:3000/PropertySearch/odata?$top=10"
```

**Development API Key:** `demo-api-key-12345` (configured by default)

## API Endpoints

### Main OData Endpoint
```
GET /PropertySearch/odata
```

### Health Check
```
GET /health
```

## Usage Examples

### Basic Property Search
```bash
# Get first 10 properties (requires API key)
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?$top=10"

# Filter by city
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=propertyInfo.address.city eq 'Austin'"

# Filter with pagination and sorting
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=estimatedValue gt 500000&\$top=5&\$orderby=estimatedValue desc"
```

### Advanced Filtering
```bash
# Multiple conditions with AND
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=propertyInfo.bedrooms eq 3 and propertyInfo.bathrooms gt 2"

# Multiple conditions with OR
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=vacant eq true or absenteeOwner eq true"

# Range queries
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=estimatedValue gt 300000 and estimatedValue lt 800000"

# Nested field queries
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=ownerInfo.absenteeOwner eq true and propertyInfo.yearBuilt gt 2000"

# Field-to-field comparisons (top-level)
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=estimatedValue gt mlsListingPrice"

# Nested field-to-field comparisons
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$filter=propertyInfo.bedrooms gt propertyInfo.bathrooms"
```

### Sorting and Pagination
```bash
# Sort by multiple fields
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$orderby=estimatedValue desc,propertyInfo.yearBuilt asc&\$top=10"

# Skip results (pagination)
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$skip=20&\$top=10"

# Get count
curl -H "x-api-key: demo-api-key-12345" \
  "http://localhost:3000/PropertySearch/odata?\$count=true&\$top=5"
```

## Supported OData Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `eq` | Equals | `city eq 'Austin'` |
| `ne` | Not equals | `vacant ne true` |
| `gt` | Greater than | `estimatedValue gt 500000` |
| `gte` | Greater than or equal | `bedrooms gte 3` |
| `lt` | Less than | `yearBuilt lt 2000` |
| `lte` | Less than or equal | `bathrooms lte 2` |
| `and` | Logical AND | `bedrooms eq 3 and bathrooms gt 2` |
| `or` | Logical OR | `vacant eq true or absenteeOwner eq true` |
| `not` | Logical NOT | `not (mlsActive eq true)` |

## Supported OData Query Options

| Option | Description | Example |
|--------|-------------|---------|
| `$filter` | Filter results | `$filter=city eq 'Austin'` |
| `$top` | Limit results (max 1000) | `$top=10` |
| `$skip` | Skip results for pagination | `$skip=20` |
| `$orderby` | Sort results | `$orderby=estimatedValue desc` |
| `$count` | Include total count | `$count=true` |

## Available Fields

The API supports querying on all fields defined in the Elasticsearch property mapping, including:

### Property Details
- `propertyInfo.bedrooms`, `propertyInfo.bathrooms`, `propertyInfo.livingSquareFeet`
- `propertyInfo.yearBuilt`, `propertyInfo.latitude`, `propertyInfo.longitude`
- `propertyInfo.propertyUse`, `propertyInfo.construction`

### Address Information
- `propertyInfo.address.city`, `propertyInfo.address.state`, `propertyInfo.address.zip`
- `propertyInfo.address.county`, `propertyInfo.address.street`

### Owner Information
- `ownerInfo.absenteeOwner`, `ownerInfo.corporateOwned`, `ownerInfo.ownerOccupied`
- `ownerInfo.owner1FirstName`, `ownerInfo.owner1LastName`

### Financial Data
- `estimatedValue`, `estimatedEquity`, `openMortgageBalance`
- `taxInfo.assessedValue`, `taxInfo.marketValue`

### Boolean Flags
- `vacant`, `auction`, `foreclosure`, `highEquity`, `mlsActive`

*For a complete list of available fields, see the field mapping in `lib/field-validator.js`*

## Error Handling

The API returns detailed error messages for invalid queries:

```json
{
  "error": "Invalid field(s) in query",
  "message": "The following fields are not valid",
  "details": {
    "invalidFields": ["invalidFieldName"],
    "availableFields": ["propertyInfo.bedrooms", "propertyInfo.bathrooms", "..."]
  }
}
```

## Response Format

All responses follow OData v4 JSON format:

```json
{
  "@odata.context": "$metadata#PropertySearch",
  "@odata.count": 1234,
  "value": [
    {
      "id": 12345,
      "propertyId": 12345,
      "address": {
        "street": "123 Main St",
        "city": "Austin",
        "state": "TX",
        "zip": "78701"
      },
      "bedrooms": 3,
      "bathrooms": 2.5,
      "estimatedValue": 650000,
      ...
    }
  ]
}
```

## Development

### Run in Development Mode
```bash
npm run dev
```

### Project Structure
```
├── server.js              # Main server file
├── lib/
│   ├── field-validator.js  # Elasticsearch field mapping validation
│   ├── odata-translator.js # OData to Elasticsearch DSL translator
│   └── response-formatter.js # Response formatting logic
├── package.json
├── .env.example
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

ISC License
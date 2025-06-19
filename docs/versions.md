# API Versions

RealEstateAPI follows semantic versioning and maintains multiple API versions to ensure backward compatibility while enabling innovation.

## Current API Versions

| Version | Status | Base URL | Support Until | Documentation |
|---------|--------|----------|---------------|---------------|
| **v3** | 🚀 **Current** | `https://api.realestateapi.com/v3` | Active | [v3 Docs](./v3/api-reference/overview.md) |
| **v2** | ✅ Supported | `https://api.realestateapi.com/v2` | Dec 2025 | [v2 Docs](./v2/api-reference/overview.md) |
| **v1** | ⚠️ Deprecated | `https://api.realestateapi.com/v1` | Dec 2024 | [v1 Docs](./v1/api-reference/overview.md) |

## Choosing the Right Version

### Use v3 (Recommended) if:
- ✅ Starting a new project
- ✅ Want the latest features and performance improvements
- ✅ Need advanced AI capabilities (PropGPT v3)
- ✅ Require enhanced security features
- ✅ Building high-performance applications

### Use v2 if:
- ✅ Have existing v2 integration that works well
- ✅ Need time to plan migration to v3
- ✅ Require stability during development
- ✅ Dependencies don't support v3 features yet

### Avoid v1:
- ❌ No longer receives new features
- ❌ Security updates only until Dec 2024
- ❌ Limited performance compared to newer versions
- ❌ Missing modern API standards

## Version Comparison

### Performance
| Feature | v1 | v2 | v3 |
|---------|----|----|----| 
| Avg Response Time | 800ms | 400ms | 200ms |
| Batch Processing | 100 properties | 1,000 properties | 5,000 properties |
| Rate Limits | 500/hour | 1,000/hour | 10,000/hour |
| Caching | Basic | Advanced | Edge CDN |

### Features
| Feature | v1 | v2 | v3 |
|---------|----|----|----| 
| Property Search | ✅ | ✅ | ✅ Enhanced |
| MLS Data | ✅ | ✅ | ✅ Real-time |
| Skip Tracing | ✅ | ✅ | ✅ ML-powered |
| PropGPT AI | ❌ | ✅ Basic | ✅ Advanced |
| OAuth 2.0 | ❌ | ❌ | ✅ |
| Webhooks | ❌ | ✅ | ✅ Enhanced |
| GraphQL | ❌ | ❌ | ✅ |

### Data Models
| Aspect | v1 | v2 | v3 |
|--------|----|----|----| 
| Response Format | Flat objects | Structured | Normalized |
| Field Naming | Inconsistent | Improved | Standardized |
| Date Format | Strings | ISO strings | ISO timestamps |
| Error Details | Basic | Detailed | Comprehensive |
| Metadata | Minimal | Standard | Rich |

## Migration Paths

### v1 → v3 Migration
For v1 users, we recommend:
1. **Direct migration to v3** (recommended)
2. **Intermediate v2 step** (if complex integration)

Resources:
- [v1 to v3 Migration Guide](./v3/migration/v1-to-v3.md)
- [Migration Assessment Tool](https://tools.realestateapi.com/migrate)

### v2 → v3 Migration
Straightforward migration with:
- [Detailed Migration Guide](./v3/migration/v2-to-v3.md)
- [Field Mapping Tools](https://tools.realestateapi.com/field-mapper)
- [Adapter Libraries](https://github.com/realestateapi/v3-adapters)

## Breaking Changes by Version

### v2 → v3 Breaking Changes
- **Field names standardized** (e.g., `bedrooms` → `bedroomCount`)
- **Nested object structure** for related data
- **ISO 8601 timestamps** instead of date strings
- **Enhanced error response format**
- **Authentication header changes** (OAuth support)

### v1 → v2 Breaking Changes
- **Response structure standardization**
- **Consistent error codes**
- **Rate limiting changes**
- **Deprecated endpoints removed**

## Version Selection in Code

### JavaScript/Node.js
```javascript
// v3 (Recommended)
import { RealEstateAPIv3 } from '@realestateapi/sdk';
const api = new RealEstateAPIv3({ 
  apiKey: 'your-key',
  version: 'v3' // Optional, defaults to latest
});

// v2 (Legacy support)
import { RealEstateAPIv2 } from '@realestateapi/sdk';
const api = new RealEstateAPIv2({ apiKey: 'your-key' });
```

### Python
```python
# v3 (Recommended)
from realestateapi.v3 import RealEstateAPI
api = RealEstateAPI(api_key='your-key')

# v2 (Legacy support)  
from realestateapi.v2 import RealEstateAPI
api = RealEstateAPI(api_key='your-key')
```

### cURL
```bash
# v3
curl "https://api.realestateapi.com/v3/properties/search" \
  -H "X-API-Key: your-key"

# v2
curl "https://api.realestateapi.com/v2/PropertySearch" \
  -H "X-API-Key: your-key"
```

## Version Support Policy

### Support Lifecycle
1. **Active Development** (18 months)
   - New features added
   - Performance improvements
   - Bug fixes and security updates

2. **Maintenance Mode** (12 months)
   - Critical bug fixes only
   - Security updates
   - No new features

3. **End of Life** 
   - No further updates
   - Documentation archived
   - Migration support available

### Notification Timeline
- **18 months before EOL**: First deprecation notice
- **12 months before EOL**: Maintenance mode begins
- **6 months before EOL**: Final migration deadline notice
- **3 months before EOL**: Weekly reminder emails
- **1 month before EOL**: Daily reminder emails

## Getting Support

### Version-Specific Support
- **v3 Support**: v3-support@realestateapi.com
- **v2 Support**: v2-support@realestateapi.com  
- **Migration Help**: migration@realestateapi.com

### Community
- **Discord**: Version-specific channels
- **Stack Overflow**: Tag with version (e.g., `realestateapi-v3`)
- **GitHub**: Version-specific repositories

### Resources
- [Migration Calculator](https://tools.realestateapi.com/migration-cost)
- [Version Comparison Tool](https://tools.realestateapi.com/version-compare)
- [Feature Roadmap](https://roadmap.realestateapi.com)

---

**Questions?** Contact our Developer Success team at developers@realestateapi.com
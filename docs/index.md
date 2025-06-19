# RealEstateAPI Documentation

Welcome to the comprehensive documentation for RealEstateAPI - the leading real estate data platform with AI-powered features.

## Choose Your API Version

<div class="version-selector">
  <div class="version-card current">
    <h3>🚀 v3 - Current</h3>
    <p>Latest features, best performance, AI-powered</p>
    <ul>
      <li>50% faster response times</li>
      <li>Enhanced PropGPT AI</li>
      <li>OAuth 2.0 support</li>
      <li>Improved data models</li>
      <li>ML-powered analytics</li>
    </ul>
    <a href="./v3/api-reference/overview" class="btn-primary">Get Started with v3</a>
  </div>
  
  <div class="version-card supported">
    <h3>✅ v2 - Supported</h3>
    <p>Stable, well-tested, supported until Dec 2025</p>
    <ul>
      <li>Mature and stable</li>
      <li>Comprehensive features</li>
      <li>Wide SDK support</li>
      <li>Migration tools available</li>
    </ul>
    <a href="./v2/api-reference/overview" class="btn-secondary">View v2 Docs</a>
  </div>
  
  <div class="version-card deprecated">
    <h3>⚠️ v1 - Deprecated</h3>
    <p>End of life: December 2024</p>
    <ul>
      <li>Security updates only</li>
      <li>No new features</li>
      <li>Migration required</li>
      <li>Limited support</li>
    </ul>
    <a href="./v1/api-reference/overview" class="btn-tertiary">v1 Reference</a>
  </div>
</div>

## Quick Migration Guide

<div class="migration-guide">
  <h3>🔄 Migrating Between Versions?</h3>
  
  <div class="migration-path">
    <strong>v1 → v3:</strong> <a href="./v3/migration/v1-to-v3">Complete Migration Guide</a>
  </div>
  
  <div class="migration-path">
    <strong>v2 → v3:</strong> <a href="./v3/migration/v2-to-v3">Step-by-step Migration</a>
  </div>
  
  <div class="migration-tools">
    <h4>Migration Tools:</h4>
    <ul>
      <li><a href="https://tools.realestateapi.com/migrate">Migration Assessment Tool</a></li>
      <li><a href="https://tools.realestateapi.com/field-mapper">Field Mapping Tool</a></li>
      <li><a href="https://github.com/realestateapi/v3-adapters">Adapter Libraries</a></li>
    </ul>
  </div>
</div>

## Version Comparison

| Feature | v1 | v2 | v3 |
|---------|----|----|----| 
| **Performance** | 800ms avg | 400ms avg | **200ms avg** |
| **Rate Limits** | 500/hour | 1,000/hour | **10,000/hour** |
| **PropGPT AI** | ❌ | ✅ Basic | **✅ Advanced** |
| **OAuth 2.0** | ❌ | ❌ | **✅** |
| **Batch Size** | 100 properties | 1,000 properties | **5,000 properties** |
| **Support Until** | Dec 2024 | Dec 2025 | **Active** |

## Getting Started

### 1. Choose Your Version
- **New projects**: Start with [v3](./v3/api-reference/overview) for the best experience
- **Existing v2**: Continue with [v2](./v2/api-reference/overview) or plan [migration](./v3/migration/v2-to-v3)
- **Legacy v1**: [Migrate immediately](./v3/migration/v1-to-v3) before EOL

### 2. Get Your API Key
1. Sign up at [RealEstateAPI.com](https://www.realestateapi.com)
2. Choose your plan
3. Generate your API key
4. Start building!

### 3. Explore Examples
- [JavaScript Examples](../examples/) for all versions
- [Python Examples](../examples/) with async support
- [PHP Examples](../examples/) with modern features

## Need Help?

<div class="support-grid">
  <div class="support-option">
    <h4>📚 Documentation</h4>
    <p>Comprehensive guides and API reference</p>
    <a href="./versions">Browse All Versions</a>
  </div>
  
  <div class="support-option">
    <h4>💬 Community</h4>
    <p>Join our developer community</p>
    <a href="https://discord.gg/realestateapi">Discord Server</a>
  </div>
  
  <div class="support-option">
    <h4>📧 Support</h4>
    <p>Get help from our team</p>
    <a href="mailto:support@realestateapi.com">Email Support</a>
  </div>
  
  <div class="support-option">
    <h4>🔄 Migration Help</h4>
    <p>Free migration assistance</p>
    <a href="mailto:migration@realestateapi.com">Migration Support</a>
  </div>
</div>

---

<style>
.version-selector {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.version-card {
  border: 2px solid #e1e5e9;
  border-radius: 8px;
  padding: 1.5rem;
  background: #f8f9fa;
}

.version-card.current {
  border-color: #28a745;
  background: #f8fff9;
}

.version-card.supported {
  border-color: #007bff;
  background: #f8f9ff;
}

.version-card.deprecated {
  border-color: #ffc107;
  background: #fffdf8;
}

.version-card h3 {
  margin-top: 0;
  margin-bottom: 1rem;
}

.version-card ul {
  margin: 1rem 0;
  padding-left: 1.2rem;
}

.version-card li {
  margin-bottom: 0.5rem;
}

.btn-primary, .btn-secondary, .btn-tertiary {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 600;
  text-align: center;
  margin-top: 1rem;
}

.btn-primary {
  background: #28a745;
  color: white;
}

.btn-secondary {
  background: #007bff;
  color: white;
}

.btn-tertiary {
  background: #6c757d;
  color: white;
}

.migration-guide {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 2rem 0;
}

.migration-path {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}

.migration-tools {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #dee2e6;
}

.support-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.support-option {
  text-align: center;
  padding: 1rem;
  border: 1px solid #dee2e6;
  border-radius: 8px;
}

.support-option h4 {
  margin: 0 0 0.5rem 0;
}

.support-option p {
  margin: 0.5rem 0 1rem 0;
  color: #6c757d;
}
</style>
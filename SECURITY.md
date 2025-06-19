# Security Policy

## Supported Versions

We actively maintain and provide security updates for the current version of our documentation.

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |

## Reporting a Vulnerability

We take the security of our documentation and related systems seriously. While this is primarily a documentation repository, we want to ensure all information is accurate and secure.

### What to Report

Please report any of the following:

- **Exposed sensitive information** in documentation or examples
- **Incorrect security guidance** in our documentation
- **Vulnerable code examples** that could lead to security issues
- **Broken authentication examples** or misleading security advice
- **XSS vulnerabilities** in any HTML content
- **Dependency vulnerabilities** in our build process

### How to Report

**For security vulnerabilities, please do NOT open a public issue.**

Instead, please email us at: **security@realestateapi.com**

Include the following information:
- Description of the vulnerability
- Steps to reproduce (if applicable)
- Potential impact
- Suggested fix (if you have one)

### What to Expect

1. **Acknowledgment**: We'll acknowledge receipt of your report within 48 hours
2. **Assessment**: We'll assess the vulnerability and determine severity
3. **Timeline**: We'll provide an estimated timeline for resolution
4. **Resolution**: We'll fix the issue and notify you when it's resolved
5. **Credit**: With your permission, we'll credit you in our security acknowledgments

### Response Times

- **Critical vulnerabilities**: 24-48 hours
- **High severity**: 3-5 business days  
- **Medium/Low severity**: 1-2 weeks

## Security Best Practices for Contributors

When contributing to this repository:

### Code Examples
- **Never include real API keys** in examples
- **Use placeholder values** like `YOUR_API_KEY`
- **Sanitize any sensitive data** in screenshots or logs
- **Review authentication examples** for security best practices

### Documentation
- **Verify security advice** is current and accurate
- **Include security warnings** where appropriate
- **Reference official security documentation** when available
- **Highlight deprecated or insecure practices**

### Development
- **Keep dependencies updated** to patch known vulnerabilities
- **Use secure coding practices** in any scripts or tools
- **Validate external links** don't lead to malicious sites
- **Check for sensitive data** in git history before pushing

## API Security Reminders

This documentation covers the RealEstateAPI. Users should:

- **Protect API keys** and never expose them in client-side code
- **Use HTTPS** for all API requests
- **Implement proper rate limiting** in applications
- **Follow authentication guidelines** exactly as documented
- **Validate all input data** before sending to the API
- **Handle errors securely** without exposing sensitive information

## Scope

This security policy covers:
- Content in this documentation repository
- Code examples and tutorials
- Build and deployment processes
- Security guidance provided in documentation

This policy does NOT cover:
- The RealEstateAPI service itself (report those to security@realestateapi.com)
- Third-party services or tools mentioned in documentation
- User implementations based on our examples

## Updates

This security policy may be updated from time to time. We'll notify the community of significant changes through our usual communication channels.

---

**Last Updated**: December 2024
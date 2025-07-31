# RealEstateAPI Tax Exemption Codes Reference

## Overview

Tax exemption codes in RealEstateAPI identify the type of property tax exemption applied to a real estate property. These single-character codes represent various categories of tax relief based on property use, owner characteristics, or special circumstances.

## Quick Reference

| Code | Description | Category |
|------|-------------|----------|
| 1 | Natural Disaster/Pandemic | Emergency Relief |
| A | Agricultural | Land Use |
| B | Disabled (any) | Personal Status |
| C | Cemetery | Religious/Memorial |
| D | Homestead | Residential |
| E | Tax Exempt/General Exemption | General |
| F | Senior Citizen | Age-Based |
| G | Government | Public Sector |
| H | Historical | Preservation |
| I | Low Income | Economic Status |
| J | Partial Exempt | Partial Relief |
| K | Head of Household | Family Status |
| L | Library/Museum | Educational/Cultural |
| M | Miscellaneous | Other |
| N | Non-profit | Organization Type |
| O | Orphanage | Social Services |
| P | Public Utilities | Infrastructure |
| Q | Charity/Fraternal Org. | Charitable Organizations |
| R | Religious/Church | Religious |
| S | School/College | Educational |
| T | Hospital/Medical | Healthcare |
| U | Redevelopment Agency | Development |
| V | Veteran | Military Service |
| W | Welfare | Social Services |
| X | Railroad | Transportation |
| Y | Native American | Tribal |
| Z | Widow/er | Survivor Status |

## Detailed Code Descriptions

### Emergency and Disaster Relief
**Tax Exemption Code 1 - Natural Disaster/Pandemic**
- Applied to properties affected by natural disasters or pandemic-related hardships
- Temporary exemption typically granted during recovery periods
- Common for flood, fire, earthquake, or pandemic economic impact situations

### Land Use Based Exemptions
**Tax Exemption Code A - Agricultural**
- Properties used primarily for farming, ranching, or agricultural production
- Includes farmland, orchards, livestock operations, and agricultural buildings
- Often requires proof of agricultural use and minimum acreage requirements

### Personal and Family Status Exemptions
**Tax Exemption Code B - Disabled (any)**
- Properties owned by individuals with qualifying disabilities
- Covers physical, mental, or developmental disabilities as defined by local jurisdiction
- May require medical documentation and income limitations

**Tax Exemption Code D - Homestead**
- Primary residence exemption for property owners
- Reduces taxable value of owner-occupied residential properties
- Most common residential tax exemption across jurisdictions

**Tax Exemption Code F - Senior Citizen**
- Age-based exemption typically for property owners 65 years or older
- May include income limitations and residency requirements
- Often combined with other exemptions like homestead

**Tax Exemption Code I - Low Income**
- Income-based exemption for property owners below specified income thresholds
- Requires annual income verification and application renewal
- Thresholds vary by jurisdiction and household size

**Tax Exemption Code K - Head of Household**
- Exemption for single parents or primary household income earners
- May require proof of dependents and income documentation
- Less common than other personal status exemptions

**Tax Exemption Code V - Veteran**
- Military service-based exemption for qualifying veterans
- May include disability requirements or service period specifications
- Often extends to surviving spouses of deceased veterans

**Tax Exemption Code Z - Widow/er**
- Surviving spouse exemption, often continuation of deceased spouse's exemption
- May have time limitations or remarriage restrictions
- Commonly applies to homestead or senior citizen exemptions

### Organizational and Institutional Exemptions
**Tax Exemption Code E - Tax Exempt/General Exemption**
- Broad category for properties with general tax-exempt status
- Catch-all code when specific exemption type doesn't apply
- May indicate federal or state-level exemption

**Tax Exemption Code G - Government**
- Properties owned by federal, state, or local government entities
- Includes office buildings, public facilities, and government-owned land
- Automatically exempt from property taxation

**Tax Exemption Code L - Library/Museum**
- Educational and cultural institutions open to the public
- Includes public and private libraries, museums, and cultural centers
- Must demonstrate public benefit and educational purpose

**Tax Exemption Code N - Non-profit**
- Properties owned by qualified non-profit organizations
- Requires 501(c)(3) or similar tax-exempt status
- Must be used for charitable, educational, or religious purposes

**Tax Exemption Code O - Orphanage**
- Properties used for child care and orphan services
- Includes children's homes, foster care facilities, and youth services
- Must provide documented social services

**Tax Exemption Code Q - Charity/Fraternal Org.**
- Properties owned by charitable organizations and fraternal societies
- Includes community service organizations and membership-based charitable groups
- Must demonstrate charitable purpose and community benefit

**Tax Exemption Code R - Religious/Church**
- Properties used for religious worship and activities
- Includes churches, temples, mosques, synagogues, and religious retreat centers
- Must be used primarily for religious purposes

**Tax Exemption Code S - School/College**
- Educational institutions from elementary through higher education
- Includes public and private schools, colleges, and universities
- Must provide documented educational services

**Tax Exemption Code T - Hospital/Medical**
- Healthcare facilities and medical service providers
- Includes hospitals, clinics, nursing homes, and medical research facilities
- Must provide healthcare services to the community

**Tax Exemption Code W - Welfare**
- Properties used for social welfare and assistance programs
- Includes homeless shelters, food banks, and social service facilities
- Must demonstrate public welfare purpose

### Infrastructure and Utilities
**Tax Exemption Code P - Public Utilities**
- Properties owned by utility companies providing public services
- Includes power plants, water treatment facilities, and transmission infrastructure
- May have special assessment procedures rather than full exemption

**Tax Exemption Code X - Railroad**
- Properties owned by railroad companies for transportation purposes
- Includes rail lines, terminals, and railroad-related infrastructure
- Often subject to special state-level taxation rather than local property tax

### Special Categories
**Tax Exemption Code C - Cemetery**
- Properties used for burial and memorial services
- Includes cemeteries, mausoleums, and memorial gardens
- Must be used primarily for burial purposes

**Tax Exemption Code H - Historical**
- Properties with historical significance or preservation status
- May require listing on historical registry or landmark designation
- Often includes restoration and maintenance requirements

**Tax Exemption Code J - Partial Exempt**
- Properties with partial tax exemption rather than full exemption
- May apply to mixed-use properties or limited exemption programs
- Exemption amount typically specified as percentage or dollar amount

**Tax Exemption Code M - Miscellaneous**
- Exemptions that don't fit other specific categories
- Catch-all code for unique or specialized exemption types
- Requires case-by-case evaluation for specific meaning

**Tax Exemption Code U - Redevelopment Agency**
- Properties owned by redevelopment or urban renewal agencies
- Part of economic development and urban improvement programs
- May have time-limited exemptions tied to development goals

**Tax Exemption Code Y - Native American**
- Properties on tribal land or owned by Native American tribes
- Subject to federal and tribal taxation rather than local property tax
- May include individual Native American property owners in some jurisdictions

## Implementation Notes for Developers

### Data Handling
- Tax exemption codes are single-character strings
- Always treat as case-sensitive (uppercase)
- Some properties may have multiple exemption codes
- Codes may vary by jurisdiction and tax year

### Common Use Cases
- Property valuation adjustments
- Tax assessment calculations
- Market analysis and comparables
- Investment property evaluation
- Municipal revenue planning

### API Integration
When working with RealEstateAPI property data, tax exemption codes appear in property detail responses and can be used as search filters. Always validate codes against current jurisdiction-specific implementations as local variations may exist.

### Search and Filtering
Tax exemption codes enable efficient filtering for:
- Investment analysis (identifying tax-advantaged properties)
- Market research (understanding exemption patterns)
- Compliance verification (confirming exemption status)
- Portfolio management (tracking exemption benefits)
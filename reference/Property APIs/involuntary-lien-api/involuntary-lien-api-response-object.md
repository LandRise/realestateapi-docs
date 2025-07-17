---
title: Involuntary Lien API Response Object
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Sample of Full Response Object

```
{
  liens: [
    {
      amount: '3993',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2019-03-15',
      releaseDate: '',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Active'
    },
    {
      amount: '1754',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2018-09-24',
      releaseDate: '2019-10-14',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Released'
    },
    {
      amount: '1719',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2018-09-19',
      releaseDate: '2018-11-19',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Released'
    },
    {
      amount: '6583',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2018-05-30',
      releaseDate: '',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Active'
    },
    {
      amount: '2491',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2018-04-24',
      releaseDate: '',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Active'
    },
    {
      amount: '512',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2013-04-17',
      releaseDate: '',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Active'
    },
    {
      amount: '1831',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2007-03-27',
      releaseDate: '',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Active'
    },
    {
      amount: '2246.31',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2006-07-26',
      releaseDate: '',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Active'
    },
    {
      amount: '4810.65',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2006-03-14',
      releaseDate: '',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Active'
    },
    {
      amount: '4630.48',
      irsSerialNumber: '',
      judgeVacatedDate: '',
      originFilingDate: '2005-12-21',
      releaseDate: '',
      filingJurisdiction: 'NJ',
      filingJurisdictionName: 'NEW JERSEY',
      filings: [Array],
      creditors: [Array],
      debtors: [Array],
      status: 'Active'
    }
  ],
  property: {
    id: 195765153,
    fips: '34013',
    apn: '17  06003-0000-00020',
    address: 'XXX EXAMPLE ST, ANYCITY, NJ 07050-1232',
    useCode: '1001',
    useCodeDescription: 'Single Family Residential',
    owner: 'REDACTED, REDACTED & REDACTED'
  }
}
```

<br />

## Sample "filings" Object

```
{
    agencyName: 'ESSEX COUNTY SPECIAL CIVIL PART',
    agencyCounty: 'ESSEX',
    agencyState: 'NJ',
    filingDate: '2019-03-15',
    filingNumber: 'DC00474319',
    filingType: 'CIVIL NEW FILING'
}
```

<br />

<br />

## Sample "creditors" Object

```
{ 
  name: 'PORTFOLIO RECOVERY ASSOCIATES', 
  address: 'PO BOX XXX, ANYCITY, NJ 07083-1975' 
}
```

<br />

<br />

## Sample "debtors" Object

```
{
    name: 'MUNOZ, FIDEL',
    address: 'XXX EXAMPLE ST, ANYCITY, NJ 07050-1232'
}
```

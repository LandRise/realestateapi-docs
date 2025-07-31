---
title: Lien Searches
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Our primary way of searching by lien is via the "tax\_lien" flag.

```
let request = {
 size: 200,
 state: 'CA',
 tax_lien: true  
}
```

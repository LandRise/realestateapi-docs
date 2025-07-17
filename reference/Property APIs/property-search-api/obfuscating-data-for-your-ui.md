---
title: Obfuscating Data for your UI
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
The "obfuscate" flag is primarily for the purpose of showing application users some but not all relevant bits of information to create an access barrier in order to drive paid data purchasing.

```
let request = {
	size: 250,
  obfuscate: true,
  city: 'Arlington',
  state: 'VA'
}

```

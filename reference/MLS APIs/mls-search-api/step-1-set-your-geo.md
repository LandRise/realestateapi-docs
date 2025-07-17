---
title: 'Step 1: Set your Geo(s)'
deprecated: false
hidden: false
metadata:
  robots: index
---
## MLS Board Codes

* mls\_board\_code \[string] or \[array of strings]

```json
//Single MLS Board Code
{
  "city": "Richmond",
	"state": "VA",
	"active": true,
	"mls_board_code": "mdbmls-r"
}


//Multiple MLS Board Codes
{
  "city": "Richmond",
	"state": "VA",
  "active": true,
	"mls_board_code": ["mdbmls-r", "ohneoh", "scctmls"]
}

```

<br />

## Zip

* zip \[string] or \[array of strings]

```json
{
  zip: "22205",
	active: true
}

--OR--

{
	active: true,
  zip: ["22205", "20301"]
}



```

<br />

## City, County,

city \[string]

county \[string]

```json
//City Example
{
  city: "Arlington",
  state: "VA",
	active: true
}

//County Example
{
  county: "Henrico",
  state: "VA",
	active: true
}


//Multiple Cities / Counties - use Compound Queries
{
	active: true,
  "and": [
    {
      "or": [
        {
          "city": "Richmond", state: "VA"
        },
        {
          "city": "Farmville", state: "VA"
        },
        {
          "city": "Arlington", state: "VA"
        },
        {
          "county": "Henrico", state: "VA"
        }
      ]
		}
}

```

<br />

## Search Radius

* "radius" works with "latitude"/"longitude", "address", "id" and "listing\_id"

```json
//Around an address
{
  address: "6806 19th Rd N, Arlington, VA 22205",
	active: true,
	radius: 2
}

//Around a latitude/longitude coordinate pair
{
  latitude: "38.885980589900285",
	longitude: "-77.15999383193586",
	active: true,
	radius: 2
}
```

<br />

## Polygon / Multiple Polygons

```
//Single Polygon
{
  active: true,
  polygon: [
    {lat: "", lon: ""},
    {lat: "", lon: ""},
    {lat: "", lon: ""}
	]
}

//Multiple Polygons
{
  active: true,
  multi_polygon: [ 
			[
        {lat: "", lon: ""},
        {lat: "", lon: ""},
        {lat: "", lon: ""}	
      ],
			[
        {lat: "", lon: ""},
        {lat: "", lon: ""},
        {lat: "", lon: ""}	
      ]
}
```
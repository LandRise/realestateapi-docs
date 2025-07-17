---
title: Polygon Searches
excerpt: >-
  Use our Property Boundary API, MapBox, GoogleMaps, or other Map APIs together
  with our Property Search API's Polygon and Multi-Polygon Searching
  capabilities to power your Map Based Applications.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
All you need is a set of latitude and longitude points to get started.

### Single Polygon Search

For the polygon geo-points, you can use string or double (floats also accepted) representations for the actual point values. Integers will not be accepted, so make sure to include precision.

```
let request = {
  	"size": 100,
  	"count": false,
    "polygon": [
        {
            "lon": "-86.32762085355883",
            "lat": "35.42300740560803"
        },
        {
            "lon": -86.43359069901402,
            "lat": 35.19184584103132
        },
        {
            "lon": "-86.0572016901352",
            "lat": "35.15490990082178"
        },
        {
            "lon": -86.00921468169653,
            "lat": 35.45088715765438
        },
        {
            "lon": "-86.32762085355883",
            "lat": "35.42300740560803"
        }
  ]
}
```

### Multi-Polygon Search

For multi-polygon searches, the input looks similar, but it consists of an array of polygon objects, instead of an array of geo-point objects.

```
let request = {
  	"size": 100,
  	"count": false,
    "multi_polygon": [
      [ //polygon1
        {
            "lon": "-86.32762085355883",
            "lat": "35.42300740560803"
        },
        {
            "lon": -86.43359069901402,
            "lat": 35.19184584103132
        },
        {
            "lon": "-86.0572016901352",
            "lat": "35.15490990082178"
        },
        {
            "lon": -86.00921468169653,
            "lat": 35.45088715765438
        },
        {
            "lon": "-86.32762085355883",
            "lat": "35.42300740560803"
        }
			],
      [ //polygon2
        ... another polygon object
      ]
  ]
}
```

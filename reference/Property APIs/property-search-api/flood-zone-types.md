---
title: Flood Zone Types
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
| Flood Zone Code         |                                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Low Risk**            |                                                                                                                                                                                                                                                                                                                                                                   |
| ["B", "X"]              | Area of moderate flood hazard, usually the area between the limits of the 100--year and 500-year floods. B Zones are also used to designate base floodplains of lesser hazards, such as areas protected by levees from 100-year flood, or shallow flooding areas with average depths of less than one foot or drainage areas less than 1 sq. mile.                   |
| ["C", "X"]              | Area of minimal flood hazard, usually depicted on FIRMs as above the 5-year flood level. Zone C may have ponding and local drainage problems that don't warrant a detailed study or designation as base floodplain. Zone X is the area determined to be outside the 500-year flood and protected by levee from 100-year flood.                                         |
|                         |                                                                                                                                                                                                                                                                                                                                                                   |
|                         |                                                                                                                                                                                                                                                                                                                                                                   |
| **High Risk**           |                                                                                                                                                                                                                                                                                                                                                                   |
| A                       | Areas with a 1% annual chance of flooding and a 26% chance of flooding over the life of a 30-year mortgage. Because detailed analyses are not performed for such areas, no depths or base flood elevations are shown within these zones.                                                                                                                            |
| AE                      | The base floodplain where base flood elevations are provided. AE Zones are now used on new format FIRMs instead of A1-A30 Zones.                                                                                                                                                                                                                                  |
| A1-A30                  | These are known as numbered A Zones (e.g., A7 or A14). This is the base floodplain where the FIRM shows a BFE (old format).                                                                                                                                                                                                                                       |
| AH                      | Areas with a 1% annual chance of shallow flooding, usually in the form of a pond, with an average depth ranging from 1 to 3 feet. These areas have a 26% chance of flooding over the life of a 30-year mortgage. Base flood elevation derived from detailed analyses are shown at selected intervals within these zones.                                            |
| AO                      | River or stream flood hazard areas, and areas with a 1% or greater chance of shallow flooding each year, usually in the form of sheet flow, with an average depth ranging from 1 to 3 feet. These areas have a 26% chance of flooding over the life of a 30-year mortgage. Average flood depths derived from detailed analyses are shown within these zones.         |
| AR                      | Areas with a temporarily increased flood risk due to the building or restoration of a flood control system (such as a levee or a dam). Mandatory flood insurance purchase requirements will apply, but rates will not exceed the rates for unnumbered A zones if the structure is built or restored in compliance with Zone AR floodplain management regulations. |
| A99                     | Areas with a 1% annual chance of flooding that will be protected by a Federal flood control system where construction has reached specified legal requirements. No depths or base flood elevations are shown within these zones.                                                                                                                                  |
|                         |                                                                                                                                                                                                                                                                                                                                                                   |
| **Coastal & High Risk** |                                                                                                                                                                                                                                                                                                                                                                   |
| V                       | Coastal areas with a 1% or greater chance of flooding and an additional hazard associated with storm wave. These areas have 26% chance of flooding over the life of a 30-year mortgage. No base flood elevations are shown within these zones.                                                                                                                    |
| VE, V1 - V30            | Coastal areas with a 1% or greater chance of flooding and an additional hazard associated with storm waves. These areas have a 26% chance of flooding over the life of a 30-year mortgage. Base flood elevations derived from detailed analyses are shown at selected intervals within these zones.                                                               |
|                         |                                                                                                                                                                                                                                                                                                                                                                   |
| D                       | Undetermined risk areas                                                                                                                                                                                                                                                                                                                                           |

### FloodZone Example

```
{
  size: 250,
  flood_zone: true,
  flood_zone_type: 'V',
  city: 'Orlando',
  state: 'FL'
}

//--OR--//

{
  size: 100,
  flood_zone: true,
  flood_zone_type: ['B', 'X'],
  city: 'Cedar Rapids',
  state: 'IA'
}
```
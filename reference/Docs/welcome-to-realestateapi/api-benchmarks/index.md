---
title: Super Speedy APIs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
### Property Search

Our Property Search API is super diverse and flexible in how it allows you to search for properties. And given how important it is in application and UI development to generate the best user experience with less than 1sec lags, APIs must be their most performant selves.

Due to the multitude of ways you can call Property Search, it is important to note the different time scales you are dealing with when building your apps and design accordingly. The more properties you pull back, or the more complex your search, the longer your request can take. However, our APIs are still the fastest around. Don't believe us? Make a few test calls in the API Reference and see how lightning quick it is (all under 1 second!)

These benchmark tables are meant to serve as a guide to expected wait times that you will encounter in your systems when calling our services.

- For more info on how to implement paging, please visit:

<TutorialTile backgroundColor="#d3d7d9" emoji="🔁" id="626098a86ebcf6008642711c" link="https://beta.realestateapi.com/v1.0/recipes/property-search-paging-example" slug="property-search-paging-example" title="Property Search: Paging Example" />

| The Different Cases                              | Avg. Runtime For Basic Filters (in milliseconds) | Count Queries (Avg.)      | Count Queries (Median) | Ids Only Searches (Avg.)    | Ids Only (Median)          |
| :----------------------------------------------- | :----------------------------------------------- | :------------------------ | :--------------------- | :-------------------------- | :------------------------- |
| Random aggregation of 10,000's of live requests  | 129.82—267.07ms (0.130-0.267 secs)               | **167.83ms (0.168 secs)** | **95 ms (0.095 secs)** | 99.202 ms (0.099 secs)      | 124 ms (0.124 secs)        |
| Requests of Size 250                             | 332.81 ms (0.333 secs)                           | —                         | —                      | —                           | —                          |
| Average Time to Complete Requests of Size 1,000  | 343.08 ms (0.343 secs)                           | —                         | —                      | —                           | —                          |
| Average Time to Complete Requests of Size 2,500  | **351.38ms (0.351 secs)**                        | —                         | —                      | —                           | —                          |
| Average Time to Complete Requests of Size 5,000  | **742.25ms (0.742 secs)**                        | —                         | —                      | —                           | —                          |
| Average Time to Complete Requests of Size 10,000 | —                                                | —                         | —                      | **638.551 ms (0.639 secs)** | **315.50 ms (0.316 secs)** |

### Property Search: Other Popular Query Types

|             | Polygon Searches | Multi-Polygon Searches | Search Radius Searches (Average) | Search Radius (Median) | MLS Searches | Sorting | Summary |
| :---------- | :--------------- | :--------------------- | :------------------------------- | :--------------------- | :----------- | :------ | :------ |
| Size 250    | —                | —                      | 248.89ms                         | 238ms                  | \<1s          | —       | —       |
| Size 500    | —                | —                      | —                                | —                      | \<1s          | —       | —       |
| Size 1,000  | —                | —                      | —                                | —                      | \<1s          | —       | —       |
| Size 2,500  | —                | —                      | —                                | —                      | \<1s          | —       | —       |
| Size 5,000  | —                | —                      | —                                | —                      | \<1s          | —       | —       |
| Size 10,000 | —                | —                      | —                                | —                      | \<1s          | —       | —       |

### AutoComplete

|                  | City/State | County | Full Address | Neighborhood | School District | Zip |
| :--------------- | :--------- | :----- | :----------- | :----------- | :-------------- | :-- |
| Time to Complete | —          | —      | —            | —            | —               | —   |

### CSV Generator for Property Search Results

\*avg is between different city/state combos where the total resultCount of the combo was below 10,000 and above 10,000 for searches of size: 10,000. Result counts below 10k lead to faster api call speeds

|                                                | Avg. Time to Complete Job (in milliseconds) |
| :--------------------------------------------- | :------------------------------------------ |
| Acknowledgement Event Message                  | 4ms                                         |
| Time for Bulk Job to Complete (500 records)    | 6984ms                                      |
| Time for Bulk Job to Complete (1,000 records)  | 5958ms                                      |
| Time for Bulk Job to Complete (5,000 records)  | 3714ms                                      |
| Time for Bulk Job to Complete (10,000 records) | 4237ms / 4828ms / 5836ms / 2999ms           |
| Time for Bulk Job to Complete (50,000 records) | —                                           |

### Other Property Endpoints

|                  | Property Detail (Average) | Property Detail (Median) | Property Comps (Average) | Property Comps (Median) | Property Boundary (Average) | Property Boundary (Median) |
| :--------------- | :------------------------ | :----------------------- | :----------------------- | :---------------------- | :-------------------------- | :------------------------- |
| Time to Complete | —                         | —                        | —                        | —                       | —                           | —                          |
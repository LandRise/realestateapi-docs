---
title: Property Search API (COPY)
excerpt: >-
  Searchable API for list building, search counts, and advanced filtering on
  properties.  You can also use this API to implement your own comparables API,
  or property analytics API.  Questions?  Contact our team to ask us for best
  practices with using this API.This API implements easy paging so your apps can
  easily manage filtered results in a results pane with paging.  When your user
  clicks on a result, just use the id from this API to get the full property
  results using the Property Detail API.  Questions on best practices for
  implementing paged property results in your app?  Just contact our team.
api:
  file: property-apis.json
  operationId: property-search-api-copy
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<TutorialTile backgroundColor="#75bdb8" emoji="🔍" id="62609866bd9325002f55f6ae" link="https://developer.realestateapi.com/v1.0/recipes/property-search-build-your-1st-list" slug="property-search-build-your-1st-list" title="Property Search: Build Your 1st List" />

<HTMLBlock>{`
<div>
  <h2><em>Overview</em></h2>
  <div style="padding-left: 15px">
    <p>Are you looking for a general purpose property search API for your product or business? Look no further.</p>
    <p>Our Property Search API gives you the flexibility to search across our national dataset using a variety of optional filtering capabilities.</p>
    <p>This endpoint uses paging for search results that return more than 250 properties.</p>
    <p>Specific Property Search examples can be found on our Postman: <a href="https://postman.com/realestateapis/workspace/realestateapi-property-search-api">Property Search Collections</a></p>
  </div>
</div>

<div>
  
  <div class="geoSelector">
    <h2><em>Geo Selection: <code>city</code>, <code>county</code>, <code>state</code>, <code>zip</code> </em></h2>
    
    <div style="padding-left: 15px">
      <p>The first step to running a Property Search is to specify which geographic locale you would like to perform the search on. There are a variety of ways to combine the filters: </p>
      <ul>
        <li>
          Zip
        </li>
        <li>
          State
        </li>
        <li>
          City + State
        </li>
        <li>
          County + State
        </li>
        <li>
          Zip + City
        </li>
        <li>
          Zip + County
        </li>
        <li>
          City + State + Zip
        </li>
        <li>
          Address only <small>(must be a fully formatted address [e.g. 123 Main St, Arlington VA 22205] -- API will return results matching filters nearest the address provided)</small>
        </li>
      </ul>
    </div>
  </div>
  
  <div>
    <h2><em>Search Radius Settings: <code>radius</code>, <code>latitude</code>, <code>longitude</code> </em></h2>
    
    <div style="padding-left: 15px">
      <p>If you want to get more specific with your search, you can provide a latitude/longitude pair and a search <code>radius</code> (in miles).</p>
    </div>
  </div>
  
  <div>
    <h2><em>Filter Selection</em></h2>
    <div style="padding-left: 15px">
      <p>The second step to defining your search parameters is to choose the filter(s) you would like to use to narrow your search.</p>
      <p>You can use any combination of filters and there is no max amount of filters that can be used, but the more specific the search, the less properties that will likely be returned.</p>
      <p>In the case of some filters such as <code>estimated_equity</code> or <code>equity_percent</code>, you will need to provide additonal values to their accesory <code>operator</code> fields in order to get a <code>200</code> response.</p>
      <p>For the full list of filters, please refer to the accepted parameters to the endpoint below.</p>
  	</div>
  </div>
  
 
  <div>
    <h2><em>Paging</em></h2>
    
    
    <div class="pagingSection">
      <h3><code>count <small>[bool]</small></code></h3>
      <p class="pagingSection">the <code>count</code> property is used to run a query with your given geo & filter choices, but instead of returning the actual property objects it'll return just the number of properties matching your search parameters. This property is required on the request input, so if you want the actual properties make sure to set it to <code>false</code></p>
  	</div>
    
    <div class="pagingSection">
      <h3><code>size <small>[int]</small></code></h3>
      <p class="pagingSection">the <code>size</code> property determines the max amount of results a given query can yield. For very specific geo+filter combinations, the number of results returned in the response (the <code>recordCount</code>) can be lower than the specified size. Since the max search size against this endpoint is 250, you might also need to change the <code>size</code> property between API calls depending on how you implement your paging solution.</p>
    </div>

    <div class="pagingSection">
      <h3><code>resultIndex <small>[int]</small></code></h3>
      <p class="pagingSection">the <code>resultIndex</code> property can be used similar to a cursor. The property's value on each subsequent response will let you know where in the paging process you are. For example, if a specific filter has 1000 results and you are grabbing it in <code>size</code> 100 chunks, the values for the resultIndex will be 0, 100, 200, 300, 400, etc. for the 1st, 2nd, 3rd, 4th API calls, respectively.</p>
    </div>

    <div class="pagingSection">
      <h3><code>recordCount <small>[int]</small></code></h3>
      <p class="pagingSection">the <code>recordCount</code> property will let you know how many records were returned from the most recent Property Search API call. If you specify a <code>size</code> 100 search, the resultCount should also have a value of 100. The only exceptions to this are when <code>resultIndex + size >= resultCount</code> or when not enough properties were found matching your search parameters to fulfill the size on the initial API call.</p>
    </div>

    <div class="pagingSection">
      <h3><code>resultCount <small>[int]</small></code></h3>
      <p class="pagingSection">the <code>resultCount</code> property is used mainly for paging. Based on the search <code>size</code> you provide and the amount of properties you need to return (max of 250 per API call), you will need to write logic using <code>resultIndex</code> and <code>resultCount</code> to page through all results.</p>
    </div>
  </div>
</div>


<style>
.pagingSection {
	padding-left: 18px;
}
.geoSelector > ul {
  padding-left: 50px;
}
</style>
`}</HTMLBlock>

<TutorialTile backgroundColor="#d3d7d9" emoji="🔁" id="626098a86ebcf6008642711c" link="https://developer.realestateapi.com/v1.0/recipes/property-search-paging-example" slug="property-search-paging-example" title="Property Search: Paging Example" />

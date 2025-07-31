---
title: Authentication
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<HTMLBlock>{`
<div>
  <span>RealEstateAPI currently offers one form of authentication:</span><br>
  <ul>
    <li>API Key</li>
  </ul>
</div>

<style>

</style>
`}</HTMLBlock>

## api\_key

For this example you can use the api key `test-[YOUR API KEY]` to test the authorization filters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>

      </th>

      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Security Schema Type
      </td>

      <td>
        API Key
      </td>
    </tr>

    <tr>
      <td>
        Header Parameter Name
      </td>

      <td>
        x-api-key
      </td>
    </tr>
  </tbody>
</Table>

## Using Your API Key

The following is an example of the header object that must be passed along with your API calls. Without properly authenticating using your Skip Engine API Key, you will receive a 401 Error Response from the API. The way that you can add a header to an API call will vary depending on which programming language or interface you choose. For more details on different methods to interact with our API, please continue reading through the Available APIs section: [https://docs.realestateapi.com/docs/available-apis](https://docs.realestateapi.com/docs/available-apis).

<HTMLBlock>{`
<div class="box">
  <p>headers: {<br>
    <span class="field">&nbsp;&nbsp;&nbsp;&nbsp;"x-api-key":"[YOUR API KEY]"<br></span>
    }
  </p>
</div>

<style>
.box {
  border: 1px solid black;
  background-color: black;
  color: white;
  padding-left: 20px;
  padding-top: 20px;
}
  
.field {
  color: rgb(160, 251, 170);
}

</style>
`}</HTMLBlock>

## Test Keys

Using the API key found in your RealEstateAPII account, you can make calls to the API, but take note that you will be charged for any API calls using this key, even if they are test calls run from within these API docs. To avoid being charged while testing out our different endpoints, you can use a test API key.

In order to make your own API key a test API key, all you have to do is just add `test-` before your key like so `test-[YOUR API KEY]` . If you are already logged into Skip Engine, all you have to do is edit your Auth Header in the developer portal and add `test-` as the prefix. To make test API calls now, visit [https://docs.realestateapi.com/reference#append-api-requests](https://docs.realestateapi.com/reference#append-api-requests)

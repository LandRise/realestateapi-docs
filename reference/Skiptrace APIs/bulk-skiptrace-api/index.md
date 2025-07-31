---
title: Bulk SkipTrace API
excerpt: Skiptrace up to 1,000 people in one API call
api:
  file: skiptrace-apis.json
  operationId: bulk-skiptrace-api
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<HTMLBlock>{`
<div>
  <div>
    <h3><em>Overview</em></h3>

    <div style="padding-left: 18px">
      The SkipTraceBatch API will allow you send up to 1,000 skip requests at a single time.<br><br> 

      Benefits of using this API include higher throughput, and a decrease in the likelihood you will receive rate limiting errors.<br><br>

      By using this API, you are able to leverage our queuing architecture which uses a first in - first out queueing strategy.<br><br>
    </div>
  </div>
  
  
  <h3><em>General Endpoint Rules</em></h3>
  
  <ul>
    <li>
      The minimum number of skip request objects you can send is 10.
    </li>
    <li>
      The maximum number of skip request objects you can send is 1,000.
    </li>
    <li>
      The maximum size of the payload is 256KB.  You will receive a <code>400</code> Bad Request response if the payload size is greater than 256KB.
    </li>
    <li>
      <code>key</code> is required for each skip request item in the array of requests. <code>key</code> is an internal number that your system uses to identify and relate each request back to an associated record in your data. <code>key</code> must be unique for each item in the batch. <code>key</code> can be an integer value or a string value.
    </li>
  </ul>

</div>

<style></style>
`}</HTMLBlock>

<HTMLBlock>{`
<div>
  <h2><em>Input</em></h2>
</div>

<div style="padding-left: 18px">
  <div>
  	<h3><code>webcomplete_url</code></h3>
      <ul>
        <li>
          <code>webcomplete_url</code> must be a valid https POST endpoint.  The webhook_url should return a https status of 200.  The response body can be empty.
        </li>
        <li>
          <code>webcomplete_url</code> will be called once after all items in the batch have been processed and sent to your webhook_url. The call to this endpoint will signify that the entire batch has been processed.  It will include statistics about the job such as total match, error, and processed counts.<br>
            <ul>
             <li>
               Note: webcomplete_url is not required.  If a webcomplete_url is not passed, we will not attempt to send a completion message.
             </li>
             <li>
               webcomplete_url will be called with the same x-api-key header and key value so that you can be sure or the origination of the request.
             </li>
            </ul>
        </li>
      </ul>
	</div>
  <div>
    <h3><code>webhook_url</code></h3>
    <ul>
      <li>
        <code>webhook_url</code> must be a valid https POST endpoint.  The webhook_url should return a https status of 200.  The response body can be empty.<br>
        <ul>
         <li>
           <code>webhook_url</code> will be called individually for all items in the batch.  If you pass 1,000 request items, the webhook_url will be called 1,000 times.  It will call your API at most 50 queries per second.  If you need additional throttling, let us know and we can add an additional throttle to slow down calls to your url.
         </li>
         <li>
           <b>New</b>: <code>webhook_url</code> will be called with the same x-api-key header and key value so that you can be sure or the origination of the request.
         </li>
        </ul>
      </li>
      <li>
        You can use different webook_urls per item for additional specification you need.  For instance, you could include a query string with meta data to pass back to your system.
      </li>
    </ul>  
  </div>
  
  
</div>



<style></style>
`}</HTMLBlock>

<HTMLBlock>{`
<div>
  
  <h3><em>Responses</em></h3>
  <hr>
  
	<p style="padding-left: 8px;">
    <em>Initial API Response / Acknowledgement</em><br><br>

    
    <span style="padding-left: 15px;">The Batch request will return an acknowledgement that the batch job has begun.</span><br>

    <div style="padding-left: 20px;">
      <code>batchId</code> is the unique task id in our system that can be used to trace the progress of batch request.<br><br>

      <code>receiveCount</code> is a validator you can use to ensure our system is processing the expected number of transactions based on the unique keys that were sent in the batch.<br><br>

      <code>batchRequestIds</code> is an array of your unique keys along with the associated unique <code>batchRequestId</code> our system generated to track each individual skip trace result in the overall batch.<br><br>
    </div>
      
  	
   
    
  </p>
  <p style="padding-left: 8px;">
		<em>Webhook Responses</em><br>

    <div style="padding-left: 20px;">
      Your <code>webhook_url</code> will be provided a POST request for each item in the batch array will include the <code>batchId</code>, <code>batchRequestId</code>, and the internal <code>key</code> that was provided in the POST body so that you have the best opportunity to match the webhook response to the associated record in your data... as well as validate the overall batch.<br><br>

      Note that <code>key</code> is included in the input object as <code>input.key</code>.<br><br>

      <code>requestId</code> is the id assigned by the skip trace process and returned from the single transaction based /SkipTraceAPI process.<br><br>
		</div>
  </p>
</div>

<style></style>
`}</HTMLBlock>

<TutorialTile backgroundColor="#1a1414" emoji="🎯" id="6269bfdbd77e060091fae0ba" link="https://developer.realestateapi.com/v1.0/recipes/bulk-skip-nodejs-server-example" slug="bulk-skip-nodejs-server-example" title="Bulk Skip - Node.js Server Example" />

---
title: ZohoCRM - RealEstateAPI Zapier Integration
excerpt: Steps on how to integrate Zoho CRM to RealEstateAPI via Zapier
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Step 1: Create a new Zap

* Left side panel click on Zaps

  <Image align="center" width="-1px" src="https://files.readme.io/a8a39e4-image.png" />

* Click on the + Create button

<Image align="center" width="-1px" src="https://files.readme.io/dcd613a-image.png" />

* Select New Zap

  ![](https://files.readme.io/7e7897d-image.png)

* Select the trigger option

![](https://files.readme.io/a57d80e-image.png)

* Search for Zoho then click on it

  ![](https://files.readme.io/27a174e-image.png)

* In the Event field, click the "New lead" to trigger zap whenever there is a new lead input then click on Continue.

  ![](https://files.readme.io/82eb626-image.png)

<br />

## Step 2: Setup and test with your Zoho account

* Make sure that you connect your Zoho account in the next step then click on continue.

  ![](https://files.readme.io/8c3ac73-image.png)

* Test your trigger in the next step

  ![](https://files.readme.io/1f5bf72-image.png)

* It will pull one sample lead that you've created in your Zoho account.\
  Click on the "Continue with the selected record".

  ![](https://files.readme.io/8493d00-image.png)

<br />

## Step 3: Create an Action using RealEstateAPI then test step

* In the next step, select the Action. Type in realestateapi and click on it.

  ![](https://files.readme.io/d13d78e-image.png)

* In the App & event step, select the action that you want to do. Get property detail for your lead in this example.

Click on continue.

![](https://files.readme.io/dad6d14-image.png)

* Next step, make sure that you connect your Reapi account/key to authorize pulling data.

  ![](https://files.readme.io/7a237aa-image.png)

* In the Action step, click on the data field that you'd want to use for getting the property details. In the sample, they are fields that you can find in Zoho. Select address so the zap will always pull information from the address field.

  ![](https://files.readme.io/239a852-image.png)

* Continue then test the step.

  ![](https://files.readme.io/faa4bd7-image.png)

<br />

## Step 4: Create another action to send back details to Zoho

* Adding another step into the Zap will make it possible for the results to actually reflect on your Zoho account.

![](https://files.readme.io/8f91404-image.png)

* Select Zoho as your last Action.

  ![](https://files.readme.io/cd322ae-image.png)

* Select update module entry to update your lead in Zoho.

  ![](https://files.readme.io/d3cbe1b-image.png)

* Use the same account in Zoho for this next step.

  ![](https://files.readme.io/061ba1d-image.png)

* Track the directories that you used in your Zoho account. ( Where is the lead you want to update)

  ![](https://files.readme.io/9d78398-image.png)

* In the Item to be updated, select Custom and click on the "Id" under the New Lead in Zoho CRM option. This way it will always locate the item id that was set up in the initial trigger and then update it.

  ![](https://files.readme.io/c1eeb5e-image.png)

<br />

## Step 5: Edit your Zoho template with your preferred fields

* Create new custom fields inside your Zoho account before moving to the next step. Zoho does not allow adding of new fields if you're on free plan, an account upgrade is required to create custom fields. Here is the link on how you can add them once you've upgraded your account.

  [https://help.zoho.com/portal/en/kb/crm/customize-crm-account/customizing-fields/articles/use-custom-fields#Custom\_Fields](https://help.zoho.com/portal/en/kb/crm/customize-crm-account/customizing-fields/articles/use-custom-fields#Custom_Fields)

  ![](https://files.readme.io/74d65bb-image.png)

* In the same action step, select the items that you want to update on Zoho. In this sample we will input the data inside the "description" part on your Zoho lead. If you want to update the Grantee name based on the pulled property details from REAPI, type in "Grantee Name: " as your identifier and then select Data mortgage history grantee name. Do the same for the other fields that you want to update. Click on continue.

  ![](https://files.readme.io/b1eccdc-image.png)

* Test the step.

  ![](https://files.readme.io/cdecda1-image.png)

* After clicking on "Test step", it should update your lead in Zoho which looks like this since we chose to provide property details on the description field.

  ![](https://files.readme.io/8358ffc-image.png)

* The whole Zapier process should look like this.

  ![](https://files.readme.io/872fe38-image.png)

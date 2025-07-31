---
title: Salesforce - RealEstateAPI Zapier Integration
excerpt: Steps on how to integrate Salesforce CRM to RealEstateAPI via Zapier
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

* Search for Salesforce then click on it

  ![](https://files.readme.io/d4d5108-image.png)

* In the Event field, click the "New Record" to trigger zap whenever there is a new lead input then click on Continue.

  ![](https://files.readme.io/c43e331-image.png)

<br />

## Step 2: Setup and test with your Salesforce account

* Make sure that you connect your Salesforce account in the next step then click on continue.

  ![](https://files.readme.io/c2d40ef-image.png)

* Set the trigger by tracking your leads in your Salesforce account. Select Lead.

  ![](https://files.readme.io/f42a0cd-image.png)

* Test your trigger in the next step

  ![](https://files.readme.io/2387e48-image.png)

* It will pull one sample lead that you've created in your Salesforce account.\
  Click on the "Continue with the selected record".

  ![](https://files.readme.io/6a9aaf1-image.png)

<br />

## Step 3: Create an Action using RealEstateAPI then test step

* In the next step, select the Action. Type in realestateapi and click on it.

  ![](https://files.readme.io/d13d78e-image.png)

* In the App & event step, select the action that you want to do. Get property detail for your lead in this example.

Click on continue.

![](https://files.readme.io/dad6d14-image.png)

* Next step, make sure that you connect your Reapi account/key to authorize pulling data.

  ![](https://files.readme.io/7a237aa-image.png)

* In the Action step, click on the data field that you'd want to use for getting the property details. In the sample, they are fields that you can find in Saleforce. Select address so the zap will always pull information from the address field. Since there is no one liner address in Sales force, you can add them individually (street address, city, state zip code).

  ![](https://files.readme.io/73ae844-image.png)

* Continue then test the step.

  ![](https://files.readme.io/f5e4716-image.png)

<br />

## Step 4: Create another action to send back details to Salesforce

* Adding another step into the Zap will make it possible for the results to actually reflect on your Salesforce account.

  ![](https://files.readme.io/c300765-image.png)

* Select Salesforce as your last Action.

  ![](https://files.readme.io/0dc84e5-image.png)

* Select "Update lead" to update your lead in Salesforce.

  ![](https://files.readme.io/e60a320-image.png)

* Use the same account in Airtable for this next step.

  ![](https://files.readme.io/2b16250-image.png)

* Select the Id of the lead that you want to update. This way it will always locate the Id of your record entry/lead.

  ![](https://files.readme.io/a8be838-image.png)

* In the same action step, select the items that you want to update on Salesforce. You can edit the fields that show up in this section when you're in your Salesforce account. We'll use Bedrooms and Bathrooms information to pull from Reapi and update on Airtable. 

  ![](https://files.readme.io/ec16826-image.png)

  <br />

## Step 5: Edit your Salesforce template with your preferred fields

* Manually add new fields on your Salesforce account before going to the next step. While on your Leads tab, click on Edit object at the upper right corner of your Dashboard.

  ![](https://files.readme.io/7b27579-image.png)

* Select "Fields & Relationships" then click on "New" beside the quick find button.

  ![](https://files.readme.io/a1c421b-image.png)

* Select "Text" for the field type - Name the new fields then complete the set up process by clicking on Next. It may take a few minutes for the new custom fields to show up on the Lead details.

* This is what it looks like inside the sample Salesforce account. Bedroom and Bathroom fields were manually added since we will use them to pull data. You can add more fields here like lot size, estimated equity, garage etc then set them up on Zapier. For now we'll use these two.

![](https://files.readme.io/ca5aad3-image.png)

* Test the step.

  ![](https://files.readme.io/f4a46c3-image.png)

* After clicking on "Test step", it should update your lead in Salesforce which looks like this. It will populate the Bedroom and Bathroom fields. 

  ![](https://files.readme.io/bba2e6a-image.png)

* The whole Zapier process should look like this.

  ![](https://files.readme.io/baed872-image.png)

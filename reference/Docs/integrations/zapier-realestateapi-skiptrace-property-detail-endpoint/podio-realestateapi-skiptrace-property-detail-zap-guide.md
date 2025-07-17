---
title: Podio - RealEstateAPI Skiptrace + Property Detail Zap Guide
excerpt: >-
  Steps on how to integrate Podio CRM to RealEstateAPI via Zapier ( Property
  Detail & Skiptrace  Endpoint )
deprecated: false
hidden: true
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

* Search for Podio then click on it

![](https://files.readme.io/abca99e-image.png)

* In the Event field, click the "New item" to trigger zap whenever there is a new lead input then click on Continue.

![](https://files.readme.io/9e11ef1-image.png)

* Make sure that you connect your Podio account in the next step then click on continue.

  ![](https://files.readme.io/7975a24-image.png)

* Select the organization that you created in your Podio. In this sample it's named "Realestateapi"

  ![](https://files.readme.io/893f38e-image.png)

* You can create several workspaces in Podio, make sure you select the right workspace where you want to update your leads whenever it triggers the zap.

  ![](https://files.readme.io/ee37a7a-image.png)

* Select leads in the Application field.

  ![](https://files.readme.io/44ea6b2-image.png)

* Test your trigger on the next step. It will pull one sample lead that you've created in your Podio account.\
  Click on the "Continue with the selected record".

  ![](https://files.readme.io/0151d36-image.png)

![](https://files.readme.io/bb44da8-image.png)

<br />

<br />

## Step 2: Create an Action using RealEstateAPI then test step (Property Detail)

* In the next step, select the Action. Type in realestateapi and click on it.

  ![](https://files.readme.io/d13d78e-image.png)

* In the App & event step, select the action that you want to do. Get property details for address in this example.

* Click on continue.

* Next step, make sure that you connect your Reapi account/key to authorize pulling data.

  ![](https://files.readme.io/9f7f4cb49aa15e9ef9fb3f83fd1f3678d07016f3571a10fd2da565ac09056f81-image.png)

<br />

* In the Action step, click on the data field that you'd want to use for getting the property details. In the sample, they are fields that you can find in podio. Select address so the zap will always pull information from the address field.

  ![](https://files.readme.io/e0526a6c78f65a09c0acf518f256c822d5a46b9594d13128f338f46adb610ec2-image.png)
* Continue then test the step.

<br />

## Step 3: Create another action using RealEstateAPI ( SkipTrace )

* In the next step, select the Action. Type in realestateapi and click on it.
* In the App & event step, select the action that you want to do. Skip Trace address in this example.
* Click on continue.
* Next step, make sure again that you connect your Reapi account/key to authorize pulling data.

![](https://files.readme.io/813f7e6888fd0eae4c253afc879d23d64c1fb12e9de83475952c191e70dba704-image.png)

<br />

* In the Configure section, click on the data field that you'd want to use for skip tracing. The data can be selected through the fields that you acquired using the property detail endpoint action on your previous step . Select the street address, city, state and zip code so the zap will pull information from those fields.

  ![](https://files.readme.io/bd35bf74a4328e5088a54e2731f0e02c60744834ecc5471e72bcfe3b99945ecc-image.png)

<br />

* Continue then test the step.

<br />

## Step 4: Create a formatter by Zapier action (Phone Numbers)

* Once the address has been skiptraced, Zapier will put the phone number and emails on one field which makes it hard to track on your CRM. This step will separate the phone numbers to be added on your Podio's specified fields.
* Set your Action Event to Utilities.

  ![](https://files.readme.io/82b848212bb1c502285b67a0e3369d8a276504592d65855c101a3d3929f6f410-image.png)
* On the Configure section's Transform field, select Line-Item to Text. 
* For the Values, select the "Output Identity Phones Phone Display" which was the result from the skiptrace
* Type in Comma ( , ) as your Separator then click Continue

  ![](https://files.readme.io/dec33bd69c11e804dab5f6881d16d8d093a372e7664747a7af51440686bb0ea1-image.png)
* Continue then test the step.

## Step 5: Create another formatter by Zapier action (Email Addresses)

* This step will separate the email addresses to be added on your Podio's specified fields.

* Set your Action Event to Utilities.

  ![](https://files.readme.io/82b848212bb1c502285b67a0e3369d8a276504592d65855c101a3d3929f6f410-image.png)

* On the Configure section's Transform field, select Line-Item to Text. 

* For the Values, select the "Output Identity Emails Email" which was the result from the skiptrace

* Type in Comma ( , ) as your Separator then click Continue

  <Image align="center" src="https://files.readme.io/efefcfa97846822af0ef3ce7d182cbf2710f055656ecca6919bc58632cbd7e3f-image.png" />

* Continue then test the step.

## Step 6: Edit your Podio template with your ideal fields

* In your Podio account. you can modify your templates by clicking on "Add Lead" (Upper right corner)  in your Leads tab
* ![](https://files.readme.io/464d72e82a9083d63226ffc0b99b8025f5a212ac54bca8bca883d47fb33f5ed8-image.png)

  Click on Modify Template in the upper left corner

  ![](https://files.readme.io/468a195ba69a92cbdb91deea38b039c7c30d8cf4c2dc33d0c23fb586779c141a-image.png)
* Drag any fields that you prefer from the left side to the right side. In this we added multiple phone number and email address fields.

![](https://files.readme.io/4f6c73301f94c93fe50ae6233a4002b61aff791e6c00471ac37fc87fa9dd5e24-image.png)

* Add more fields for the data that you acquired from your property detail action as well.

  ![](https://files.readme.io/ab3f802f9e5a385a77c882b52bbc59973b1a48f464ce12c9c3f377b0cfcda924-image.png)
* Once that's done, your account is ready to receive the skip traced data from RealEstateAPI

## Step 7: Create another action to send details back to Podio

* This step will pass the skip trace results to your Podio account.
* Select Podio as your App, Action Event - Update Item. Confirm your Account if needed.

![](https://files.readme.io/235f64eee947550306799d781688b7c202024b4787679fcf07479303a2a03375-image.png)

* In the Configure section, select the same directories that was used in the Trigger section.

  ![](https://files.readme.io/69bf9a9-image.png)

  * In the Item to be updated, select Custom and click on the "Item Id". This way it will always locate the item id that was set up in the initial trigger and then update it.

![](https://files.readme.io/dc0849547635927406dc46e0112cea23d95784c1a6bd3b2433d1e694d503c91c-image.png)

* In the same action step, configure field. select the items that you want to update on Podio, for example to update the phone numbers we got from RealEstateAPI, then select Phone 1 and put Output item 1, Phone 2 - Output Item 2 and so on. These are the separated phone numbers produced by the Zapier formatter.

  ![](https://files.readme.io/b9af83df19458c5a0a78c70791495f462d2e3b784180a62f0cf8b15fbf22fcaa-image.png)
* For email addresses, click on Email Address 1 and put in the Output Item 1 that we got from the "Split Emails into Separate Fields" action. Email Address 2 - Output item 2 and so on.

![](https://files.readme.io/fcdaa28e52c7f3cbd11dabb31e376e4303f0dfbde15428560261000e12c9d967-image.png)

* Do the same for the property detail fields that you acquired from the Property detail action.

  ![](https://files.readme.io/86558f279d06631d6b2dcad6f8e10e3ec0ebf3040ac617fd1734a3181161bf40-image.png)
* Continue then test the step.
* That should update your items Podio from this page with blank fields

![](https://files.readme.io/1c6e7ce448a0a72111c6659c0db12a3d1c6a99f25ce4c5894619fed9c2678ae9-image.png)

* Into this page with populated phone numbers, email addresses and property data fields.

  ![](https://files.readme.io/7926befcc69ba28af92ffc67fc5e4715069b32665dba7029d88368f0f913125d-image.png)

<br />

![](https://files.readme.io/9dc0b03b21b6e54f11e5d396fb424d3b3b03cc9778e5108fd68f2266399490ae-image.png)

* All Set! Your whole Zapier Setup should look like this.

![](https://files.readme.io/793e818604f5bbfe9b14d137491d7fa2c73c8da513fc8dae41b223c763d2e043-image.png)

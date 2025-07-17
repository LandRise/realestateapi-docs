---
title: Hubspot - RealEstateAPI Skiptrace Zap Guide
excerpt: Steps on how to integrate Hubspot CRM to RealEstateAPI via Zapier
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

* Search for Hubspot then click on it

  ![](https://files.readme.io/7abe7e6-image.png)

* During Set up in the Trigger event field, click the "New contact" to trigger zap whenever there is a new contact input and make sure that you connect your Hubspot account then click on continue.

  ![](https://files.readme.io/b910343d9725dda8cc59302733b45e425d86bcdcd2005b96df4696dffa90a268-image.png)

* In the configure tab click on "Additional properties to retrieve" then select Contact information: Full address. Click Continue.

  ![](https://files.readme.io/87be010ff88625a581464256102564d15d90284ea96c130b79b75f1bb583997c-image.png)

* It will pull one sample lead that you've created in your Hubspot account as a test.\
  Click on the "Continue with selected record".

![](https://files.readme.io/28c820124c6828f003e8cbf8833ae41543378990b8cfb2ecbe15eac59fdb2bde-image.png)

<br />

## Step 2: Create an action using RealEstateAPI

* In the next step, select the Action. Type in realestateapi and click on it.
* In the App & event step, select the action that you want to do. Skip Trace address in this example.
* Click on continue.
* Next step, make sure again that you connect your Reapi account/key to authorize pulling data.

![](https://files.readme.io/813f7e6888fd0eae4c253afc879d23d64c1fb12e9de83475952c191e70dba704-image.png)

* In the Configure section, click on the data field that you'd want to use for skip tracing. The data can be selected through the fields that you acquired using the property detail endpoint action on your previous step . Select the street address, city, state and zip code so the zap will pull information from those fields.

  ![](https://files.readme.io/28cc253d272dad9b1633531b6d0e5df7d0a3bcfa93141e64f78a147f93e25291-image.png)

* Continue then test the step.

## Step 4: Create a formatter by Zapier action (Phone Numbers)

* Once the address has been skiptraced, Zapier will put the phone number and emails on one field which makes it hard to track on your CRM. This step will separate the phone numbers to be added on your Hubspot's specified fields.
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

## Step 6: Edit your Hubspot template with your ideal fields

* We'll need to add new fields into your Hubspot account before going to the next step. Since we use the Contacts category, go to contacts - click on edit columns at the right side of your screen.

![](https://files.readme.io/2dc7e0d-image.png)

* Click on Create a property. It will direct you to a new page for adding properties.

![](https://files.readme.io/ce8b114-image.png)

* In this sample we'll add phone number. Fill in the required fields on the Details category.

  ![](https://files.readme.io/be3aa2dcf358fd52cc50e8f678c9e107c22de27066eea62e8e597e509ed3bf3b-image.png)
* On the left hand side select field type and set it as phone number. Click on Create on the upper right corner of the page.

![](https://files.readme.io/6a10b45a66feb6f526077a8d02675abd3fb7de3c069c31192d02acf4f8a9d1f7-image.png)

* Once your new property is created, click on any contact in your account (even the trial one) then click on the settings icon just beside Actions.

![](https://files.readme.io/d1d97c32ebd5761bdec1f7a57d74c9ea822e2da4c2bfd79293917e0d532ff057-image.png)

* It will open up the Edit Card menu where you make your newly added properties visible on any contact. For skip tracing you may add multiple phone number and email fields depending on your need (also your hubspot plan).

  ![](https://files.readme.io/cbc5a0f8cfe2c21fb3bd3ba647f00c081350136b01149c1fbeaacc378995fca5-image.png)
* Hit save and check your contact menu if all your preferred fields are visible.

## Step 7: Create another action to send details back to Hubspot

* This step will pass the skip trace results to your Hubspot account.
* Select Hubspot as your App, Action Event - Update Item. Confirm your Account if needed.

![](https://files.readme.io/420ab5e2de8437455d29536f0e534a0573118ee37ed31296d04ed55253f28aa3-image.png)

* In the Configure section, select the object ID of the contact that's being used on the setup . Then choose all the appropriate data results that you want to pass into your Hubspot account.

  ![](https://files.readme.io/e43787c612e1afd44501284b42401d26bfd34cd4479a0290661d12e59809b5f0-image.png)

  <br />
* In the same action step, configure field. select the items that you want to update on Hubspot, for example to update the phone numbers we got from RealEstateAPI, then select Phone 1 and put Output item 1, Phone 2 - Output Item 2 and so on. These are the separated phone numbers produced by the Zapier formatter.

  ![](https://files.readme.io/5a88965c2b0814152189e0891fc1ac1e630281eeb7d2ffdc81260bc1b7099feb-image.png)
* For email addresses, click on Email Address 1 and put in the Output Item 1 that we got from the "Split Emails into Separate Fields" action. Email Address 2 - Output item 2 and so on.

![](https://files.readme.io/f56d2d81953e7e48eb95fa7ed3bd568fbb358faa7968c123be675bfd2279d35e-image.png)

* Do the same for the property detail fields that you acquired from the Property detail action.

![](https://files.readme.io/26957499b2465ec971b398e611cd258f701bbd18916ee9334683734e3a66a54c-image.png)

* Continue then test the step.
* That should update your items Hubspot from this page with blank fields

  ![](https://files.readme.io/6e07daaa1c978747c8b950c7e4fcb1ada95c957d338d79dc552852369160a665-image.png)
* Into this page with populated phone numbers, email addresses and property data fields.

  ![](https://files.readme.io/92ef31d35784151e8bbb7fcf42131bc339b33979e3d97e550cfb64925bda02b7-image.png)
* All Set! Your whole Zapier Setup should look like this.

![](https://files.readme.io/1eb59353c7356c133e74960fc5e13959a7d9d6569fbd2d4716a5d0a7c0d9c3cd-image.png)

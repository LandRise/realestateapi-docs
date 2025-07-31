---
title: Podio - RealEstateAPI Skiptrace Zap Guide
excerpt: Steps on how to integrate Podio CRM to RealEstateAPI via Zapier
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

<br />

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

## Step 2: Create a "Formatter By Zapier" Action (Address Fields)

* Podio by default will read the state field as full input state like "Texas" instead of "TX". Our skiptrace endpoint requires the street address, city, state(abbreviated) and zip to process. This step will take care of the format needed.
* Action - Formatter by Zapier:
* Choose Text > Split Text

  ![](https://files.readme.io/3046e51a884866f609f5f2c2001c60c393167a972b233004afa35d849dd90dff-image.png)
* For the Input, use the full address field from Podio.
* For the Separator, use a comma: ,
* Segment Index: Select All (as Separate Fields)

  ![](https://files.readme.io/e9e85839c744bad065d02e70c72c546ec21798be9db6e507c6fc35258dd50671-image.png)
* Continue then Test step
* This will return output as\
  5722 Vanderbilt Ave\
  Dallas\
  TX 75206

## Step 3: Create another "Formatter By Zapier" Action (State and Zip)

* Text > Split Text

  ![](https://files.readme.io/bcf2406da42cebf96968ed98ec6b894abe06642729ab1d66bae05af9d79ccfdd-image.png)
* Input: the 3rd element from the previous step (TX 75206)
* Separator: space ( )
* Segment Index: All (as Separate Fields)

  ![](https://files.readme.io/ef5f74a4ec79c2f5c7205892e28f7a2bbfc661da3655d5ab20bb7cb6b9d3ebd1-image.png)
* Now we can map these fields for our skip trace endpoint.\
  Street Address: 5722 Vanderbilt Ave\
  City: Dallas\
  State: TX\
  ZIP: 75206

## Step 4: Create an Action using RealEstateAPI then test step

* In the next step, select the Action. Type in realestateapi and click on it.

  ![](https://files.readme.io/d13d78e-image.png)

* In the App & event step, select the action that you want to do. Skip Trace address in this example.

* Click on continue.

* Next step, make sure that you connect your Reapi account/key to authorize pulling data.

  ![](https://files.readme.io/e9c7b48b0fa15938f68b5b6ef5372df547c2c35dbe65bd4e5c422e6ea33c40d6-image.png)

* In the Configure section, click on the data field that you'd want to use for skip tracing. In the sample, they are fields that you can find in podio. Select the street address, city, state(from your formatter) and zip code so the zap will always pull information from those fields. You can also get all the address data from your formatter action except for the state.

  ![](https://files.readme.io/56518c570b6cef7b0f0c473e41023c2ecbf6b96928108b0ac7614ef1de5db931-image.png)

* Continue then test the step.

## Step 5: Create another formatter by Zapier action (Phone Numbers)

* Once the address has been skiptraced, Zapier will again put the phone number and emails on one field which makes it hard to track on your CRM. This step will separate the phone numbers to be added on your Podio's specified fields.
* Set your Action Event to Utilities.

  ![](https://files.readme.io/82b848212bb1c502285b67a0e3369d8a276504592d65855c101a3d3929f6f410-image.png)
* On the Configure section's Transform field, select Line-Item to Text. 
* For the Values, select the Output Identity Phones Phone Display which was the result from the skiptrace
* Type in Comma as your Separator then click Continue

![](https://files.readme.io/51886c80cd6f695af074e2c2490f5d8ffb5d6e53b5ca5ba56276b5f5293c1b82-image.png)

<br />

* Continue then test the step.

<br />

## Step 6: Create another formatter by Zapier action (Email Addresses)

* This step will separate the email addresses to be added on your Podio's specified fields.
* Set your Action Event to Utilities.

  ![](https://files.readme.io/82b848212bb1c502285b67a0e3369d8a276504592d65855c101a3d3929f6f410-image.png)

<br />

* On the Configure section's Transform field, select Line-Item to Text. 
* For the Values, select the Output Identity Emails Email which was the result from the skiptrace
* Type in Comma as your Separator then click Continue

![](https://files.readme.io/9f3a17da7157bcc018b0cddd5f86d1e90d44775961286a96aef3c70491f6af56-image.png)

<br />

* Continue then test the step.

## Step 7: Edit your Podio template with your ideal fields ( If you haven't already )

* In your Podio account. you can modify your templates by clicking on "Add Lead" (Upper right corner)  in your Leads tab
* ![](https://files.readme.io/464d72e82a9083d63226ffc0b99b8025f5a212ac54bca8bca883d47fb33f5ed8-image.png)

  Click on Modify Template in the upper left corner

  ![](https://files.readme.io/468a195ba69a92cbdb91deea38b039c7c30d8cf4c2dc33d0c23fb586779c141a-image.png)
* Drag any fields that you prefer from the left side to the right side. In this we added multiple phone number and email address fields.

![](https://files.readme.io/4f6c73301f94c93fe50ae6233a4002b61aff791e6c00471ac37fc87fa9dd5e24-image.png)

* Once that's done, your account is ready to receive the skip traced data from RealEstateAPI

## Step 8: Create another action to send details back to Podio

* This step will pass the skip trace results to your Podio account.
* Select Podio as your App, Action Event - Update Item. Confirm your Account if needed.

![](https://files.readme.io/235f64eee947550306799d781688b7c202024b4787679fcf07479303a2a03375-image.png)

* In the Configure section, select the same directories that was used in the Trigger section.

  ![](https://files.readme.io/69bf9a9-image.png)

  * In the Item to be updated, select Custom and click on the "Item Id". This way it will always locate the item id that was set up in the initial trigger and then update it.

![](https://files.readme.io/dc0849547635927406dc46e0112cea23d95784c1a6bd3b2433d1e694d503c91c-image.png)

<br />

* In the same action step, configure field. select the items that you want to update on Podio, for example to update the phone numbers we got from RealEstateAPI, then select Phone 1 and put Output item 1, Phone 2 - Output Item 2 and so on

![](https://files.readme.io/6ea82c82e411e2a55d444359d788964413001f08b172c6ac9db809321db42b14-image.png)

* For email addresses, click on Email Address 1 and put in the Output Item 1 that we got from the "Split Emails into Separate Fields" action. Email Address 2 - Output item 2 and so on.

![](https://files.readme.io/fcdaa28e52c7f3cbd11dabb31e376e4303f0dfbde15428560261000e12c9d967-image.png)

<br />

* Continue then test the step.
* That should update your items Podio from this page with blank fields

<br />

![](https://files.readme.io/1c6e7ce448a0a72111c6659c0db12a3d1c6a99f25ce4c5894619fed9c2678ae9-image.png)

* Into this page with populated number and email address fields.

  ![](https://files.readme.io/7926befcc69ba28af92ffc67fc5e4715069b32665dba7029d88368f0f913125d-image.png)

<br />

* All Set! Your whole Zapier Setup should look like this.

![](https://files.readme.io/5a5f3da34d8b438e24e99080d39c20ffce7c12c7c4674386e987a621b3ad13e8-image.png)

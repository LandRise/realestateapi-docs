---
title: Podio - RealEstateAPI Zapier Integrations
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

* In the next step, select the Action. Type in realestateapi and click on it.

  ![](https://files.readme.io/d13d78e-image.png)

* In the App & event step, select the action that you want to do. Get property detail for your lead in this example.

Click on continue.

![](https://files.readme.io/dad6d14-image.png)

* Next step, make sure that you connect your Reapi account/key to authorize pulling data.

  ![](https://files.readme.io/7a237aa-image.png)

* In the Action step, click on the data field that you'd want to use for getting the property details. In the sample, they are fields that you can find in podio. Select address so the zap will always pull information from the address field.

  ![](https://files.readme.io/e428d63-image.png)

* Continue then test the step.

  ![](https://files.readme.io/edb3456-image.png)

* Adding another step into the Zap will make it possible for the results to actually reflect on your Podio account.

![](https://files.readme.io/8f91404-image.png)

* Select Podio as your last Action.

  ![](https://files.readme.io/f834ec1-image.png)

* Select update item to update your lead in Podio.

  ![](https://files.readme.io/a4edcc1-image.png)

* Use the same account in Podio for this next step.

  ![](https://files.readme.io/5fbae67-image.png)

* Select the same directories that was used in the Trigger section.

  ![](https://files.readme.io/69bf9a9-image.png)

* In the Item to be updated, select Custom and click on the "Item Id". This way it will always locate the item id that was set up in the initial trigger and then update it.

  ![](https://files.readme.io/39f5fcb-image.png)

* In the same action step, select the items that you want to update on Podio, for example if you want to update the bedrooms and baths based on the pulled property details from REAPI, then select Data property info Bedrooms and Data property info Bathrooms for each of their respective fields. Click on continue.

  ![](https://files.readme.io/79184e9-image.png)

* Test the step.

  ![](https://files.readme.io/cbab701-image.png)

* After clicking on "Test step", it should update your lead in Podio which looks like this since we chose to provide details specifically for the bedrooms and bathrooms.

  ![](https://files.readme.io/885a84b-image.png)

* The whole Zapier process should look like this.

  ![](https://files.readme.io/fad3b06-image.png)

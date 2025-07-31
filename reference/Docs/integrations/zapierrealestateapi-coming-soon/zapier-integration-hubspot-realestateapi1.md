---
title: Hubspot - RealEstateAPI Zapier Integrations
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

* In the Event field, click the "New contact" to trigger zap whenever there is a new contact input then click on Continue.

  ![](https://files.readme.io/2581310-image.png)

* Make sure that you connect your Hubspot account in the next step then click on continue.

  ![](https://files.readme.io/4122a29-image.png)

* Test your trigger in the next step

  ![](https://files.readme.io/46ba628-image.png)

* It will pull one sample lead that you've created in your Hubspot account.\
  Click on the "Continue with the selected record".

  ![](https://files.readme.io/37954b5-image.png)

* In the next step, select the Action. Type in realestateapi and click on it.

  ![](https://files.readme.io/d13d78e-image.png)

* In the App & event step, select the action that you want to do. Get property detail for your lead in this example.

Click on continue.

![](https://files.readme.io/dad6d14-image.png)

* Next step, make sure that you connect your RealEstateAPI account/key to authorize pulling data.

  ![](https://files.readme.io/7a237aa-image.png)

* In the Action step, click on the data field that you'd want to use for getting the property details. In the sample, they are fields that you can find in Hubspot. Select street address, city, state and postal code so the zap will always pull information from the those fields.

  ![](https://files.readme.io/062048f-image.png)

* Continue then test the step.

  ![](https://files.readme.io/aa8efa2-image.png)

* Adding another step into the Zap will make it possible for the results to actually reflect on your Zoho account.

  ![](https://files.readme.io/fad3aa4-image.png)

* Select Hubspot as your last Action.

  ![](https://files.readme.io/a6c3adf-image.png)

* In the Event field, select update contact to update your lead in Zoho.

  ![](https://files.readme.io/b511181-image.png)

* Use the same account in Hubspot for this next step.

  ![](https://files.readme.io/4748244-image.png)

* In the Item to be updated, select Custom and click on the "Id" under the New Contact in Hubspot CRM option. This way it will always locate the item id that was set up in the initial trigger and then update it.

  ![](https://files.readme.io/2cddbc5-image.png)

* We'll need to add new fields into your Hubspot account before going to the next step. Since we use the Contacts category, go to contacts - click on edit columns at the right side of your screen.

  ![](https://files.readme.io/2dc7e0d-image.png)

  * Click on Create a property

    ![](https://files.readme.io/ce8b114-image.png)

* In this sample we added and used Bathroom and Bedroom fields.

  ![](https://files.readme.io/aed947e-image.png)

* In the same action step, select the items that you want to update on Hubspot. Fill in the fields that we manually added from hubspot and select the appropriate data from the RealEstateAPI data.

  ![](https://files.readme.io/35202d2-image.png)

* Test the step.

  ![](https://files.readme.io/cf97bc5-image.png)

* After clicking on "Test step", it should update your contact in Hubspot which looks like this.

  ![](https://files.readme.io/8242658-image.png)

* The whole Zapier process should look like this.

  ![](https://files.readme.io/1cc3e32-image.png)

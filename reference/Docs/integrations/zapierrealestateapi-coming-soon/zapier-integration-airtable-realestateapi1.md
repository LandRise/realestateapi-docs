---
title: Airtable - RealEstateAPI Zapier Integrations
excerpt: Steps on how to integrate Airtable CRM to RealEstateAPI via Zapier
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

* Select the trigger option.

![](https://files.readme.io/a57d80e-image.png)

* Search for Airtable then click on it

  ![](https://files.readme.io/a11aa9e-image.png)

* In the Event field, click the "New Record" to trigger zap whenever there is a new lead input then click on Continue.

  ![](https://files.readme.io/f1dab23-image.png)

* Make sure that you connect your Airtable account in the next step then click on continue.

  ![](https://files.readme.io/148d5b9-image.png)

* Set the trigger by tracking your leads in your Airtable account. In this sample they are in Lead list (base) - Leads ( table ). Click on continue.

  ![](https://files.readme.io/5fbfd1d-image.png)

* Test your trigger in the next step

  ![](https://files.readme.io/dc99b29-image.png)

* It will pull one sample lead that you've created in your Airtable account.\
  Click on the "Continue with the selected record".

  ![](https://files.readme.io/345bfcf-image.png)

* In the next step, select the Action. Type in RealEstateAPI and click on it.

  ![](https://files.readme.io/d13d78e-image.png)

* In the App & event step, select the action that you want to do. Get property detail for your lead in this example.

Click on continue.

![](https://files.readme.io/dad6d14-image.png)

* Next step, make sure that you connect your RealEstateAPI account/key to authorize pulling data.

  ![](https://files.readme.io/7a237aa-image.png)

* In the Action step, click on the data field that you'd want to use for getting the property details. In the sample, they are fields that you can find in Airtable. Select address so the zap will always pull information from the address field.

  ![](https://files.readme.io/0546f21-image.png)

* Continue then test the step.

  ![](https://files.readme.io/aa9ae16-image.png)

* Adding another step into the Zap will make it possible for the results to actually reflect on your Airtable account.

  ![](https://files.readme.io/9000449-image.png)

* Select Airtable as your last Action.

  ![](https://files.readme.io/8331263-image.png)

* Select update record to update your lead in Airtable

  ![](https://files.readme.io/2eac1cf-image.png)

* Use the same account in Airtable for this next step.

  ![](https://files.readme.io/2b16250-image.png)

* Track the directories that you used in your Airtable account. ( Where is the lead you want to update, same as your initial trigger set up). On the Record field, select the Id of the lead that you want to update. This way it will always locate the Id of your record entry/lead.

  ![](https://files.readme.io/2899b4b-image.png)

* In the Item to be updated, select Custom and click on the "Id" under the New Lead in Zoho CRM option. This way it will always locate the item id that was set up in the initial trigger and then update it.

  ![](https://files.readme.io/c1eeb5e-image.png)

* In the same action step, select the items that you want to update on Airtable. You can edit the fields that show up in this section when you're in your Airtable account. We'll use Bedrooms and Bathrooms information to pull from RealEstateAPI and update on Airtable. 

  ![](https://files.readme.io/283ab9f-image.png)

* Manually add new fields into your Airtable account before going to the next step. While on your Lead list dashboard, click on the + Add field button at the far right side.

  ![](https://files.readme.io/941ba0e-image.png)

  * Name the field ( We'll add Bedroom and Bathroom fields in this sample ). Then select Single line text. Save.

    ![](https://files.readme.io/ac047cf-image.png)

* This is what it looks like inside the sample Airtable account once you've added the Bedroom and Bathroom fields. You can add more fields here like lot size, estimated equity, garage etc then set them up on Zapier. For now we'll use these two.\
  ![](https://files.readme.io/1511ffb-image.png)

* Test the step.

  ![](https://files.readme.io/3ba9fa6-image.png)

* After clicking on "Test step", it should update your lead in Airtable which looks like this. It will populate the Bedroom and Bathroom fields. 

  ![](https://files.readme.io/d904bcf-image.png)

* The whole Zapier process should look like this.

  ![](https://files.readme.io/f706d8c-image.png)

# Edge client with machine certificate authentication

## Overview

In this guide we are checking the steps to use postman collection to configure `BIG-IP Next Access` for VPN using Edge client with machine certificate authentication.

Steps summary, 

1. Update the Postman variables to meet your deployment (Whether via Postman or via CI/CD used flow)
2. Start checking Postman body to meet your requirements as well. 
3. Whether click run to send the postman calls, or run the calls one by one. 


## Update Postman collection variables 

1. Click Import and select the postman collection file downloaded from [Postman collection](https://github.com/f5devcentral/bigip_automation_examples/tree/access-May-1/bigip/bigip_next/next_access/postman_collections). 
2. Once imported, head to variables to update the variable as per your environment. 

![figure](assets/updatevariables.JPG)


## Check Postman body and calls


The collection in question `Machine Tunnel+Cert Authentication`. This one can be used for both use cases Edge client or Machine tunnel, the change will be in altering the matching condition in the advanced resource assignemnt rule. 

![figure](assets/advanceresourcerule.JPG)

1. Login call to request access token which we will make use of in the subsequent calls. 

![figure](assets/logincall.JPG)

2. Policy requirement items for example uploading Trusted CA certificate. 

![figure](assets/uploadcacert.JPG)

3. Create Security policy. 

![figure](assets/createpolicy.JPG)

4. Create application and attach the security policy. 

![figure](assets/createapplication.JPG)

5. Deploy application to the instance with additional parameters if any. 

![figure](assets/deployapp.JPG)


## Run postman calls 


1. The collection in question `Machine Tunnel+Cert Authentication`. This one can be used for both use cases Edge client or Machine tunnel, the change will be in altering the matching condition in the advanced resource assignemnt rule. 

![figure](assets/advanceresourcerule.JPG)

![figure](assets/runcacertcol.JPG)

2. Select the calls to run and adjust settings as needed (Run manually, scheduled or automatically) then hit Run. 

![figure](assets/runcol.JPG)

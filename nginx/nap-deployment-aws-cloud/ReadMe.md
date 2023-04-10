# NGINX App Protect Deployment in AWS Cloud
 
## Overview:
This Repo helps you to deploy the NGINX APP Protect in one click using AWS platform's officially available NGINX AMI's in AWS marketplace.
This will eliminate the need of manually pre building the AMI for our WAF deployment each time and getting the financial benefit of paying as per the usage instead of purchasing a year-long license.

Please refer below devcentral article for detail information,

https://devcentral.f5.com/s/articles/NGINX-App-Protect-Deployment-in-AWS-Cloud.

## Pre-requisites
Clone the Repo locally and update the below listed variables under settings --> Secrets --> Actions --> New repository secrets.
   * AWS_ACCESS_KEY_ID (AWS credentials which you will get under aws --> users -->  Command line or programmatic access info)
   * AWS_SECRET_ACCESS_KEY
   * AWS_SESSION_TOKEN
   * AWS_DEFAULT_REGION
    Note: Above values typically expire in every 12 hours. 
    ![image](https://user-images.githubusercontent.com/6093830/209962425-1c3452ec-9b32-4509-adb5-cc85d4a67a10.png)
   * EC2 key related pem and pub file should be copied to nginx/nap-deployment-aws-cloud/terraform folder
   * Make sure the Arcadia application hosted instance that you mentioned under nginx/nap-deployment-aws-cloud/terraform/nginx.conf is UP and running.
     Note: Arcadia in ohio with 8080, run ./start_arcadia.sh in the instance
   * Update the `ENV` variables in `verified_designs_examples/nginx/nap-deployment-aws-cloud/data/testbed-data.json`
   * Make sure your self hosted runner is installed and added to this repo
   * Make sure `awscli`, `pytest` and other required tools are installed in this private custom runner. Refer `requirements.txt` file for more details

## Steps to run the workflow:
* Navigate to Actions tab in the repository and select the workflow "Deploy Nginx App Protect in AWS" to execute.
* Click on Run workflow on the right side of the UI
### Steps:
![image](https://user-images.githubusercontent.com/39581520/205597185-2b160fb6-65c1-4192-a42d-66fc5f3746fd.png)
### Jobs:
![image](https://user-images.githubusercontent.com/39581520/205597316-d54a7f67-dd3f-4d48-9c64-d810cac43908.png)
### Jobs In-detail:
![image](https://user-images.githubusercontent.com/39581520/205601145-79079495-d8de-490b-ad7a-a5453e086cdf.png)

### Debugging steps:
* No pipeline job is getting executed - Check if self hosted runner is available
* Pipeline fails with credential/token error - Check if credentials are valid and not expired
* Testing job fails - Check if any errors in Testing job failed TC's in Report.html file and rerun testing job
* Deploy job fails with already exists errors - Check if components in this article are not cleaned properly because of some intermittent network issues. If some components are stil available please delete them like VPC or EC2 instance

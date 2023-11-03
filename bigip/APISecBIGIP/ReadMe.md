This project automates all manual testing done as part of https://devcentral.f5.com/s/articles/Protecting-an-API-with-BigIP-WAF. <br />
<br />

**Prerequisites:**
1. Clone the repo locally and update AWS credentials like `access keys`, `secret key` , `EC2_KEY_NAME` and `session token` be in  `settings` --> `Secrets` --> `Actions` section <br />
![image](https://user-images.githubusercontent.com/39581520/212069607-93ae74ee-ecbc-4fb4-bd63-619b777e5506.png)
> Note: Above values typically expire in every 12 hours. If you are not using session token please remove this field accordingly in workflow file step name-`configure aws credentials` in all jobs

2. Bigip password and EC2 keys should be updated properly in `settings` --> `Secrets` --> `Actions` section <br />
> Note: Make sure passwords follow company security standards like alpha numeric, etc. <br />

3. EC2 key related pem and pub file should be copied to bigip/declarative-advanced-waf-policy/terraform folder <br />

4. Make sure you have subscribed to the latest `BIGIP AMI` in AWS account (Sample AMI ID is `ami-0f859d430f5f0ea80`) <br />

5. Update your `ENV` variables in `verified_designs_examples/bigip/APISecBIGIP/data/testbed-data.json` <br />

6. Make sure your self hosted runner is installed and added to this repo <br />

7. Make sure `awscli`, `ansible-playbook`, `pytest` and other required tools are installed in this private custom runner. Refer `requirements.txt` file for more details <br />

> Note: Please install and make sure packages `pytest-html`, `awscli==1.18.105` and `botocore==1.17.28` are available with their correct versions in runner to avoid failures <br />
<br />

**Tools needed:**
1. Terraform - Used for deploying EC2 instances
2. Ansible - Used for deploying AS3 application
3. Python - Used for deploying docker and Arcadia application

**Steps to execute:**
1. Go to `Actions` tab and select your article work-flow - `Deploy API Sec in BIGIP article`
2. Click on `Run Workflow` option and execute it
3. Check the CI/CD jobs execution and check the artifacts if needed <br />
> Note: BIGIP console is available on `https://<bigip-eip>:8443/tmui/login.jsp` and login credentials are `admin` and password provided in `secrets` <br />

**Jobs info in pipeline :**
![image](https://user-images.githubusercontent.com/39581520/212072411-79e1d519-22e3-4946-9140-b8268ad753e2.png)
1. `Deploy` - 
Job will deploy and configure all needed components in AWS like, BIGIP, EC2 instance with Arcadia application, etc.
Tools used - Terraform and Ansible
2. `Testing` -
All valid and illegal traffic will be pushed to the application which is been hosted in AWS EC2 using containers through Virtual server created on BIGIP and all result will be captured.
Tools used - Python requests module and PyTest framework
3. `Destroy` -
This job will destroy all components created for this article.
Tools used - Terraform and Ansible
<br />

**Resources info:**
1. Use existing code using terraform tool to deploy BIGIP, NW's and Docker EC2 machine
2. Use python to deploy Arcadia application as docker containers and expose application port 8080 to port 80 on host
3. Use ansible code to add above created node, Create pool, deploy VS and AS3 security policy in BIGIP
4. Use existing python libs to send illegal traffic to above created VS and validate results

**Test cases planned for automation :**
1. Deploy AS3 security JSON in BigIP
2. Run Securing APIs with BigIP related attacks and validate the result and attch result in TestRail.

**Debugging steps :**
1. No pipeline job is getting executed - Check if self hosted runner is available
2. Pipeline fails with credential/token error - Check if credentials are valid and not expired
3. Testing job fails - Check if any errors in Testing job failed TC's in Report.html file and rerun testing job
4. Deploy job fails with already exists errors - Check if components in this article are not cleaned properly because of some intermittent network issues. If some components are stil available delete them like VPC.
5. Subscription issue with aws ec2 instance, check the subscription status in AWS--> marketplace subscripton--> discovery products--> your ami status.
<br />

**References:**
https://devcentral.f5.com/s/articles/Protecting-an-API-with-BigIP-WAF


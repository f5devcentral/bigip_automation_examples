## Overview

This is a consolidated automation repo for different verified designs customer use case examples available across diversified `F5` products like `BigIP`, `Nginx` and `Distributed cloud`. Users can use this to test a specific use case end to end by using the automation code available in this repo. </br>
</br>
**NOTE: To learn about each use case check the devcentral article link provided in each scenario folder README** </br>
</br>

## Prerequisites

* [F5 Distributed Cloud Account (F5XC)](https://console.ves.volterra.io/signup/usage_plan)
  * [F5XC API certificate](https://docs.cloud.f5.com/docs/how-to/user-mgmt/credentials)
* [AWS Account](https://aws.amazon.com) - Due to the assets being created, free tier will not work.
  * The F5 BIG-IP AMI being used from the [AWS Marketplace](https://aws.amazon.com/marketplace) should be subsribed to your account
  * The F5 Nginx App Protect AMI being used from the [AWS Marketplace](https://aws.amazon.com/marketplace) should be subsribed to your account
  * Please make sure resources like VPC and Elastic IP's are below the threshold limit in that aws region
* [GitHub Account](https://github.com)
* In case of F5 XC use cases, make sure a valid application is available and accessible using public IP (this app is used to test the F5 XC features) 

## Steps to execute

1. Clone the repo locally and update AWS credentials like `access keys`, `secret key` and `session token` be in  `settings` --> `Secrets` --> `Actions` section <br />
![image](https://user-images.githubusercontent.com/6093830/209962425-1c3452ec-9b32-4509-adb5-cc85d4a67a10.png)
> Note: Above values typically expire in every 12 hours. If you are not using session token please remove this field accordingly in workflow file step name-`configure aws credentials` in all jobs

2. Bigip password and EC2 keys should be updated properly in `settings` --> `Secrets` --> `Actions` section <br />
> Note: Make sure passwords follow company security standards like alpha numeric, etc. <br />

3. EC2 key related pem and pub file should be copied to terraform folder in your use case<br />

4. Make sure you have subscribed to the latest `BIGIP AMI` in AWS account (Sample AMI ID is `ami-0f859d430f5f0ea80`) <br />

5. Update your `ENV` variables in `/data/testbed-data.json` file in your use case folder <br />

6. Install self hosted runner and add it to this repo <br />

7. Make sure `awscli`, `kubectl`, `ansible-playbook`, `pytest`, `git` and other required tools are installed in this private custom runner. Refer `requirements.txt` file for more details <br />

> Note: Please install and make sure python packages like `pytest-html`, `awscli==1.18.105` and `botocore==1.17.28` are available with their correct versions in runner to avoid failures <br />

8. If you want to test F5 XC use case, make sure you have valid .p12 extracted cert and key available in use case folder location. Check `terraform.tfvars.json` and update details of your application plublic IP, port, LB dns, etc. <br />

9. Go to `Actions` tab and select your article work-flow <br />

10. Click on `Run Workflow` option and execute it <br />

11. Check the CI/CD jobs execution and check the artifacts for more details <br />
<br />

## Sample resources which are created by terraform
 
1. EKS with name `apisecurity_automation_eks`
2. VPC with name `apisecurity-automation-VPC`
3. EC2 instance with name `apisecurity-automation-BIGIP`
4. EC2 access key with name `automation-key`
5. Auto scaling group with name `apisecurity_automation_eks-*`
6. Network interface with name `BIGIP-Managemt-Interface-0`
7. IAM policies with names `apisecurity_automation_eks-elb-sl-role-creation*`and `apisecurity_automation_eks-deny-log-group*`
8. IAM role with name `apisecurity_automation_eks*`
9. Elastic IP with no name 
10. In case of F5 XC, scripts will create `Origin Pool`, `Load balancer` and `Application Firewall` with names provided in their scripts <br />
<br />


## Support

For support, please open a GitHub issue.  Note, the code in this repository is community supported and is not supported by F5 Networks.  

## Community Code of Conduct

Please refer to the [F5 DevCentral Community Code of Conduct](code_of_conduct.md).

## License

[Apache License 2.0](LICENSE)

## Copyright

Copyright 2014-2023 F5 Networks Inc.

### F5 Networks Contributor License Agreement

Before you start contributing to any project sponsored by F5 Networks, Inc. (F5) on GitHub, you will need to sign a Contributor License Agreement (CLA).

If you are signing as an individual, we recommend that you talk to your employer (if applicable) before signing the CLA since some employment agreements may have restrictions on your contributions to other projects.
Otherwise by submitting a CLA you represent that you are legally entitled to grant the licenses recited therein.

If your employer has rights to intellectual property that you create, such as your contributions, you represent that you have received permission to make contributions on behalf of that employer, that your employer has waived such rights for your contributions, or that your employer has executed a separate CLA with F5.

If you are signing on behalf of a company, you represent that you are legally entitled to grant the license recited therein.
You represent further that each employee of the entity that submits contributions is authorized to submit such contributions on behalf of the entity pursuant to the CLA.

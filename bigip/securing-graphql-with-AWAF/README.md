# Securing-GraphQL-with-Advanced-WAF-declarative-policies

This project automates all manual testing done as part of https://devcentral.f5.com/s/articles/Securing-GraphQL-with-Advanced-WAF-declarative-policies.
Steps to execute this pipeline

Prerequisites:

1. Fork the repo, AWS credentials like `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_SESSION_TOKEN` along with `AWS_DEFAULT_REGION` and `TF_VAR_F5_PASSWORD` should be updated in Github Actions secrets and variables (`Settings->Secrets and variables->Actions->New repository secret`)<br>
2. Make sure passwords follow company security standards like minimum password length, alpha numeric etc.<br>
3. Make sure you have subscribed to the F5 BIGIP AWAF software solution from AWS Marketplace in your AWS account<br>
4. EC2 key related pem and pub file should be copied to verified_designs_examples/bigip/securing-graphql-with-AWAF/terraform folder (file names should be: graphql-automation-key and graphql-automation-key.pub) <br>
5. Update your variables in verified_designs_examples/bigip/securing-graphql-with-AWAF/data/testbed-data.json file <br>
6. Make sure you have a self hosted runner and it is added to this repo<br>
7. Make sure awscli, kubectl, ansible-playbook, pytest and other required tools are installed on this private custom self hosted runner. Refer requirements.txt file for more details<br>

Steps to run the workflow:

1. Navigate to Actions tab in the repository and select the workflow you want to execute.<br>
`Note:` If Actions tab is disabled: (Navigate to `Settings->General->Actions permission->Allow all actions and reusable workflows->save`)<br>
2. Click on Run workflow on the right side of the UI.<br>
`Note:` Once all jobs in workflow are executed, test report can be downloaded from artifacts<br>

![02](https://user-images.githubusercontent.com/90624610/225229339-f93135a1-071f-4254-9983-515b3787abd7.JPG)

Jobs info in pipeline:

![01](https://user-images.githubusercontent.com/90624610/225229401-863dcc21-19b3-4410-b605-690ec3f2cf36.JPG)

`terraform` - This job will deploy and configure all needed components in AWS like, BIGIP, EKS, DVGA etc.<br>
`test` - This job will push security policies to BIGIP, send traffic to Virtual server created on BIGIP and capture results in html files which can be downloaded from artifacts.<br>
`destroy` - This job will destroy all components created for this article.<br>

Tools used:<br>
`Terraform, Ansible, Python requests module and PyTest framework`<br>

Debugging steps:

1. No job is getting executed - Check if self hosted runner is available.<br>
2. Workflow fails with credential/token error - Check if credentials are valid and not expired.<br>
3. Deploy job fails with already exists errors - Check if components in this article are not cleaned properly because of some intermittent network issues. If some components like EKS, VPC, Key pair are still available delete them.<br>

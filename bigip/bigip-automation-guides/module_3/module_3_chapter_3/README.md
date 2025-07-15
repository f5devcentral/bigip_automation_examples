## Infrastructure Configuration using Terraform, Ansible, AS3, and iRules
### module 3 chapter 3

### Prerequisites

- Access to an AWS account with permissions to create resources
- Git repository (GitLab, GitHub, or Bitbucket) to host the code
- Jenkins server with access to the Git repository
- Jenkins Runner configured to execute the pipeline

### Overview

This repository contains a Jenkinsfile that automates the deployment of F5 BIG-IP infrastructure using Terraform and Ansible. It includes stages for provisioning cloud resources, configuring BIG-IP with Ansible, and applying configurations using AS3 and iRules.

The Jenkinsfile defines a pipeline that automates:

1. **Terraform** provisioning for cloud infrastructure (e.g., AWS).
2. **Ansible** configuration of BIG-IP using AS3 and iRules.


### Setup Instructions

#### 1. Push to Your Own Git Repository

Clone or download this repository, then push the contents of the `module_3_chapter3` directory to your Git repository. Ensure you have a `Jenkinsfile` in the root of your repository.

#### 2. Configure Multibranch Pipeline in Jenkins

1. Open Jenkins.
2. Create a new **Multibranch Pipeline** job.
3. Under **Branch Sources**, select your Git provider (e.g., GitHub or GitLab).
4. Add your repository URL.
5. Configure credentials if needed.
6. Jenkins will scan branches with a `Jenkinsfile`.

#### 3. Add Webhook (Optional) 

Set up a webhook in your Git hosting platform to notify Jenkins of changes:

* GitHub: **Settings → Webhooks**

Use the URL:

```
http://<your-jenkins-url>/github-webhook/
```

#### 4. Configure secrets in Jenkins

1. Go to **Manage Jenkins → Manage Credentials**.
2. Add the following credentials:
   - **AWS Access Key ID**: `aws_access_key_id`
   - **AWS Secret Access Key**: `aws_secret_access_key`
   - **AWS Session Token** (if using temporary credentials): `aws_session_token`
   - **BIG-IP Username**: `bigip_username`
   - **BIG-IP Password**: `bigip_password`
   - **GitHub Token**: `github_token`

#### 5. Run the Pipeline

Once a branch with a `Jenkinsfile` is pushed:

* Jenkins will automatically discover the branch.
* It will execute the defined stages in the Jenkinsfile.
* You can monitor the job in the **Multibranch Pipeline dashboard**.

After the pipeline runs successfully, it will provision the infrastructure, configure the BIG-IP instance, and apply the necessary iRules with Ansible.

The output will include details about the created resources, such as the IP address of the BIG-IP instance. Credentials for accessing the BIG-IP device are stored in the Jenkins credentials store.

To verify the setup, log in to the BIG-IP web interface and check that the iRules have been applied correctly.
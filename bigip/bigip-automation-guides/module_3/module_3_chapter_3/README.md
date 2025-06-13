## Infrastructure Configuration using Terraform, Ansible, AS3, and iRules
### module 3 chapter 3


### Overview

This repository contains a Jenkinsfile that automates the deployment of F5 BIG-IP infrastructure using Terraform and Ansible. It includes stages for provisioning cloud resources, configuring BIG-IP with Ansible, and applying configurations using AS3 and iRules.

The Jenkinsfile defines a pipeline that automates:

1. **Terraform** provisioning for cloud infrastructure (e.g., AWS).
2. **Ansible** configuration of BIG-IP using AS3 and iRules.


### Setup Instructions

#### 1. Push to Your Own Git Repository

Copy this repository and push it to your own GitLab/GitHub/Bitbucket project:

```bash
git clone https://your-clone-url.git
cd your-project
git remote add origin https://your.git.server/your-username/your-repo.git
git push -u origin main
```

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

#### 4. Run the Pipeline

Once a branch with a `Jenkinsfile` is pushed:

* Jenkins will automatically discover the branch.
* It will execute the defined stages in the Jenkinsfile.
* You can monitor the job in the **Multibranch Pipeline dashboard**.

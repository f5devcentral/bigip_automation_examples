# DRAFT: Scale API Security Session demo

# Table of Contents

- [DRAFT: Scale API Security Session demo](#draft-scale-api-security-session-demo)
- [Table of Contents](#table-of-contents)
- [Environment Setup](#environment-setup)
- [Manual Configuration](#manual-configuration)
  - [Enable Server Maintenance Mode using Policy via TMOS](#enable-server-maintenance-mode-using-policy-via-tmos)
    - [Test Sites Availability](#test-sites-availability)
    - [Create Policy and Maintenance Rule](#create-policy-and-maintenance-rule)
    - [Add Policy to Virtual Server](#add-policy-to-virtual-server)
    - [Test Maintenance Mode](#test-maintenance-mode)
    - [Disable Maintenance Mode \& Test](#disable-maintenance-mode--test)
  - [Enable Server Maintenance Mode using iRule via TMOS](#enable-server-maintenance-mode-using-irule-via-tmos)
    - [Test Sites Availability](#test-sites-availability-1)
    - [Create Maintenance iRule](#create-maintenance-irule)
    - [Add iRule to Virtual Server](#add-irule-to-virtual-server)
    - [Test Maintenance Mode](#test-maintenance-mode-1)
    - [Disable Maintenance Mode \& Test](#disable-maintenance-mode--test-1)
- [Automated Configuration](#automated-configuration)
  - [Enable Server Maintenance Mode using Policy via Terraform](#enable-server-maintenance-mode-using-policy-via-terraform)
    - [Test Sites Availability](#test-sites-availability-2)
    - [Run Terraform with Maintenance Policy](#run-terraform-with-maintenance-policy)
      - [1. Initialize Terraform](#1-initialize-terraform)
      - [2. Import Server](#2-import-server)
      - [3. Apply Terraform](#3-apply-terraform)
    - [Test Maintenance Mode](#test-maintenance-mode-2)
    - [Disable Maintenance Mode](#disable-maintenance-mode)
    - [Check Policy \& Test](#check-policy--test)
  - [Avoid Path Traversal using iRule via Ansible](#avoid-path-traversal-using-irule-via-ansible)
    - [Add iRule](#add-irule)
    - [Test Added iRule](#test-added-irule)
    - [Detach iRule](#detach-irule)
  - [Update Application to Scale via GitOPS](#update-application-to-scale-via-gitops)
    - [Run the CI/CD Environment](#run-the-cicd-environment)
    - [Overview the Scale Solution](#overview-the-scale-solution)
    - [Ansible Script to Scale the Application](#ansible-script-to-scale-the-application)
    - [Run the Pipelines](#run-the-pipelines)
    - [Test Waiting Room](#test-waiting-room)

# Environment Setup

Proceed to the following directory:

```bash
bigip/bigip_next/security/operations/scale-api-security/env-setup/playbooks
```

First, install the app:

```bash
app_install.yml
```

Next, run TMOS setup:

```bash
tmos_setup.yml
```

# Manual Configuration

In this part of the guide we have two sites on one virtual server. We will manually move the first one to maintenance mode, whereas the second one will stay up and running. In the first use-case, we will use LLM security policy with a maintenance rule, in the second use-case - maintenance iRule via TMOS.

## Enable Server Maintenance Mode using Policy via TMOS

In order to switch the server to maintenance mode, we will configure LTM policy with a maintenance rule. Then we will add the policy to the virtual server and test site availability. Note that we will specify host name of one site in the policy rule since there can be a few sites in one virtual server.

### Test Sites Availability

First, run the following command to see the `app.domain.local` is up and running:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, test the second `app-2.domain.local` site:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from both outputs, both sites are in **Performing Action**.

### Create Policy and Maintenance Rule

Go to TMOS, proceed to **Local Traffic** => **Policies** => **Create**.

Give policy a name and click the **Create Policy** button.

Add a maintenance rule. Click the **Create** button.

We will add requests from the first site to this rule. Specify all the required configuration for the rule: **HTTP Host**, **app.domain.local**, **request**. Select **forward traffic** to **pool** and choose the maintenance pool.

Publish the created policy.

### Add Policy to Virtual Server

Navigate to **Local Traffic** => **Virtual Servers** => **Virtual Server List**. Enter the server and proceed to **Resources**. Click the **Manage** button for policies.

Enable the policy we created earlier for this server.

### Test Maintenance Mode

First, run the first site:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, try the second one:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from the output, the first site has changed its status and is in **Maintenance mode** now, whereas the second one is still performing.

### Disable Maintenance Mode & Test

Back in your TMOS, **Virtual Servers** => **Virtual Server List**, in the opened server configuration click the **Manage** button for policies. Remove the added maintenance policy.

Finally, let's test the sites. First, run the following command:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, the second one:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from the output, both sites are in **Performing Action**.

## Enable Server Maintenance Mode using iRule via TMOS

In this part we will create maintenance iRule and use it to enable maintenance mode for the site.

### Test Sites Availability

First, run the following command to see the `app.domain.local` is up and running:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, test the second `app-2.domain.local` site:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from both outputs, both sites are in **Performing Action**.

### Create Maintenance iRule

Go to TMOS, proceed to **Local Traffic** => **iRules** => **iRule List**. Click the **Create** button.

Give iRule a name and paste the following definition:

```bash
===TODO====
```

### Add iRule to Virtual Server

Navigate to **Local Traffic** => **Virtual Servers** => **Virtual Server List**. Enter the server and proceed to **Resources**. Click the **Manage** button for iRules.

Enable the maintenance iRule we created earlier for this server.

### Test Maintenance Mode

First, run the first site:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, try the second one:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from the output, the first site has changed its status and is in **Maintenance mode** now, whereas the second one is still performing.

### Disable Maintenance Mode & Test

Back in your TMOS, **Virtual Servers** => **Virtual Server List**, in the opened server configuration click the **Manage** button under iRules. Remove the added maintenance iRule.

Finally, let's test the sites. First, run the following command:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, the second one:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from the output, both sites are in **Performing Action**.

# Automated Configuration

## Enable Server Maintenance Mode using Policy via Terraform

In this part of the guide we will use Terraform automated scripts to switch one of the sites that are on one virtual server to maintenance mode, whereas the second one will stay up and running. We will use LTM policy to do that.

### Test Sites Availability

First, run the following command to see the `app.domain.local` is up and running:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, test the second `app-2.domain.local` site:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from both outputs, both sites are in **Performing Action**.

### Run Terraform with Maintenance Policy

Go to the following directory:

```bash
cd ~/bigip_automation_examples/bigip/bigip_next/security/operations/scale-api-security/maintenance-terraform
```

Take a look at the maintenance policy we are going to use:

```bash
bigip/bigip_next/security/operations/scale-api-security/maintenance-terraform/main.tf
```

#### 1. Initialize Terraform

Initialize Terraform by running the following command:

```bash
terraform init
```

#### 2. Import Server

Since we already have infrastructure in TMOS, we cannot apply the configuration. First we will need to import server configuration to Terraform local state, and only after that we will apply Terraform scenario.

Run the following command to import server configuration to Terraform:

```bash
terraform import bigip_ltm_virtual_server.http /Common/app-scale-api
```

#### 3. Apply Terraform

Finally, run Terraform:

```bash
terraform apply -var-file=terraform.tfvars
```

### Test Maintenance Mode

First, we will check the applied maintenance policy via TMOS. Navigate to **Local Traffic** => **Policies** => **Policy List**. You will see the published policy.

Next, proceed to **Virtual Servers** => **Virtual Server List**. Enter the server and proceed to **Resources**. You will see the applied maintenance policy.

Next, we will test the maintenance mode. First, run the first site:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, try the second one:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from the output, the first site has changed its status and is in **Maintenance mode** now, whereas the second one is still performing.

### Disable Maintenance Mode

Enter the following file again:

```bash
bigip/bigip_next/security/operations/scale-api-security/maintenance-terraform/main.tf
```

Remove the policy in the end of the file:

```bash
 policies    = [var.policy_name]
```

Run the updated Terraform with removed policy:

```bash
terraform apply -var-file=terraform.tfvars
```

### Check Policy & Test

first, we will check the removed maintenance policy via TMOS. In **Virtual Servers** proceed to **Virtual Server List**. Enter the server and proceed to **Resources**. You will see that that applied earlier maintenance policy is removed.

After that, we will test sites availability.

First, run the following command:

```bash
curl --resolve app.domain.local:80:10.1.10.41 http://app.domain.local/action
```

Then, the second one:

```bash
curl --resolve app-2.domain.local:80:10.1.10.41 http://app-2.domain.local/action
```

As you can see from the output, both sites are in **Performing Action**.

## Avoid Path Traversal using iRule via Ansible

Apply avoid path traversal attack rule at scale: to bunch of servers. To specify the servers list, open the config file and update the list.

```
//TODO: Add the config file to update
```

Then we can take a look at the iRule we are going to apply by navigating to:

```bash
bigip/bigip_next/security/operations/scale-api-security/ata-ansible/templates/irule.tcl
```

### Add iRule

Run the command to create the iRule and add to a batch of 20 virtual servers:

```bash
ansible-playbook ./playbooks/create-attach-rule.yml
```

### Test Added iRule

First, we will take a look at the added iRule vie TMOS.

In **Virtual Servers** proceed to **Virtual Server List**. Enter the server and proceed to **Resources**. You will see the added iRule.

Next, we will rerun the request to test the servers:

```bash
for ip in $(seq 41 60); do echo "Requesting http://10.1.10.$ip"; curl -X GET "http://10.1.10.$ip/action?filename=../sensitive_file_$ip"; done
```

As seen from the outputs, the request is not answered.

Finally, we will take a look at the server traffic via TMOS. You can also see the traffic via TMOS. Navigate to the **System** => **Logs** => **Local Traffic** to see the events and the applied iRule.

### Detach iRule

Finally, we can detach the added iRule. Run the following command:

```bash
ansible-playbook ./playbooks/detach-rule.yml
```

Navigate to **Local Traffic** => **Virtual Servers** proceed to **Virtual Server List**. Enter the server and proceed to **Resources**. You will see no resources attached.

Run the GET request:

```bash
curl -X GET "http://10.1.10.41/action?filename=../sensitive_file"
```

After that, run the POST request to send the data to the server:

```bash
curl -X POST -d "filename=../sensitive_file" "http://10.1.10.41/action"
```

As you can see from the output, both are in **Performing Action**.

## Update Application to Scale via GitOPS

On schedule scale the application to correspond to the predictable demand.

### Run the CI/CD Environment

Run Git and Jenkins environment to apply Ansible scaling script to the TMOS instance. Use logins/passwords from Jenkins secrets.

### Overview the Scale Solution

1. Add nodes
2. Add pools
3. Add IRule to route traffic as well as put excessive requests to wait room

### Ansible Script to Scale the Application

```yaml
TODO: Add IRUle to perform the waiting room routine
```

### Run the Pipelines

Login to Jenkins. Run the pipeline. Overview the result

### Test Waiting Room

Open Firefox. Open tab to an application. Open another tab. The second tab will be put to the Waiting room. In 10 seconds, the request will be automatically routed to the app page.

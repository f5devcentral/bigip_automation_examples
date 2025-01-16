# Scale API Security

# Table of Contents

- [Scale API Security](#scale-api-security)
- [Table of Contents](#table-of-contents)
- [Environment Setup](#environment-setup)
- [Manual Configuration](#manual-configuration)
  - [Enable Server Maintenance Mode using Policy via TMOS](#enable-server-maintenance-mode-using-policy-via-tmos)
    - [Test Sites Availability](#test-sites-availability)

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

### Disable Maintenance Mode

Back in your TMOS, **Virtual Servers** => **Virtual Server List**, in the opened server configuration click the **Manage** button for policies. Remove the added maintenance policy.

### Test Sites Availability

First, run the following command:

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

### Disable Maintenance Mode

Back in your TMOS, **Virtual Servers** => **Virtual Server List**, in the opened server configuration click the **Manage** button under iRules. Remove the added maintenance iRule.

### Test Sites Availability

First, run the following command:

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

Note that since we already have a virtual server in TMOS, we will first need to import server configuration to Terraform, and only after that we will apply Terraform.

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

Next, import server configuration to Terraform:

```bash
terraform import bigip_ltm_virtual_server.http /Common/app-scale-api
```

#### 3. Apply Terraform

Finally, run Terraform:

```bash
terraform apply -var-file=terraform.tfvars
```

### Check Applied Maintenance Policy via TMOS

Navigate to **Local Traffic** => **Policies** => **Policy List**. You will see the published policy.

Next, proceed to **Virtual Servers** => **Virtual Server List**. Enter the server and proceed to **Resources**. You will see the applied maintenance policy.

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

### Check Removed Maintenance Policy via TMOS

In **Virtual Servers** proceed to **Virtual Server List**. Enter the server and proceed to **Resources**. You will see that that applied earlier maintenance policy is removed.

### Test Sites Availability

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

Let's take a look at the iRule we are going to apply by navigating to:

```bash
bigip/bigip_next/security/operations/scale-api-security/ata-ansible/templates/irule.tcl
```

### Test

Proceed to the following directory:

```bash
cd ~/bigip_automation_examples/bigip/bigip_next/security/operations/scale-api-security/ata-ansible
```

Run first the GET request:

```bash
curl -X GET "http://10.1.10.41/action?filename=../sensitive_file"
```

After that, run the POST request to send the data to the server:

```bash
curl -X POST -d "filename=../sensitive_file" "http://10.1.10.41/action"
```

As you can see from the output, both are in **Performing Action**.

### Add iRule

Run the command to create the iRule and add to virtual server:

```bash
ansible-playbook ./playbooks/create-attach-rule.yml
```

### Test Added iRule

First, we will take a look at the added iRule vie TMOS.

In **Virtual Servers** proceed to **Virtual Server List**. Enter the server and proceed to **Resources**. You will see the added iRule.

Next, we will rerun the requests:

```bash
curl -X GET "http://10.1.10.41/action?filename=../sensitive_file"
```

```bash
curl -X POST -d "filename=../sensitive_file" "http://10.1.10.41/action"
```

As seen from the outputs, the request is not answered.

Finally, we will take a look at the server traffic via TMOS. You can also see the traffic via TMOS. Navigate to the **System** => **Logs** => **Local Traffic** to see the even and the applied iRule.

Now let's test the app:

```bash
curl http://10.1.10.41/action
```

The output shows it's in **Performing Action**.

### Detach iRule

Finally, we can detach the added iRule. Run the following command:

```bash
ansible-playbook ./playbooks/detach-rule.yml
```

Navigate to **Local Traffic** => **Virtual Servers** proceed to **Virtual Server List**. Enter the server and proceed to **Resources**. You will see no resources attached.

Now let's test the app:

```bash
curl http://10.1.10.41/action
```

The output shows it's in **Performing Action**.

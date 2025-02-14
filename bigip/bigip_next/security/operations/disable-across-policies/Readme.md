# Disable Signatures Across Policies

# Table of Contents

- [Disable Signatures Across Policies](#disable-signatures-across-policies)
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Environment](#environment)
- [Automated Workflow Guide](#automated-workflow-guide)
  - [1. Configure Connectivity to Central Manager](#1-configure-connectivity-to-central-manager)
  - [2. Configure Update Logging](#2-configure-update-logging)
    - [2.1 Connect to Running Docker](#21-connect-to-running-docker)
    - [2.2 Review Logs in Real-Time](#22-review-logs-in-real-time)
  - [3. Deploy Updates](#3-deploy-updates)
  - [4. Reports](#4-reports)
    - [4.1 Signature Override Report](#41-signature-override-report)
    - [4.2 Realtime Signature Override Logs](#42-realtime-signature-override-logs)

# Overview

This flow is one of three use-cases of the [Operations](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/Readme.md) series focused on disabling signatures across multiple policies via Ansible. In the course of this guide we will add parameters with their overrides. For this guide we will use the app with a WAF policy setup and deployed in the [Deploy and Protect a New App on BIG-IP Next with Security Policy](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/deploy-with-new-next-waf/Readme.md#environment--pre-requisites) guide. We will assume that our app stores scripts to be embedded in webpages. We have app's server that allows app to execute CRUD operations and has its APIs specified in the Swagger file.

# Environment

If you are completing this use case after having done the [Disable signature on specific URL or parameter](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/disable-signature-url/Readme.md) guide, you can skip environment setup part.

If this use case is the first one you take, you will need to complete the [Deploy and Protect a New App on BIG-IP Next with Security Policy](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/deploy-with-new-next-waf/Readme.md#environment--pre-requisites) guide first in order to set up the environment and deploy app with security policy, including the following steps:

- [Blueprint Setup (for F5 employees or customers with access to UDF)](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/deploy-with-new-next-waf/Readme.md#blueprint-setup-for-f5-employees-or-customers-with-access-to-udf)
- [Docker Setup](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/deploy-with-new-next-waf/Readme.md#docker-setup)
- [Infrastructure Configuration - items 1 & 2](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/deploy-with-new-next-waf/Readme.md#infrastructure-configuration)
- [Automated Workflow Guide - items 1 - 5](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/deploy-with-new-next-waf/Readme.md#automated-workflow-guide) to deploy the app with the WAF policy
- Verify the Deployed App with its Policy:

  - (optional) If you want to view app's APIs, enter the Swagger file of app API by running the following command:

    ```bash
    cat ~/bigip_automation_examples/bigip/bigip_next/env-init/environment/templates/code-crud-swagger.yaml
    ```

  - Run the following command to see the list of scripts:

    ```bash
    curl 'http://10.1.10.93/api/v1/script'
    ```

  - Run the following command to update a script:

    ```bash
    curl -X PUT "http://10.1.10.93/api/v1/script/1?code=<script>showPopup()</script>"
    ```

    This will output the false positive result because we have a setup WAF whose signature is executed when we send the code parameter for the script and makes it impossible to execute the command. So we will need to disable the signature that executes as false positive for this API and code parameter in URL.

# Automated Workflow Guide

## 1. Configure Connectivity to Central Manager

**Note that we will use source files from another [Operations](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/Readme.md) use case - [Disable signature on specific URL or parameter](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/disable-signature-url/Readme.md).**

If you are using Blueprint, you need to add the second policy for update - `juice_shop_policy` in the following file:

```bash
bigip/bigip_next/security/operations/disable-signature-url/next_vars.yml
```

Your `next_vars.yml` file might be as follows:

```yml
central_manager:
  address: 10.1.1.5
  user: admin
  password: Welcome1234567!

override_signature:
  - name:
      - waf_greenfield_demo_policy
      - juice_shop_policy
    parameters:
      - name: code
        signatures:
          - 200001088
      - name: query
        signatures:
          - 200000098
          - 200001088
          - 200001475
          - 200101609

task_timeout_minutes: 15
override_report: ../signature-override-report.txt
```

If you are not using Blueprint, you will need to edit the file as follows:

- specify Central Manager parameters: `address`, `user`, `password`,
- add policy names as an array, list of parameters and signatures to be overridden
- indicate file to save override reports to and task timeout time in minutes. Note that if you have three and more BIG IP Next nodes for updates, you might need 15 and more minutes.

## 2. Configure Update Logging

**If you have completed the [Disable signature on specific URL or parameter](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/disable-signature-url/Readme.md) guide, your connection is already established and you can skip this step.**

### 2.1 Connect to Running Docker

If the docker option is used, there is a possibility to see the logs of parameter update with signature overrides process. First, you need to establish one more SSH connection to jumphost. Second, connect to the running docker. To do that navigate to:

```bash
bigip/bigip_next/env-init/docker
```

In this folder run the following command to connect to the running Docker:

```bash
sh ./connect.sh
```

### 2.2 Review Logs in Real-Time

Proceed to the following folder:

```bash
bigip/bigip_next/security/operations/disable-signature-url
```

Run the following command to review logs:

```bash
tail -f ./logs/cm_polling.log
```

## 3. Deploy Updates

Navigate to the following directory in your first CLI:

```bash
bigip/bigip_next/security/operations/disable-signature-url
```

Run the following command to deploy the updates. Note that deploy can take some time.

```bash
ansible-playbook ./playbooks/site.yml
```

You will see the process status in the second CLI set up for logging.

## 4. Reports

### 4.1 Signature Override Report

Run the following command to view update logs:

```bash
cat signature-override-report.txt
```

You will see the following report as output showing both policies, time of deploy task creation & completion, and parameters status:

```
|-----------------------------------------------|----------------------------------|----------------------------------|-----------------------------------------------|--------------|--------------------------------------------|
| Policy Name                                   | Deploy Task Created              | Deploy Task Completed            | Paremeter                                     | Status       | Message                                    |
|-----------------------------------------------|----------------------------------|----------------------------------|-----------------------------------------------|--------------|--------------------------------------------|
| waf_greenfield_demo_policy                    | 2024-09-24T16:13:18.201501Z      | 2024-09-24T16:13:31.825522Z      |                                               | Successed    | Task completed                             |
|                                               |                                  |                                  | code: Update                                  |              |                                            |
|                                               |                                  |                                  | query: Update                                 |              |                                            |
|-----------------------------------------------|----------------------------------|----------------------------------|-----------------------------------------------|--------------|--------------------------------------------|
| juice_shop_policy                             | 2024-09-24T16:13:34.513242Z      | 2024-09-24T16:13:47.473602Z      |                                               | Successed    | Task completed                             |
|                                               |                                  |                                  | code: Add                                     |              |                                            |
|                                               |                                  |                                  | query: Add                                    |              |                                            |
|-----------------------------------------------|----------------------------------|----------------------------------|-----------------------------------------------|--------------|--------------------------------------------|
```

### 4.2 Realtime Signature Override Logs

You will see the following logs in the second connected CLI:

```
Task Polling: eaa95fbb-8737-4b98-8f58-c30d332954b6 - Redeploy Policy > running
Task Polling: eaa95fbb-8737-4b98-8f58-c30d332954b6 - Redeploy Policy > running
Task Polling: eaa95fbb-8737-4b98-8f58-c30d332954b6 - Redeploy Policy > running
Task Polling: eaa95fbb-8737-4b98-8f58-c30d332954b6 - Redeploy Policy > completed
Task Polling: 912c997c-bf9a-4a33-8de5-2d308429ccfe - Redeploy Policy > running
Task Polling: 912c997c-bf9a-4a33-8de5-2d308429ccfe - Redeploy Policy > running
Task Polling: 912c997c-bf9a-4a33-8de5-2d308429ccfe - Redeploy Policy > running
Task Polling: 912c997c-bf9a-4a33-8de5-2d308429ccfe - Redeploy Policy > completed
```

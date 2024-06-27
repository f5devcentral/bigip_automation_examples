# Deploy a New App to BIG-IP Next with Next WAF Policy

# Table of Contents

- [Overview](#overview)
- [Setup Diagram](#setup-diagram)
- [Manual Workflow Guide](#manual-workflow-guide)
  - [1. Start Creating an App](#1-start-creating-an-app)
  - [2. Add Pool and Server](#2-add-pool-and-server)
  - [3. Create WAF Security Policy](#3-create-waf-security-policy)
  - [4. Add Pool Member](#4-add-pool-member)
  - [5. Validate and Deploy](#5-validate-and-deploy)
- [Automated Workflow Guide](#automated-workflow-guide)
- [Additional Related Resources](#additional-related-resources)

# Overview

In this part of the guide we will take a look at a greenfield use-case where we will deploy an app to BIG-IP Next, as well as create a WAF Policy for it. We will be using BIG-IP Next Central Manager that will let us experience the ease of all deployment process and the possibility to configure Next WAF policy in blocking mode right in the process of its creation.

# Setup Diagram

======TODO======

# Manual Workflow Guide

You can follow the steps in the manual or automated guides below:

## 1. Start Creating an App

Log in BIG-IP Next Central Manager and proceed to **Application Workspace**.

![alt text](./assets/cm-navigate.png)

Click the **Start Adding Apps** button. This will open the creation form.

![alt text](./assets/start-adding-app.png)

Before moving on to app configuration, give it a name, select kind of application service and click the **Start Creating** button.

![alt text](./assets/app-form.png)

You can type in a description for the application service and move on.

![alt text](./assets/app-description.png)

## 2. Add Pool and Server

Next, we will add a pool and virtual server. Navigate to the **Pools** tab and click the **Create** tab.

![alt text](./assets/pool-create.png)

Give pool a name, make sure to use Service Port **80** and Load-Balancing Mode **round-robin** for this flow. Move on to the **Virtual Servers** tab to configure one for the app.

![alt text](./assets/pool-name.png)

Give virtual server a name, select the pool we've just added in the drop-down menu and make sure to have Virtual Port **80** specified. As soon as the virtual server has been configured, proceed to adding a WAF Security Policy.

![alt text](./assets/create-security-policy.png)

## 3. Create WAF Security Policy

First, we need to enable using WAF Policy using the toggle. Next, click the **Create** button which will open WAF Policy configuration form.

![alt text](./assets/waf-policy.png)

Give WAF policy a name and enable the L7 DoS Protection for the app. Take a look at other configuration, such as enabled Bot Defense and Threat Intelligence options. Also make sure to have **Blocking** selected for Enforcement Mode. As you can see, BIG-IP Next Central Manager provides an opportunity to set up the blocking enforcement mode right at the WAF Policy configuration stage which makes the whole process fast and easy and allows us to have blocking mode for our app from day one. When the policy properties have been configured, proceed by clicking **Save**.

![alt text](./assets/waf-config.png)

The name should appear in WAF Policy name field. Click **Save** to move on.

![alt text](./assets/save-policy.png)

Back on the app configuration page, take a look at the configured properties and click **Review and Deploy**.

![alt text](./assets/deploy-app.png)

After that, we will specify deployment instance. CLick the **Start Adding** button, choose an instance and add it to the list.

![alt text](./assets/select-bigipnext-instance.png)

## 4. Add Pool Member

Finally, in order to specify deployment instance, we will add a pool member. Open the drop-down menu under **Members** and select adding a pool member.

![alt text](./assets/pool-member.png)

In the opened configuration window add a row and fill it in by giving pool member a name and specifying the IP Address.

![alt text](./assets/member-config.png)

## 5. Validate and Deploy

Back on the deployment instance page, the configured pool member will appear in the table. Fill in instance virtual address and click the **Validate All** button. This will start the process of validating all the configuration before deployment.

![alt text](./assets/validate-all.png)

As soon as validation is over, its result will be displayed on the page. If the validation is successful, you can click the **Deploy Changes** button.

![alt text](./assets/deploy-changes.png)

The next window will ask you to confirm application service deployment. Take a look at app name and deployment instance and click **Yes, Deploy**.

![alt text](./assets/confirm-deploy.png)

As soon as the deployment process is over, you will see a notification in the lower right corner and the application will be displayed in the table. You can see its health status, instance and security policy we configured.

![alt text](./assets/deployment-complete.png)

Congrats, you did it! You deployed a new app to BIG-IP Next and applied a WAF policy to it using BIG-IP Next Central Manager. Central Manager let us configure the WAF Policy in an easy and straightforward way making blocking mode available right away.

# Automated Workflow Guide

=======TODO========

# Additional Related Resources

=======TODO========

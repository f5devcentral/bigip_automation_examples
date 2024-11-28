# Migrate LTM by Request

# Table of Contents

- [Update Signature Package for Next WAF in Central Manager and Push to All Instances](#update-signature-package-for-next-waf-in-central-manager-and-push-to-all-instances)
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Docker Setup](#docker-setup)
- [Manual Workflow Guide](#manual-workflow-guide)
- [Automated Workflow Guide](#automated-workflow-guide)
  - [1. Configure Connectivity](#1-configure-connectivity)
  - [2. Configure Update Logging](#2-configure-update-logging)
    - [2.1 Connect to Running Docker](#21-connect-to-running-docker)
    - [2.2 Review Logs in Real-Time](#22-review-logs-in-real-time)
  - [3. Checking for Updates and Installing Them](#3-checking-for-updates-and-installing-them)
  - [4. Reports](#4-reports)
    - [4.1 Live Update Report](#41-live-update-report)
    - [4.2 Push Updates Report](#42-push-updates-report)
    - [4.3 Realtime Live Update Logs](#43-realtime-live-update-logs)

# Overview

This flow is one of three use-cases of the [Operations](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/security/operations/Readme.md) series on applying updates to Next WAF. It provides manual walk-through steps and automated Terraform scripts for updating signature package for Next WAF in Central Manager and then pushing them to all the instances.

# Docker Setup

You may choose to use the included Docker. You may run it on Linux machine in order to take advantage of Ansible tooling.

If you chose to use Docker, follow the steps to set it up in this [guide](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/security/deploy-with-new-next-waf#docker-setup).

# Automated Workflow Guide

Log in BIG-IP Next Central

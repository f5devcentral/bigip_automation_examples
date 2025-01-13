# BIG-IP Next WAF Operations

# Table of Contents

- [BIG-IP Next WAF Operations](#big-ip-next-waf-operations)
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Environment \& Pre-requisites](#environment--pre-requisites)
- [Questions \& Issues](#questions--issues)

# Overview

**Next WAF Operations** guide showcases managing updates for BIG-IP Next WAF using Central Manager (CM) and automation via CM APIs. BIG-IP Next Central Manager accelerates app migration and simplifies management of BIG-IP Next infrastructure and app services.

We will focus on _manual_ management of Next WAF as well as _automation_ scripts for the following use-cases:

1. [Update signature package in CM and push to all instances](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/live-update/Readme.md),
2. [Disable signature on specific URL or parameter](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/disable-signature-url/Readme.md),
3. [Disable signature across policies](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/disable-across-policies/Readme.md)
4. [API Endpoint Protection](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/open-api-protection/Readme.md)

| **Guide**                                                | **Manual**                                                                                                                                                                               | **Automation**                                                                                                                                                                                   |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Update signature package in CM and push to all instances | [Manual flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/live-update/Readme.md#manual-workflow-guide)           | [Automated flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/live-update/Readme.md#automated-workflow-guide)             |
| Disable signature on specific URL or parameter           | [Manual flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/disable-signature-url/Readme.md#manual-workflow-guide) | [Automated flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/disable-signature-url/Readme.md#automated-workflow-guide)   |
| Disable signature across policies                        | N/A                                                                                                                                                                                      | [Automated flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/disable-across-policies/Readme.md#automated-workflow-guide) |
| API Endpoint Protection                                  | [Manual flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/open-api-protection/Readme.md#manual-workflow-guide)   | [Automated flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/security/operations/open-api-protection/Readme.md#automated-workflow-guide)     |

# Environment & Pre-requisites

You may use your own environment with BIG-IP Next, in which, as a pre-requisite, you need to have at a minimum:

- BIG-IP Next Central Manager, which we will use for managing signatures
- BIG-IP Next Instance(s), where we will deploy the signature package(s) and policy updates

For executing automation scripts, you need to utilize a Linux machine with network access to the BIG-IP CM / Next instances.
On this Linux machine, you may choose to run Docker in order to take advantage of the sample app(s) and tooling (Ansible, Terraform, etc.)

Before working through Next WAF operations of Disabling Signatures, you will need to set up your environment to match the config in prerequisites. Each of the use-case guides contains detailed info on setting up the prerequisite configuration. Note that the signature package management does not require any additional infrastructure configuration besides the default Next WAF setup.

# Questions & Issues

Please open a GitHub issue within this repo for any questions or issues identified with this or other Next WAF use-case guides in this repo.

# LTM Migration

# Table of Contents

- [LTM Migration](#ltm-migration)
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Environment \& Pre-requisites](#environment--pre-requisites)
- [Questions \& Issues](#questions--issues)

# Overview

**LTM Migration** series of guides showcases migration of application with custom monitor and routing LTM policy from TMOS to BIG-IP Next using Central Manager (CM). BIG-IP Next Central Manager accelerates app migration and simplifies management of BIG-IP Next infrastructure and app services.

We will focus on _manual_ as well as _automated_ migration processes for the following use-cases:

1. [Migrate Custom Monitor](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/ltm/migrate-ltm-custom-monitors/Readme.md),
2. [Migrate with Routing LTM Policy](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/ltm/migrate-ltm-request/Readme.md),

| **Guide**                       | **Manual**                                                                                                                                                                     | **Automation**                                                                                                                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Migrate Custom Monitor          | [Manual flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/ltm/migrate-ltm-custom-monitors/Readme.md#manual-workflow-guide) | [Automated flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/ltm/migrate-ltm-custom-monitors/Readme.md#automated-workflow-guide) |
| Migrate with Routing LTM Policy | N/A                                                                                                                                                                            | [Automated flow](https://github.com/yoctoserge/bigip_automation_examples/blob/feature/merge-all/bigip/bigip_next/ltm/migrate-ltm-request/Readme.md#automated-workflow-guide)         |

# Environment & Pre-requisites

You may use your own environment with BIG-IP Next, in which, as a pre-requisite, you need to have at a minimum:

- BIG-IP Next Central Manager
- BIG-IP Next Instances

For executing automation scripts, you need to utilize a Linux machine with network access to the BIG-IP CM / Next instances.
On this Linux machine, you may choose to run Docker in order to take advantage of the sample app(s) and tooling (Ansible, Terraform, etc.)

Before working through the guides, you will need to set up your environment to match the config in prerequisites. Each of the use-case guides contains detailed info on setting up the prerequisite configuration.

# Questions & Issues

Please open a GitHub issue within this repo for any questions or issues identified with this or other use-case guides in this repo.

## OpenAPI Schema Validation with Ansible and GitLab CI/CD

###  Prerequisites

- GitLab account with a project to host your code
- GitLab Runner set up to run Ansible playbooks
- BIG-IP instance with an accessible API
- Web server running a Docker container with the application from the `./src` directory

#### 1. Copy the Repository

Clone or download this repository, then push the contents of the `module_3_chapter_2` directory to your GitLab project.

#### GitLab CI/CD Pipeline Setup

Enable CI/CD for your GitLab project. The `.gitlab-ci.yml` file in this directory contains the pipeline configuration.

Before running the pipeline, update the `bigip_vars.yaml` file in the `./ansible` directory with your BIG-IP credentials and the IP address of your BIG-IP instance.


#### 2. Push to `main` Branch

Any commit to the `main` branch will automatically trigger the deployment pipeline.


#### 3. Check Pipeline Status

When the pipeline runs:

* GitLab uses the `python:3.10` image.
* Installs Ansible.
* Uses `ansible/ansible.cfg` as the Ansible configuration file.
* Executes `ansible/playbook.yml` to upload the OpenAPI schema to the BIG-IP device.

You can check the pipeline status in **CI/CD -> Pipelines** in your GitLab project.

After a successful run, verify that the OpenAPI schema has been uploaded to the BIG-IP device.
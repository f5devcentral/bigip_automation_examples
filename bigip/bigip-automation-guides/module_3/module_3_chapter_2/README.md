## OpenAPI Schema Validation with Ansible and GitLab CI/CD


###  How to Use

Follow these steps to set up and run this pipeline in your own GitLab project.

#### 1. Copy the Repository

Clone or download this repository, then push it to your own GitLab project:

```bash
git clone https://your-clone-url.git
cd your-project
git remote add origin https://gitlab.com/your-username/your-repo.git
git push -u origin main
```

---


#### 2. Push to `main` Branch

Any commit to the `main` branch will trigger the deployment pipeline.

```bash
git add .
git commit -m "Trigger Ansible deployment"
git push origin main
```

#### 3. Check Pipeline Status

When the pipeline runs:

* GitLab uses the `python:3.10` image.
* Installs Ansible.
* Uses `ansible/ansible.cfg` as the Ansible configuration file.
* Executes `ansible/playbook.yml` to upload the OpenAPI schema to the BIG-IP device.

You can check the pipeline status in **CI/CD -> Pipelines** in your GitLab project.
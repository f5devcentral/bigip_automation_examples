## Terraform and Ansible chaining for F5 BIG-IP Automation
### module 2 chapter 1

### DRAFT
### Work In Progress

### Prerequisites

- [Terraform](https://developer.hashicorp.com/terraform/install) installed
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed
- AWS CLI configured with appropriate credentials

### Steps

#### 1. Initialize and Apply Terraform

```sh
cd terraform
terraform init
terraform apply
```

Terraform will provision the required infrastructure and output relevant connection details for Ansible.

#### 2. Run Ansible Playbook

After Terraform completes, run the Ansible playbook to configure BIG-IP:

```sh
cd ansible
ansible-galaxy install -r requirements.yml
ansible-playbook -i ./inventory/bigip_hosts.yml playbook.yml
```

#### 3. Destroy Resources (Optional)
If you want to clean up the resources created by Terraform, run:

```sh
terraform destroy
```

### Notes

- Ensure the Terraform state file is available for Ansible
- Review and customize variables as needed in both Terraform and Ansible configurations
- For troubleshooting, check the logs/output of both Terraform and Ansible commands
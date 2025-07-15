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

Before running the Terraform commands, ensure you have the necessary AWS credentials and AWS CLI configured.
To set up the infrastructure using Terraform, follow these steps:

```sh
cd terraform
terraform init
terraform apply
```

Terraform will create the infrastructure in the `us-west-1` region, including the F5 BIG-IP instance and two EC2 instances for testing with nginx web servers. This process may take a few minutes.

Make sure you have set up your AWS credentials and that your IAM user has the necessary permissions to create EC2 instances, security groups, and other related resources.

By default, the Terraform setup uses the `default` AWS profile. If you want to use a different profile, you can update the `providers.tf` file.

Once the terraform apply command finishes successfully, it will output key details about the created resources, including the IP address of the BIG-IP instance. These details are also saved in the Terraform state file.

BIG-IP connection details can be found in the Terraform output. Username and password for the BIG-IP instance are set in the `variables.ts` file.

#### 2. Run Ansible Playbook

After Terraform finishes, go to the Ansible directory and install the required dependencies:

```sh
cd ansible
ansible-galaxy install -r requirements.yml
```

Next, run the playbook using the inventory file, which references the Terraform state file. The `terraform_provider` plugin will read the necessary details from the state.

Run the playbook with:

```sh
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
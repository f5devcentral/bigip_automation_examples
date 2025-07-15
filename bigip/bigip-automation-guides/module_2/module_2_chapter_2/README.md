## API endpoint protection using BIG-IP ASM with OpenAPI schema validation
### module 2 chapter 2

## Terraform

### Prerequisites

- [Terraform](https://developer.hashicorp.com/terraform) installed
- AWS CLI configured with appropriate credentials
- Access to an AWS account with permissions to create resources


### Setup Instructions

1. **Initialize Terraform**

Note: The Terraform scripts do not support ARM64 architecture. Make sure you're using an Intel-based machine to run Terraform.

To initialize Terraform and set up the required providers, run the following commands:

  ```sh
  cd terraform
  terraform init
  ```

2. **Review and Edit Variables**

Create a `terraform.tfvars` file or update the variables directly in `variables.tf` to match your environment. 
You can use the `terraform.tfvars.example` file as a reference.
By default, Terraform uses the `default` AWS CLI profile. If you want to use a different profile, set the `main.tf` file.

1. **Apply the Configuration**

Run the following command to create the resources defined in the Terraform configuration:

  ```sh
  terraform apply
  ```

Terraform will output details about the created resources, including the IP address of the BIG-IP instance and the credentials needed to access it.

4. **Destroy the Deployment (Optional)**

  ```sh
  terraform destroy
  ```

5. **Review the Lab Guide**

Review the [Lab Guide](https://clouddocs.f5.com/training/community/public-cloud/html/class13/class13.html) for detailed instructions and architecture overview.

## Ansible

### Prerequisites
- [Ansible](https://www.ansible.com/)
- AWS CLI configured with appropriate credentials
- Access to an AWS account with permissions to create resources
- BIG-IP instance

### Setup Instructions

1. **Initialize Ansible**

Before running the Ansible playbook, make sure the required dependencies are installed.

Navigate to the Ansible directory and run:

```sh
cd ansible
ansible-galaxy install -r requirements.yml
```

2. **Review and Edit Variables**

Edit `./inventory/group_vars/all/common.yml` to set your BIG-IP username and password.
Edit `./inventory/bigip_hosts.yml` to set the BIG-IP IP address. You can also specify the Python interpreter if needed.

In the `playbook.yml`, you can customize the `pool_members` variable to define the backend servers that the BIG-IP will manage.

3. **Run the Playbook**

To run the Ansible playbook, execute the following command:

```sh
ansible-playbook -i ./inventory/bigip_hosts.yml playbook.yml
```

This will configure the BIG-IP instance based on the tasks defined in the playbook.

To verify the results, review the playbook output or log in to the BIG-IP web interface and check the applied configuration.

--------------
## Additional Information
### This module is based on the Agility Lab and contains the Terraform code to deploy a BIG-IP HA pair in a public cloud environment

- Lab Guide: https://clouddocs.f5.com/training/community/public-cloud/html/class13/class13.html


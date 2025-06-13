## API endpoint protection using BIG-IP ASM with OpenAPI schema validation
### module 2 chapter 2

## Terraform

### Prerequisites

- [Terraform](https://developer.hashicorp.com/terraform)
- AWS CLI configured with appropriate credentials
- Access to an AWS account with permissions to create resources
### Setup Instructions

1. **Initialize Terraform**

  ```sh
  cd terraform
  terraform init
  ```

2. **Review and Edit Variables**

  - Edit `terraform.tfvars` or the variables in `variables.tf` as needed for your environment.

3. **Apply the Configuration**

  ```sh
  terraform apply
  ```

  - Confirm the action when prompted.

5. **Destroy the Deployment (Optional)**

  ```sh
  terraform destroy
  ```

## Ansible

### Prerequisites
- [Ansible](https://www.ansible.com/)
- AWS CLI configured with appropriate credentials
- Access to an AWS account with permissions to create resources

### Setup Instructions

1. **Initialize Ansible**

  ```sh
  cd ansible
  ansible-galaxy install -r requirements.yml
  ```

2. **Review and Edit Variables**
- Edit `./invevntory/group_vars/all/common.yml` and set the variables as needed for your environment.

3. **Run the Playbook**

  ```sh
  ansible-playbook -i ./inventory/bigip_hosts.yml playbook.yml
  ```


# Notes

- Ensure your AWS credentials are set in your environment or via the AWS CLI.
- Review the [Lab Guide](https://clouddocs.f5.com/training/community/public-cloud/html/class13/class13.html) for detailed instructions and architecture overview.
- This module will deploy a BIG-IP HA pair in your AWS account. Charges may apply for AWS resources.
____________________________________________
# This module is based on the Agility Lab and contains the Terraform code to deploy a BIG-IP HA pair in a public cloud environment

## File package for Agility Lab: A&amp;O BIG-IP HA in Public Cloud with Terraform

- Lab Guide: https://clouddocs.f5.com/training/community/public-cloud/html/class13/class13.html


## Previous Versions

- Agility 2022: https://github.com/tmarfil/f5agility2022-pc201


## Contributors

- Jason Chiu  - Updated and expanded for Agility 2023
- Tony Marfil - Updated for Agility 2022
- Tony Marfil - Original creation for Agility 2021


# Tested Versions
- hashicorp/aws v4.62.0
- hashicorp/tls v4.0.4
- hashicorp/random v3.4.3
- hashicorp/http v3.2.1
- hashicorp/null v3.2.1
- hashicorp/template v2.2.0
- hashicorp/local v1.4.0
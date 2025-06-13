# Lab quickstart script
# Usage:
#   - Ensure that you have executed "source setup.sh" before running this script
#   - Log into the AWS Console with your UDF cloud account
#   - Execute: source quickstart.sh
#   - The AWS Marketplace will automatically open in a new browser window. Subscribe to the AMI and wait for completion.
#   - Return to the BASH terminal and enter 'yes' to apply the Terraform plan
#

export BROWSER=wslview
wslview https://aws.amazon.com/marketplace/pp/prodview-cs4qijwjf3ijs
#cp ~/f5lab/scripts/misc/aws-ami-bigip.url /mnt/c/Users/user/Desktop/"AMI-F5 Advanced WAF (PAYG, 25Mbps).url"
cp ~/f5lab/terraform/terraform.tfvars.example ~/f5lab/terraform/terraform.tfvars
cd ~/f5lab/terraform
terraform init
terraform apply

provider "bigip" {
  address                 = module.infrastructure.management_public_ip
  username                = var.bigip_admin_user
  password                = var.bigip_admin_password
}

terraform {
  required_version = ">= 1.1.7"
  required_providers {
    bigip = {
      source = "F5Networks/bigip"
      version = "1.22"
    }
    ansible = {
      version = "~> 1.3.0"
      source  = "ansible/ansible"
    }
  }

  backend "s3" {
    bucket       = "learn-f5-terraform-state"
    key          = "jenkins.tfstate"
    region       = var.aws_region
    use_lockfile = true
  }
}

provider "aws" {
  region                   = var.aws_region
  profile                  = "default"
}

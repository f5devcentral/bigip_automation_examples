terraform {
  required_providers {
    bigip = {
      source  = "F5Networks/bigip"
      version = "~> 1.15" # Adjust this to the version you need
    }
  }

  required_version = ">= 1.0.0" # Adjust to match your Terraform version
}

provider "bigip" {
  address  = var.bigip_address
  username = var.bigip_username
  password = var.bigip_password
}


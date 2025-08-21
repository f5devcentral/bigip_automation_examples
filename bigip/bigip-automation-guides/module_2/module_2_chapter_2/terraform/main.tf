terraform {
  required_version = ">= 1.1.7"
  required_providers {
    template = "~> 2.1"
    local    = "~> 1.2"
    bigip = {
      source = "F5Networks/bigip"
    }
  }
}

provider "aws" {
  region                   = var.aws_region
  shared_credentials_files = ["~/.aws/credentials"]
  profile                  = "gov"
}

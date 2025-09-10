terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.97.0"
    }
    bigip = {
      source  = "terraform-providers/bigip"
      version = "1.22.9"
    }
  }

  backend "s3" {
    bucket         = "learn-f5-terraform-state"
    key            = "terraform.tfstate"
    region         = "us-west-1"
    encrypt        = true
    dynamodb_table = "demo-tf-lockid"
  }
}
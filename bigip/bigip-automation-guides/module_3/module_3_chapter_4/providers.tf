provider "aws" {
  region = local.aws_region
}

locals {
  aws_region  = "us-west-1"

  tags = {
    project = "learnf5-demo"
    env     = "learnf5-demo"
    version = "1.0"
  }
}
terraform {
  backend "s3" {
    region = "ap-south-1"
    bucket = "apisecurity-bucket"
    key    = "automation-nap-deployment-aws.tfstate"
  }
}

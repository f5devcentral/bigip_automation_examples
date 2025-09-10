variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default = {
    Name        = "f5lab"
    Environment = "lab"
  }
}

variable "aws_key_name" {
  description = "Name for AWS keypair"
  default     = "demolab"
}

variable "availability_zone" {
  description = "Availability zone"
  default     = "us-west-1a"
}

variable "vpc_cidrs" {
  description = "VPC subnets (CIDR)"
  type        = map(map(string))
  default = {
    bigip = {
      vpc                       = "10.0.0.0/16"
      bigip_mgmt                = "10.0.10.0/24"
      bigip_mgmt_private_ip     = "10.0.10.10"
      bigip_internal            = "10.0.11.0/24"
      bigip_internal_private_ip = "10.0.11.10"
      bigip_external            = "10.0.12.0/24"
      bigip_external_private_ip = "10.0.12.10"
    }
    app = {
      vpc     = "10.1.0.0/16"
      appsvr1 = "10.1.10.0/24"
      appsvr2 = "10.1.20.0/24"
    }
  }
}


variable "f5_ami_search_name" {
  type    = string
  default = "F5 BIGIP-17.1.*PAYG-Good 25Mbps*"
}

variable "bigip_instance_type" {
  type    = string
  default = "m5.xlarge"
}

variable "bigip_admin_user" {
  description = "BIG-IP admin user"
  type    = string
  default = "admin"
}

variable "bigip_admin_password" {
  description = "BIG-IP admin password"
  type        = string
  default     = "l8ibVeW45O0EXwMF"
}

variable "bigip_ami" {
  description = "BIG-IP AMI"
  type        = string
  default     = "ami-0f3013461e16d9249"
  
}
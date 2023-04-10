variable "pub_key" {
    default = "automation-key.pub"
}
variable "main_vpc_cidr" {}
variable "mgmt_subnet1" {}
variable "public_subnet2" {}
variable "private_subnet3" {}

variable f5_instance_count {
  description = "Number of BIG-IPs to deploy"
  type        = number
  default     = 1
}

variable ec2_instance_type {
  description = "AWS EC2 instance type"
  type        = string
  default     = "c4.4xlarge"
}

variable EC2_KEY_NAME {
  description = "AWS EC2 Key name for SSH access"
  type        = string
  default     = "automation-key"
}

variable custom_user_data {
  description = "Provide a custom bash script or cloud-init script the BIG-IP will run on creation"
  type        = string
  default     = null
}

variable NAP_image_name {
  description = "AMI name for NAP."
  type        = string
  default     = ""
}

# below are for ALB
variable "health_check" {
  type = map(string)
  default = {
    "timeout"  = "10"
    "interval" = "20"
    "path"     = "/"
    "port"     = "80"
    "unhealthy_threshold" = "2"
    "healthy_threshold" = "3"
  }
}

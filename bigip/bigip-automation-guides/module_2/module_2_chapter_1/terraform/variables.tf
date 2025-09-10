variable "aws_region" {
  description = "aws region"
  default     = "us-west-1"
}

variable "bigip_mgmt_ip" {
  description = "BIG-IP management private IP"
  type        = string
  default     = ""
}

variable "bigip_admin_user" {
  description = "BIG-IP admin user"
  type    = string
  default = "admin"
}

variable "bigip_admin_password" {
  description = "BIG-IP admin password"
  type    = string
  default = "l8ibVeW45O0EXwMF"
}
variable "bigip_address" {
  description = "The IP address or hostname of the F5 BIG-IP device"
  type        = string
}

variable "bigip_username" {
  description = "The username for the F5 BIG-IP device"
  type        = string
}

variable "bigip_password" {
  description = "The password for the F5 BIG-IP device"
  type        = string
  sensitive   = true
}

variable "virtual_server_name" {
  description = "The name of the virtual server"
  type        = string
}

variable "virtual_server_destination" {
  description = "The destination of the virtual server"
  type        = string
}

variable "virtual_server_pool" {
  description = "The default pool for the virtual server"
  type        = string
}

variable "policy_name" {
  description = "The name of the LTM policy"
  type        = string
}

variable "policy_pool" {
  description = "The pool used in the LTM policy"
  type        = string
}

variable "http_host_value" {
  description = "The HTTP host value for the policy condition"
  type        = string
}


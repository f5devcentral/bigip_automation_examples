variable "vpc_cidrs" {
  description = "VPC subnets (CIDR)"
  type        = map(map(string))
  default = {
    bigip = {
      bigip_internal_private_ip = "10.0.11.10"
      bigip_external_private_ip = "10.0.12.10"
    }
  }
}

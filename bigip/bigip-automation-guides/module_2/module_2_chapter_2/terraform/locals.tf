# Local variables for bigipX.tf modules

locals {

  # BIG-IP admin password
  random_password = random_string.password.result

  # Device Group
  cluster_primary_ip   = split("/", var.bigip_netcfg["bigip1"]["mgmt"])[0]
  cluster_secondary_ip = split("/", var.bigip_netcfg["bigip2"]["mgmt"])[0]

  # Device Trust remote host index
  #   "1" for bigip1
  #   "0" for bigip2
  bigip1_remote_index = "1"
  bigip2_remote_index = "0"

}

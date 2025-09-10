resource "ansible_host" "host" {
  name   = "hosts"
  groups = ["bigip"]

  variables = {
    bigip_host   = module.infrastructure.management_public_ip
    bigip_vs_ip  = module.infrastructure.external_private_ip
  }
}
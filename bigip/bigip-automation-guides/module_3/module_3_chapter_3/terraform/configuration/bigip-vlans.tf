resource "bigip_net_vlan" "external" {
  name = "external"
  tag      = 4094
  interfaces {
    vlanport = "1.1"
    tagged   = false
  }
}


resource "bigip_net_vlan" "internal" {
  name = "internal"
  tag      = 4093
  interfaces {
    vlanport = "1.2"
    tagged   = false
  }
}

resource "bigip_net_selfip" "external_selfip" {
  name       = var.vpc_cidrs["bigip"]["bigip_external_private_ip"]
  ip         = "${var.vpc_cidrs["bigip"]["bigip_external_private_ip"]}/24"
  vlan       = "/Common/${bigip_net_vlan.external.id}"

  port_lockdown = ["none"]
}

resource "bigip_net_selfip" "internal_selfip" {
  name       = var.vpc_cidrs["bigip"]["bigip_internal_private_ip"]
  ip         = "${var.vpc_cidrs["bigip"]["bigip_internal_private_ip"]}/24"
  vlan       = "/Common/${bigip_net_vlan.internal.id}"

  port_lockdown = ["none"]
}

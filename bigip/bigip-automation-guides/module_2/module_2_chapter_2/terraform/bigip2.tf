# Deploy PAYG BIG-IP 3-NIC VE instance

#########################################################################
# This is BIG-IP #2 - Availability Zone 2
#########################################################################

# Generate cloud-init script for BIG-IP
data "template_file" "bigip2_onboard" {
  template = file("${path.module}/templates/f5_onboard_3nic_custom.tmpl")
  vars = {
    bigip_hostname = var.bigip_netcfg["bigip2"]["hostname"]
    bigip_username = var.bigip_admin
    bigip_password = local.random_password

    # Device Group
    cluster_primary_ip   = local.cluster_primary_ip
    cluster_secondary_ip = local.cluster_secondary_ip
    remote_index         = local.bigip2_remote_index

    # Self IPs
    # - External self IP - Retrieved from AWS metadata service by F5 Runtime Init
    # - Internal self IP - Retrieved from AWS metadata service by F5 Runtime Init

    # Default Route
    # - Default gateway on external subnet - Retrieved from AWS metadata service by F5 Runtime Init

    # Static Route(s)
    app_route = var.vpc_cidrs["app"]["vpc"]
    # - Next hop gateway to app servers via internal subnet+AWS transit gateway - Retrieved from AWS metadata service by F5 Runtime Init

    # BIG-IP Runtime Init package URL
    INIT_URL = var.INIT_URL

    # F5 ATC package URLs and Versions
    DO_URL   = var.DO_URL
    DO_VER   = var.DO_VER
    AS3_URL  = var.AS3_URL
    AS3_VER  = var.AS3_VER
    TS_URL   = var.TS_URL
    TS_VER   = var.TS_VER
    CFE_URL  = var.CFE_URL
    CFE_VER  = var.CFE_VER
    FAST_URL = var.FAST_URL
    FAST_VER = var.FAST_VER
  }
}

# [Optional] Store local copy of the BIP-IP Runtime Init config
resource "local_file" "bigip2_f5_onboard" {
  # Set count=0 to disable
  count    = 1
  content  = data.template_file.bigip2_onboard.rendered
  filename = "${path.module}/bigip2_f5_onboard.rendered"
}

# Create BIG-IP instance
resource "aws_instance" "bigip2" {

  ami                  = data.aws_ami.bigip.id
  instance_type        = var.bigip_instance_type
  key_name             = aws_key_pair.generated_key.key_name
  iam_instance_profile = aws_iam_instance_profile.f5_cloud_failover_profile.name

  # Network interfaces
  network_interface {
    network_interface_id = aws_network_interface.bigip2_mgmt.id
    device_index         = 0
  }
  network_interface {
    network_interface_id = aws_network_interface.bigip2_external.id
    device_index         = 1
  }
  network_interface {
    network_interface_id = aws_network_interface.bigip2_internal.id
    device_index         = 2
  }

  user_data                   = data.template_file.bigip2_onboard.rendered
  user_data_replace_on_change = true

  tags = {
    Name     = format("%s_%s", var.prefix, var.bigip_netcfg["bigip2"]["tag"])
    hostname = var.bigip_netcfg["bigip2"]["hostname"]
    Owner    = var.emailid
  }

}

resource "aws_network_interface" "bigip2_mgmt" {
  description     = "NIC for BIG-IP management interface"
  subnet_id       = aws_subnet.hub_bigip2_mgmt.id
  private_ips     = [split("/", var.bigip_netcfg["bigip2"]["mgmt"])[0]]
  security_groups = [aws_security_group.f5_mgmt.id]

  tags = {
    Name  = format("%s_bigip2_mgmt", var.prefix)
    Owner = var.emailid
  }

}

resource "aws_network_interface" "bigip2_external" {
  description             = "NIC for BIG-IP external interface"
  subnet_id               = aws_subnet.hub_bigip2_external.id
  private_ip_list_enabled = true
  private_ip_list         = flatten([split("/", var.bigip_netcfg["bigip2"]["external"])[0], split("/", var.bigip_netcfg["bigip2"]["external_secondary"])[0], var.bigip_netcfg["bigip2"]["app_vips"]])
  source_dest_check       = "false"
  security_groups         = [aws_security_group.f5_external.id]

  # Cloud Failover Extension Tags
  tags = {
    Name                      = format("%s_bigip2_external", var.prefix)
    Owner                     = var.emailid
    f5_cloud_failover_label   = "mydeployment"
    f5_cloud_failover_nic_map = "external"
  }
}

resource "aws_network_interface" "bigip2_internal" {
  description       = "NIC for BIG-IP internal interface"
  subnet_id         = aws_subnet.hub_bigip2_internal.id
  private_ips       = [split("/", var.bigip_netcfg["bigip2"]["internal"])[0]]
  source_dest_check = "false"
  security_groups   = [aws_security_group.f5_internal.id]

  tags = {
    Name  = format("%s_bigip2_internal", var.prefix)
    Owner = var.emailid
  }

}

# Public IP Address for management IP (jumphost inbound access)
resource "aws_eip" "bigip2_mgmt" {
  domain            = "vpc"
  network_interface = aws_network_interface.bigip2_mgmt.id

  tags = {
    Name  = format("%s_bigip2_mgmt_eip", var.prefix)
    Owner = var.emailid
  }
}


# Outputs
output "bigip2_username" {
  value = var.bigip_admin
}

output "bigip2_password" {
  value = local.random_password
}

output "bigip2_mgmt_public_ip" {
  value = aws_eip.bigip2_mgmt.public_ip
}

output "bigip2_private_mgmt_address" {
  value = var.bigip_netcfg["bigip2"]["mgmt"]
}

output "bigip2_private_external_address" {
  value = var.bigip_netcfg["bigip2"]["external"]
}

output "bigip2_private_internal_address" {
  value = var.bigip_netcfg["bigip2"]["internal"]
}

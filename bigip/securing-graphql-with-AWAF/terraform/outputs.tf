output vpc {
  value=aws_vpc.Main.id
}

output default_sg {
	value = aws_default_security_group.automn_default.id
}

output sn1 {
	value = aws_subnet.publicsubnet1.id
}

output sn2 {
	value = aws_subnet.publicsubnet2.id
}

output sn3 {
	value = aws_subnet.publicsubnet3.id
}


# BIG-IP Management Public IP Addresses
output mgmtPublicIP {
  description = "List of BIG-IP public IP addresses for the management interfaces"
  value       = aws_eip.mgmt[0].public_ip
}

# BIG-IP Management Public DNS
output mgmtPublicDNS {
  description = "List of BIG-IP public DNS records for the management interfaces"
  value       = aws_eip.mgmt[*].public_dns
}

output f5_username {
  value = var.f5_username
}

output bigip_password {
  description = <<-EOT
 "Password for bigip user ( if dynamic_password is choosen it will be random generated password or if azure_keyvault is choosen it will be key vault secret name )"
  EOT
  value       = var.F5_PASSWORD
}

output private_addresses {
  description = "List of BIG-IP private addresses"
  value       = aws_network_interface.mgmt1.0.private_ips
}

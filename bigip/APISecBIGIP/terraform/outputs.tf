
# BIG-IP Management Public IP Addresses
output mgmtPublicIP {
  description = "List of BIG-IP public IP addresses for the management interfaces"
  value       = aws_eip.mgmt[0].public_ip
}

# BIG-IP Management Public DNS
output mgmtPublicDNS {
  description = "List of BIG-IP public DNS records for the management interfaces"
  value       = aws_eip.mgmt[0].public_dns
}

output f5_username {
  value = var.f5_username
}

output node_public_ip {
  value = aws_instance.nap[0].public_ip
}

output bigip_password {
  description = <<-EOT
 "Password for bigip user ( if dynamic_password is choosen it will be random generated password or if azure_keyvault is choosen it will be key vault secret name )"
  EOT
  value       = var.F5_PASSWORD
}

output private_addresses {
  description = "List of BIG-IP private addresses"
  value       = aws_instance.f5_bigip[0].private_ip
}

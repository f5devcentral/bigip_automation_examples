output "management_public_ip" {
  value      = aws_eip.eip_mgmt.public_ip
  depends_on = [ null_resource.wait_for_bigip_http ]
}

output "external_public_ip" {
  value      = aws_eip.eip_vip.public_ip
  depends_on = [ null_resource.wait_for_bigip_http ]
}

output "external_private_ip" {
  value      = var.vpc_cidrs["bigip"]["bigip_external_private_ip"]
  depends_on = [ null_resource.wait_for_bigip_http ]
}


output "big_ip_vs_ip" {
  value = aws_eip.eip_vip.public_ip
}
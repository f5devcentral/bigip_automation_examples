### (Re)Deploy AS3 declarations to BIG-IP

# Setup connectivity to BIG-IP #1
provider "bigip" {
  address  = aws_eip.bigip1_mgmt.public_ip
  username = var.bigip_admin
  password = local.random_password
}

# AS3 declaration files
resource "bigip_as3" "as3_config1" {
  as3_json   = file(var.as3_configs[0].as3file)
  depends_on = [aws_instance.bigip1]
}

resource "bigip_as3" "as3_config2" {
  as3_json   = file(var.as3_configs[1].as3file)
  depends_on = [aws_instance.bigip1, bigip_as3.as3_config1]
}

resource "bigip_as3" "as3_config3" {
  as3_json   = file(var.as3_configs[2].as3file)
  depends_on = [aws_instance.bigip1, bigip_as3.as3_config1, bigip_as3.as3_config2]
}

# Render ImportDevices Template File
data "template_file" "ImportDevices" {
  template   = file("./templates/importdevices_template.json")
  vars = {
    BIGIP_ADMIN_PASSWORD = local.random_password

    BIGIP1_MGMT_IP_ADDRESS      = aws_eip.bigip1_mgmt.public_ip
    BIGIP2_MGMT_IP_ADDRESS      = aws_eip.bigip2_mgmt.public_ip

  }
}


resource "local_file" "ImportDevices_rendered" {
  content    = data.template_file.ImportDevices.rendered
  filename   = "../ATC/f5extension/devices.json"
}

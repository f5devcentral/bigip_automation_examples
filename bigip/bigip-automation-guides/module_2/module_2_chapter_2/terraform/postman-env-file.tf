# Render Postman Template File
data "template_file" "postman" {
  depends_on = [null_resource.ecdsa_certs]
  template   = file("./templates/f5lab_postman_env_template.json")
  vars = {
    AWS_SECRET_ACCESS_KEY = "var.AWS_SECRET_ACCESS_KEY"
    AWS_ACCESS_KEY_ID     = "var.AWS_ACCESS_KEY_ID"
    AWS_REGION            = var.aws_region

    BIGIP_ADMIN          = var.bigip_admin
    BIGIP_ADMIN_PASSWORD = local.random_password

    BIGIP1_MGMT_IP_ADDRESS      = aws_eip.bigip1_mgmt.public_ip
    BIGIP2_MGMT_IP_ADDRESS      = aws_eip.bigip2_mgmt.public_ip
    BIGIP1_MGMT_PRIVATE_ADDRESS = var.bigip_netcfg["bigip1"]["mgmt"]
    BIGIP2_MGMT_PRIVATE_ADDRESS = var.bigip_netcfg["bigip2"]["mgmt"]

    BIGIP1_TRAFFIC_PRIVATE_ADDRESS = var.bigip_netcfg["bigip1"]["external"]
    BIGIP2_TRAFFIC_PRIVATE_ADDRESS = var.bigip_netcfg["bigip2"]["external"]

    BIGIP1_DEFAULT_ROUTE = "${cidrhost(var.vpc_cidrs["hub"]["bigip1_external"], 1)}"
    BIGIP2_DEFAULT_ROUTE = "${cidrhost(var.vpc_cidrs["hub"]["bigip2_external"], 1)}"

    BIGIP1_EXAMPLE01_ADDRESS = var.bigip_netcfg["bigip1"]["app_vips"][0]
    BIGIP1_EXAMPLE02_ADDRESS = var.bigip_netcfg["bigip1"]["app_vips"][1]
    BIGIP1_EXAMPLE03_ADDRESS = var.bigip_netcfg["bigip1"]["app_vips"][2]
    BIGIP1_EXAMPLE04_ADDRESS = var.bigip_netcfg["bigip1"]["app_vips"][3]

    BIGIP2_EXAMPLE01_ADDRESS = var.bigip_netcfg["bigip2"]["app_vips"][0]
    BIGIP2_EXAMPLE02_ADDRESS = var.bigip_netcfg["bigip2"]["app_vips"][1]
    BIGIP2_EXAMPLE03_ADDRESS = var.bigip_netcfg["bigip2"]["app_vips"][2]
    BIGIP2_EXAMPLE04_ADDRESS = var.bigip_netcfg["bigip2"]["app_vips"][3]

    EXAMPLE01A_ECDSA_CERT = fileexists("example01a.f5lab.dev.cert") ? file("example01a.f5lab.dev.cert") : "null"
    EXAMPLE01A_ECDSA_KEY  = fileexists("example01a.f5lab.dev.key") ? file("example01a.f5lab.dev.key") : "null"
    EXAMPLE01B_ECDSA_CERT = fileexists("example01b.f5lab.dev.cert") ? file("example01b.f5lab.dev.cert") : "null"
    EXAMPLE01B_ECDSA_KEY  = fileexists("example01b.f5lab.dev.key") ? file("example01b.f5lab.dev.key") : "null"

    WEB1_PRIVATE_IP_ADDRESS = var.appsvr_netcfg["appsvr1"]["eth0"]
    WEB2_PRIVATE_IP_ADDRESS = var.appsvr_netcfg["appsvr2"]["eth0"]

  }
}


resource "local_file" "postman_rendered" {
  depends_on = [null_resource.ecdsa_certs]
  content    = data.template_file.postman.rendered
  filename   = "../postman/f5lab_postman_environment.json"
}


# Variables for Postman template - set by BASH environment variables
# variable "AWS_SECRET_ACCESS_KEY" {}
# variable "AWS_ACCESS_KEY_ID" {}

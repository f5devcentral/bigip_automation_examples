resource "aws_key_pair" "ubuntu" {
  key_name   = var.EC2_KEY_NAME
  public_key = file("${var.EC2_KEY_NAME}.pub")
}

resource "aws_vpc" "Main" {                # Creating VPC here
   cidr_block       = var.main_vpc_cidr     # Defining the CIDR block use 10.0.0.0/16 for demo
   instance_tenancy = "default"
   enable_dns_hostnames = true
  tags = {
    Name = "graphql-automation-VPC"
  }
 }
 
resource "aws_default_security_group" "automn_default" {
  vpc_id = aws_vpc.Main.id
  tags = {
      Name = "graphql-automation-securitygroup"
    }
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "SSH"
    from_port   = 8443
    to_port     = 8443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "app"
    from_port   = 30000
    to_port     = 31662
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

#Create Internet Gateway and attach it to VPC
resource "aws_internet_gateway" "IGW" {    # Creating Internet Gateway
    vpc_id =  aws_vpc.Main.id               # vpc_id will be generated after we create VPC
  tags = {
    Name = "graphql-automation-IGW"
  }
}
 
#Create a Public Subnet1
resource "aws_subnet" "publicsubnet1" {    # Creating Public Subnets
   vpc_id =  aws_vpc.Main.id
   cidr_block = var.mgmt_subnet1      # CIDR block of public subnets
   map_public_ip_on_launch = true
   availability_zone = "${var.region}a"
  tags = {
    Name = "graphql-automation-SN1"
  }
}
 
#Create a Public Subnet2
resource "aws_subnet" "publicsubnet2" {
   vpc_id =  aws_vpc.Main.id
   cidr_block = var.public_subnet2         # CIDR block of subnet2
   map_public_ip_on_launch = true
      availability_zone = "${var.region}a"
   tags = {
    Name = "graphql-automation-SN2"
  }
}

#Create a Public Subnet3
resource "aws_subnet" "publicsubnet3" {
   vpc_id =  aws_vpc.Main.id
   cidr_block = var.private_subnet3         # CIDR block of subnet3
   map_public_ip_on_launch = true
   availability_zone = "${var.region}b"
   tags = {
    Name = "graphql-automation-SN3"
  }
}

# Route table for Public Subnets
resource "aws_route_table" "PublicRT" {    # Creating RT for Public Subnet
    vpc_id =  aws_vpc.Main.id
         route {
    cidr_block = "0.0.0.0/0"               # Traffic from Public Subnet reaches Internet via Internet Gateway
    gateway_id = aws_internet_gateway.IGW.id
     }
  tags = {
    Name = "graphql-automation-RT"
  }
}

# Route table Association with Public Subnet's
resource "aws_route_table_association" "PublicRTassociation" {
    subnet_id = aws_subnet.publicsubnet1.id
    route_table_id = aws_route_table.PublicRT.id
}
 
# Route table Association with Subnet 2
resource "aws_route_table_association" "PublicRTassociation2" {
    subnet_id = aws_subnet.publicsubnet2.id
    route_table_id = aws_route_table.PublicRT.id
}

# Route table Association with Subnet 3
resource "aws_route_table_association" "PublicRTassociation3" {
    subnet_id = aws_subnet.publicsubnet3.id
    route_table_id = aws_route_table.PublicRT.id
}


# EKS deployment code
data "aws_eks_cluster" "cluster" {
  name = module.my-cluster.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.my-cluster.cluster_id
}


module "my-cluster" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "automation-eks-cluster"
  vpc_id       = aws_vpc.Main.id
  cluster_version = "1.25"
  version = "17.24.0"
  subnets      = [aws_subnet.publicsubnet1.id, aws_subnet.publicsubnet2.id, aws_subnet.publicsubnet3.id]
  worker_groups = [
    {
      instance_type = "m4.large"
      asg_max_size  = 1
    }
  ]
}

provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
  token                  = data.aws_eks_cluster_auth.cluster.token
  load_config_file       = false
  version                = "~> 1.9"
}


# BIGIP deployment
# below code is for BIGIP component
terraform {
  required_version = ">= 0.13"
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = ">2.3.0"
    }
    template = {
      source  = "hashicorp/template"
      version = ">2.1.2"
    }
    null = {
      source  = "hashicorp/null"
      version = ">2.1.2"
    }
    bigip = {
      source = "F5Networks/bigip"
      version = "1.8.0"
    }

  }
}

data "aws_ami" "bigip_ami" {
  most_recent = true
  owners = ["679593333241"]

  filter {
    name   = "name"
    values = [var.bigip_ami_name]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }
}


 resource "aws_security_group" "sg1" {
  vpc_id = aws_vpc.Main.id
  tags = {
      Name = "graphql-automation-securitygroup1"
    }

  ingress {
    description = "bigipui"
    from_port   = 8443
    to_port     = 8443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "app"
    from_port   = 30000
    to_port     = 31662
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

 resource "aws_security_group" "sg2" {
  vpc_id = aws_vpc.Main.id
  tags = {
      Name = "graphql-automation-securitygroup2"
    }

  ingress {
    description = "bigipui"
    from_port   = 8443
    to_port     = 8443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "app"
    from_port   = 30000 
    to_port     = 31662
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

locals {
  bigip_map = {
    "mgmt_subnet_ids"            = [{ "subnet_id" = aws_subnet.publicsubnet1.id, "public_ip" = null, "private_ip_primary" = null }]
    "mgmt_securitygroup_ids"     = [aws_default_security_group.automn_default.id]
    "external_subnet_ids"        = [{ "subnet_id" = aws_subnet.publicsubnet2.id, "public_ip" = null, "private_ip_primary" = null, "private_ip_secondary" = null }]
    "external_securitygroup_ids" = [aws_security_group.sg1.id]
    "internal_subnet_ids"        = [{ "subnet_id" = aws_subnet.publicsubnet3.id, "public_ip" = null, "private_ip_primary" = null }]
    "internal_securitygroup_ids" = [aws_security_group.sg2.id]
  }
  mgmt_public_subnet_id = [
    for subnet in local.bigip_map["mgmt_subnet_ids"] :
    subnet["subnet_id"]
    if subnet["public_ip"] == true
  ]
  mgmt_public_index = [
    for index, subnet in local.bigip_map["mgmt_subnet_ids"] :
    index
    if subnet["public_ip"] == true
  ]
  mgmt_public_security_id = [
    for i in local.mgmt_public_index : local.bigip_map["mgmt_securitygroup_ids"][i]
  ]
  mgmt_private_subnet_id = [
    for subnet in local.bigip_map["mgmt_subnet_ids"] :
    subnet["subnet_id"]
    if subnet["public_ip"] == false
  ]
  mgmt_private_index = [
    for index, subnet in local.bigip_map["mgmt_subnet_ids"] :
    index
    if subnet["public_ip"] == false
  ]
  mgmt_private_security_id = [
    for i in local.mgmt_private_index : local.bigip_map["mgmt_securitygroup_ids"][i]
  ]
  external_public_subnet_id = [
    for subnet in local.bigip_map["external_subnet_ids"] :
    subnet["subnet_id"]
    if subnet["public_ip"] == true
  ]
  external_public_index = [
    for index, subnet in local.bigip_map["external_subnet_ids"] :
    index
    if subnet["public_ip"] == true
  ]
  external_public_security_id = [
    for i in local.external_public_index : local.bigip_map["external_securitygroup_ids"][i]
  ]
  external_private_subnet_id = [
    for subnet in local.bigip_map["external_subnet_ids"] :
    subnet["subnet_id"]
    if subnet["public_ip"] == false
  ]
  external_private_index = [
    for index, subnet in local.bigip_map["external_subnet_ids"] :
    index
    if subnet["public_ip"] == false
  ]
  external_private_security_id = [
    for i in local.external_private_index : local.bigip_map["external_securitygroup_ids"][i]
  ]
  internal_public_subnet_id = [
    for subnet in local.bigip_map["internal_subnet_ids"] :
    subnet["subnet_id"]
    if subnet["public_ip"] == true
  ]
  internal_public_index = [
    for index, subnet in local.bigip_map["internal_subnet_ids"] :
    index
    if subnet["public_ip"] == true
  ]
  internal_public_security_id = [
    for i in local.internal_public_index : local.bigip_map["internal_securitygroup_ids"][i]
  ]
  internal_private_subnet_id = [
    for subnet in local.bigip_map["internal_subnet_ids"] :
    subnet["subnet_id"]
    if subnet["public_ip"] == false
  ]
  internal_private_index = [
    for index, subnet in local.bigip_map["internal_subnet_ids"] :
    index
    if subnet["public_ip"] == false
  ]
  internal_private_security_id = [
    for i in local.internal_private_index : local.bigip_map["internal_securitygroup_ids"][i]
  ]
 internal_private_ip_primary = [
    for private in local.bigip_map["internal_subnet_ids"] :
    private["private_ip_primary"]
    if private["public_ip"] == false
  ]
  external_private_ip_primary = [
    for private in local.bigip_map["external_subnet_ids"] :
    private["private_ip_primary"]
    if private["public_ip"] == false
  ]
  external_private_ip_secondary = [
    for private in local.bigip_map["external_subnet_ids"] :
    private["private_ip_secondary"]
    if private["public_ip"] == false
  ]
  external_public_private_ip_primary = [
    for private in local.bigip_map["external_subnet_ids"] :
    private["private_ip_primary"]
    if private["public_ip"] == true
  ]
  external_public_private_ip_secondary = [
    for private in local.bigip_map["external_subnet_ids"] :
    private["private_ip_secondary"]
    if private["public_ip"] == true
  ]
  mgmt_private_ip_primary = [
    for private in local.bigip_map["mgmt_subnet_ids"] :
    private["private_ip_primary"]
    if private["public_ip"] == false
  ]
  #mgmt_public_private_ip_primary = ["10.1.1.94"]
  mgmt_public_private_ip_primary = [
    for private in local.bigip_map["mgmt_subnet_ids"] :
    private["private_ip_primary"]
    if private["public_ip"] == true
  ]

  total_nics       = length(concat(local.mgmt_public_subnet_id, local.mgmt_private_subnet_id, local.external_public_subnet_id, local.external_private_subnet_id, local.internal_public_subnet_id, local.internal_private_subnet_id))
  vlan_list        = concat(local.external_public_subnet_id, local.external_private_subnet_id, local.internal_public_subnet_id, local.internal_private_subnet_id)
  selfip_list_temp = concat(aws_network_interface.public.*.private_ip, aws_network_interface.external_private.*.private_ip, aws_network_interface.private.*.private_ip, aws_network_interface.public1.*.private_ip, aws_network_interface.external_private1.*.private_ip, aws_network_interface.private1.*.private_ip)
  ext_interfaces   = concat(aws_network_interface.public.*.id, aws_network_interface.public1.*.id, aws_network_interface.external_private.*.id, aws_network_interface.external_private1.*.id)
  selfip_list      = flatten(local.selfip_list_temp)
  //bigip_nics       = concat(aws_network_interface.public.*.id, aws_network_interface.external_private.*.id,aws_network_interface.private.*.id)
  //bigip_nics_map   = concat(data.aws_network_interfaces.bigip_nic.*.private_ip)
  instance_prefix = format("%s-%s", var.prefix, random_id.module_id.hex)

}

#
# Create a random id
#
resource random_id module_id {
  byte_length = 2
}

#
# Create random password for BIG-IP
#
resource random_string dynamic_password {
  //count = var.f5_password == null ? 1 : 0
  length      = 16
  min_upper   = 1
  min_lower   = 1
  min_numeric = 1
  special     = false
}

#
# Ensure Secret exists
#
data "aws_secretsmanager_secret" "password" {
  count = var.aws_secretmanager_auth ? 1 : 0
  name  = var.aws_secretmanager_secret_id
}

data "aws_secretsmanager_secret_version" "current" {
  count     = var.aws_secretmanager_auth ? 1 : 0
  secret_id = data.aws_secretsmanager_secret.password[count.index].id
  //depends_on =[data.aws_secretsmanager_secret.password]
}


#
# Create Management Network Interfaces
#
#This resource is for static  primary and secondary private ips 
resource "aws_network_interface" "mgmt" {
  count           = length(compact(local.mgmt_public_private_ip_primary)) > 0 ? length(local.bigip_map["mgmt_subnet_ids"]) : 0
  subnet_id       = local.bigip_map["mgmt_subnet_ids"][count.index]["subnet_id"]
  private_ips     = [local.mgmt_public_private_ip_primary[count.index]]
  security_groups = local.bigip_map["mgmt_securitygroup_ids"]
  tags = {
    Name   = format("%s-%d", "BIGIP-Managemt-Interface", count.index)
    Prefix = format("%s", local.instance_prefix)
  }
}

#This resource is for dynamic  primary and secondary private ips  
resource "aws_network_interface" "mgmt1" {
  count             = length(compact(local.mgmt_public_private_ip_primary)) > 0 ? 0 : length(local.bigip_map["mgmt_subnet_ids"])
  subnet_id         = local.bigip_map["mgmt_subnet_ids"][count.index]["subnet_id"]
  security_groups   = local.bigip_map["mgmt_securitygroup_ids"]
  private_ips_count = 0
  tags = {
    Name   = format("%s-%d", "BIGIP-Managemt-Interface", count.index)
    Prefix = format("%s", local.instance_prefix)
  }
}

#
# add an elastic IP to the BIG-IP management interface
#
resource "aws_eip" "mgmt" {
  count = length(local.bigip_map["mgmt_subnet_ids"])
  #network_interface = aws_network_interface.mgmt[count.index].id
  network_interface = length(compact(local.mgmt_public_private_ip_primary)) > 0 ? aws_network_interface.mgmt[count.index].id : aws_network_interface.mgmt1[count.index].id
  vpc               = true
}

#
# add an elastic IP to the BIG-IP External Public interface
#
resource "aws_eip" "ext-pub" {
  count = length(local.external_public_subnet_id)
  #network_interface = aws_network_interface.public[count.index].id
  network_interface = length(compact(local.external_public_private_ip_primary)) > 0 ? aws_network_interface.public[count.index].id : aws_network_interface.public1[count.index].id
  vpc               = true
  depends_on        = [aws_eip.mgmt]
}

#
# Create Public External Network Interfaces
#
#This resource is for static  primary and secondary private ips

resource "aws_network_interface" "public" {
  count = length(compact(local.external_public_private_ip_primary)) > 0 ? length(local.external_public_subnet_id) : 0
  #count             = length(local.external_public_subnet_id)
  subnet_id         = local.external_public_subnet_id[count.index]
  security_groups   = local.bigip_map["external_securitygroup_ids"]
  private_ips       = [local.external_public_private_ip_primary[count.index], local.external_public_private_ip_secondary[count.index]]
  source_dest_check = var.external_source_dest_check
  # private_ips_count = 1
  tags = {
    Name   = format("%s-%d", "BIGIP-External-Public-Interface", count.index)
    Prefix = format("%s", local.instance_prefix)
  }
}

#This resource is for dynamic  primary and secondary private ips

resource "aws_network_interface" "public1" {
  count = length(compact(local.external_public_private_ip_primary)) > 0 ? 0 : length(local.external_public_subnet_id)
  #count             = length(local.external_public_subnet_id)
  subnet_id         = local.external_public_subnet_id[count.index]
  security_groups   = local.bigip_map["external_securitygroup_ids"]
  source_dest_check = var.external_source_dest_check
  private_ips_count = 1
  tags = {
    Name   = format("%s-%d", "BIGIP-External-Public-Interface", count.index)
    Prefix = format("%s", local.instance_prefix)
  }
}

#
# Create Private External Network Interfaces
#
#This resource is for static  primary and secondary private ips

resource "aws_network_interface" "external_private" {
  count = length(compact(local.external_private_ip_primary)) > 0 ? length(local.external_private_subnet_id) : 0
  # count             = length(local.external_private_subnet_id)
  subnet_id       = local.external_private_subnet_id[count.index]
  security_groups = local.bigip_map["external_securitygroup_ids"]
  private_ips     = [local.external_private_ip_primary[count.index], local.external_private_ip_secondary[count.index]]
   #  private_ips_count = 1
  tags = {
    Name   = format("%s-%d", "BIGIP-External-Private-Interface", count.index)
    Prefix = format("%s", local.instance_prefix)
  }
}

#This resource is for dynamic  primary and secondary private ips

resource "aws_network_interface" "external_private1" {
  count = length(compact(local.external_private_ip_primary)) > 0 ? 0 : length(local.external_private_ip_primary)
  #count             = length(local.external_private_subnet_id)
  subnet_id         = local.external_private_subnet_id[count.index]
  security_groups   = local.bigip_map["external_securitygroup_ids"]
  private_ips_count = 1
  tags = {
    Name   = format("%s-%d", "BIGIP-External-Private-Interface", count.index)
    Prefix = format("%s", local.instance_prefix)
  }
}
#
# Create Private Network Interfaces
#
#This resource is for static  primary and secondary private ips

resource "aws_network_interface" "private" {
  count             = length(compact(local.internal_private_ip_primary)) > 0 ? length(local.internal_private_subnet_id) : 0
  subnet_id         = local.internal_private_subnet_id[count.index]
  security_groups   = local.bigip_map["internal_securitygroup_ids"]
  private_ips       = [local.internal_private_ip_primary[count.index]]
  source_dest_check = var.internal_source_dest_check
  tags = {
    Name   = format("%s-%d", "BIGIP-Internal-Interface", count.index)
    Prefix = format("%s", local.instance_prefix)
  }
}

#This resource is for dynamic  primary and secondary private ips

resource "aws_network_interface" "private1" {
  count             = length(compact(local.internal_private_ip_primary)) > 0 ? 0 : length(local.internal_private_subnet_id)
  subnet_id         = local.internal_private_subnet_id[count.index]
  security_groups   = local.bigip_map["internal_securitygroup_ids"]
  private_ips_count = 0
  source_dest_check = var.internal_source_dest_check
  tags = {
    Name   = format("%s-%d", "BIGIP-Internal-Interface", count.index)
    Prefix = format("%s", local.instance_prefix)
  }
}

data "template_file" "user_data_vm0" {
  template = file("${path.module}/f5_onboard.tmpl")
  vars = {
    bigip_username         = var.f5_username
   aws_secretmanager_auth = var.aws_secretmanager_auth
    bigip_password         = var.F5_PASSWORD
    INIT_URL               = var.INIT_URL,
    DO_URL                 = var.DO_URL,
    DO_VER                 = split("/", var.DO_URL)[7]
    AS3_URL                = var.AS3_URL,
    AS3_VER                = split("/", var.AS3_URL)[7]
    TS_VER                 = split("/", var.TS_URL)[7]
    TS_URL                 = var.TS_URL,
    CFE_VER                = split("/", var.CFE_URL)[7]
    CFE_URL                = var.CFE_URL,
    FAST_URL               = var.FAST_URL
  }
}

resource "null_resource" "delay" {
  provisioner "local-exec" {
    command = "sleep 30"
  }
}

# Deploy BIG-IP
#
resource "aws_instance" "f5_bigip" {
  # determine the number of BIG-IPs to deploy
  count         = var.f5_instance_count
  instance_type = var.ec2_instance_type
  ami           = data.aws_ami.bigip_ami.id
  key_name = var.EC2_KEY_NAME
  root_block_device {
    delete_on_termination = true
  }

  # set the mgmt interface
  dynamic "network_interface" {
    #for_each = toset([aws_network_interface.mgmt[count.index].id])
    for_each = length(compact(local.mgmt_public_private_ip_primary)) > 0 ? toset([aws_network_interface.mgmt[count.index].id]) : toset([aws_network_interface.mgmt1[count.index].id])
    content {
      network_interface_id = network_interface.value
      device_index         = 0
    }
  }

  # set the public interface only if an interface is defined
  dynamic "network_interface" {
    for_each = length(local.ext_interfaces) > count.index ? toset(local.ext_interfaces) : toset([])
    //for_each = length(aws_network_interface.public) > count.index ? toset([aws_network_interface.public[count.index].id]) : toset([])

    content {
      network_interface_id = network_interface.value
      device_index         = 1 + index(tolist(toset(local.ext_interfaces)), network_interface.value)
    }
  }

  # set the private interface only if an interface is defined
  dynamic "network_interface" {
    for_each = length(aws_network_interface.private) > count.index ? toset([aws_network_interface.private[count.index].id]) : toset([])

    content {
      network_interface_id = network_interface.value
      device_index         = (length(local.ext_interfaces) + 1) + index(tolist(toset([aws_network_interface.private[count.index].id])), network_interface.value)
    }
  }

  dynamic "network_interface" {
    for_each = length(aws_network_interface.private1) > count.index ? toset([aws_network_interface.private1[count.index].id]) : toset([])

    content {
      network_interface_id = network_interface.value
      device_index         = (length(local.ext_interfaces) + 1) + index(tolist(toset([aws_network_interface.private1[count.index].id])), network_interface.value)
    }
  }
  iam_instance_profile = var.aws_iam_instance_profile
  user_data            = data.template_file.user_data_vm0.rendered
  
  provisioner "local-exec" {
       command = "sleep 300"
  }
  tags = {
    Name = "graphql-automation-BIGIP"
  }
  depends_on = [aws_eip.mgmt, aws_network_interface.public, aws_network_interface.private, null_resource.delay]
}

data template_file clustermemberDO1 {
  count    = local.total_nics == 1 ? 1 : 0
  template = file("${path.module}/onboard_do_1nic.tpl")
  vars = {
    hostname      = aws_eip.mgmt[0].public_dns
    name_servers  = join(",", formatlist("\"%s\"", ["169.254.169.253"]))
    search_domain = "f5.com"
    ntp_servers   = join(",", formatlist("\"%s\"", ["169.254.169.123"]))
  }
}

resource "null_resource" "launch_site" {
connection {
    #private_key = file("../terraform/key_pair.pem")
    type     = "ssh"
    user     = "admin"
    password = var.F5_PASSWORD
    host     = aws_instance.f5_bigip[0].public_ip
  }


  provisioner "remote-exec" {
    inline = [
    "tmsh modify sys provision asm { level nominal }",
    "tmsh save sys config",
    ]
 }
 provisioner "local-exec" {
    command = "sleep 90"
  }

}
resource "local_file" "host_new_cfg" {
  content = templatefile("hosts.tmpl",
    {
      ansible_host = aws_eip.mgmt[*].public_ip
    }
  )
  filename = "../ansible/inventory/hosts"
}

resource "local_file" "host_cfg" {
  content = templatefile("host_ansible.tmpl",
    {
      ansible_host = aws_eip.mgmt[*].public_ip
    }
  )
  
  filename = "../ansible/host_vars/bigip01.internal.yaml"
}

resource "local_file" "vip" {
  content = "${aws_eip.mgmt[0].public_ip}"
  filename = "../ansible/vip"
}

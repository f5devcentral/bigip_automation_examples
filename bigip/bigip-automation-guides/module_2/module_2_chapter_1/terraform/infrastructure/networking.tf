resource "aws_vpc" "vpc" {
  cidr_block = var.vpc_cidrs["bigip"]["vpc"]

  tags = var.tags
}

resource "aws_internet_gateway" "default" {
  vpc_id = aws_vpc.vpc.id

  tags = var.tags
}

resource "aws_subnet" "mgmt" {
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = var.vpc_cidrs["bigip"]["bigip_mgmt"]
  map_public_ip_on_launch = true
  availability_zone       = var.availability_zone

  tags = var.tags
}

resource "aws_subnet" "external" {
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = var.vpc_cidrs["bigip"]["bigip_external"]
  map_public_ip_on_launch = true
  availability_zone       = var.availability_zone

  tags = var.tags
}

resource "aws_subnet" "internal" {
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = var.vpc_cidrs["bigip"]["bigip_internal"]
  map_public_ip_on_launch = true
  availability_zone       = var.availability_zone

  tags = var.tags
}

resource "aws_route" "internet_access" {
  route_table_id         = aws_vpc.vpc.main_route_table_id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.default.id
}

resource "aws_route_table_association" "route_table_external" {
  subnet_id      = aws_subnet.external.id
  route_table_id = aws_vpc.vpc.main_route_table_id
}

resource "aws_route_table_association" "route_table_internal" {
  subnet_id      = aws_subnet.internal.id
  route_table_id = aws_vpc.vpc.main_route_table_id
}

resource "aws_network_interface" "mgmt" {
  subnet_id       = aws_subnet.mgmt.id
  private_ips     = [var.vpc_cidrs["bigip"]["bigip_mgmt_private_ip"]]
  security_groups = ["${aws_security_group.mgmt.id}"]

  tags = var.tags
}

resource "aws_network_interface" "external" {
  subnet_id       = aws_subnet.external.id
  private_ips     = [var.vpc_cidrs["bigip"]["bigip_external_private_ip"]]
  security_groups = ["${aws_security_group.external.id}"]

  tags = var.tags
}

resource "aws_network_interface" "internal" {
  subnet_id       = aws_subnet.internal.id
  private_ips     = [var.vpc_cidrs["bigip"]["bigip_internal_private_ip"]]
  security_groups = ["${aws_security_group.internal.id}"]

  tags = var.tags
}

resource "aws_eip" "eip_vip" {
  network_interface         = aws_network_interface.external.id
  associate_with_private_ip = var.vpc_cidrs["bigip"]["bigip_external_private_ip"]

  tags = var.tags
}

resource "aws_eip" "eip_mgmt" {
  network_interface         = aws_network_interface.mgmt.id
  associate_with_private_ip = var.vpc_cidrs["bigip"]["bigip_mgmt_private_ip"]

  tags = var.tags
}
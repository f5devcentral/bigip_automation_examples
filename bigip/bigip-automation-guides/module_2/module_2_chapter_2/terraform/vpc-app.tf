# Application VPC
resource "aws_vpc" "app-vpc" {
  cidr_block           = var.vpc_cidrs["app"]["vpc"]
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "true"

  tags = {
    Name  = format("%s_app_vpc", var.prefix)
    Owner = var.emailid
  }
}

# AZ 1 - Subnets
resource "aws_subnet" "appsvr1" {
  vpc_id                  = aws_vpc.app-vpc.id
  cidr_block              = var.vpc_cidrs["app"]["appsvr1"]
  map_public_ip_on_launch = "false"
  availability_zone       = format("%sa", var.aws_region)

  tags = {
    Name  = format("%s_app_az1_subnet", var.prefix)
    Owner = var.emailid
  }
}

# AZ 2 - Subnets
resource "aws_subnet" "appsvr2" {
  vpc_id                  = aws_vpc.app-vpc.id
  cidr_block              = var.vpc_cidrs["app"]["appsvr2"]
  map_public_ip_on_launch = "false"
  availability_zone       = format("%sb", var.aws_region)

  tags = {
    Name  = format("%s_app_az2_subnet", var.prefix)
    Owner = var.emailid
  }
}

# Route Table
resource "aws_route_table" "app_default_tgw" {
  vpc_id = aws_vpc.app-vpc.id

  route {
    cidr_block         = "0.0.0.0/0"
    transit_gateway_id = aws_ec2_transit_gateway.tgw.id
  }

  tags = {
    Name  = format("%s_app_default_tgw_rt", var.prefix)
    Owner = var.emailid
  }


}

resource "aws_main_route_table_association" "app" {
  vpc_id         = aws_vpc.app-vpc.id
  route_table_id = aws_route_table.app_default_tgw.id
}

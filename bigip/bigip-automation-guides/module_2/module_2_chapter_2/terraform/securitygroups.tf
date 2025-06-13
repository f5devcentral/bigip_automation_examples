# Security Groups

# BIG-IP management subnets ACL
resource "aws_security_group" "f5_mgmt" {
  name   = format("%s_f5_mgmt_sg", var.prefix)
  vpc_id = aws_vpc.hub-vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [format("%s/32", data.http.myip.response_body)]
  }

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [var.vpc_cidrs["hub"]["vpc"]]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name  = format("%s_f5_mgmt_sg", var.prefix)
    Owner = var.emailid
  }
}

# BIG-IP external subnets ACL
resource "aws_security_group" "f5_external" {
  name   = format("%s_f5_external_sg", var.prefix)
  vpc_id = aws_vpc.hub-vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [format("%s/32", data.http.myip.response_body)]
  }

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [var.vpc_cidrs["hub"]["vpc"]]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name  = format("%s_f5_external_sg", var.prefix)
    Owner = var.emailid
  }
}

# BIG-IP internal subnets ACL
resource "aws_security_group" "f5_internal" {
  name   = format("%s_f5_internal_sg", var.prefix)
  vpc_id = aws_vpc.hub-vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [var.vpc_cidrs["hub"]["vpc"], var.vpc_cidrs["app"]["vpc"]]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name  = format("%s_f5_internal_sg", var.prefix)
    Owner = var.emailid
  }
}


# App server access
resource "aws_security_group" "appservers" {
  name   = format("%s_appsvr_sg", var.prefix)
  vpc_id = aws_vpc.app-vpc.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8
    to_port     = 0
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name  = format("%s_f5_appsvr_sg", var.prefix)
    Owner = var.emailid
  }
}


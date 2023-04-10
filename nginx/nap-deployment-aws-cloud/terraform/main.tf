resource "aws_key_pair" "ubuntu" {
  key_name   = var.EC2_KEY_NAME
  public_key = file("${var.EC2_KEY_NAME}.pub")
}

resource "aws_vpc" "Main" {                # Creating VPC here
   cidr_block       = var.main_vpc_cidr     # Defining the CIDR block to use
   instance_tenancy = "default"
   enable_dns_hostnames = true
  tags = {
    Name = "apisecurity-automation-VPC"
  }
 }
 
resource "aws_default_security_group" "automn_default" {
  vpc_id = aws_vpc.Main.id
  tags = {
      Name = "apisecurity-automation-securitygroup"
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
    description = "app"
    from_port   = 8080
    to_port     = 8080
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
    Name = "apisecurity-automation-IGW"
  }
}
 
#Create a Public Subnet1
resource "aws_subnet" "publicsubnet1" {    # Creating Public Subnets
   vpc_id =  aws_vpc.Main.id
   cidr_block = var.mgmt_subnet1      # CIDR block of public subnets
   map_public_ip_on_launch = true
   availability_zone = "ap-south-1a"
  tags = {
    Name = "apisecurity-automation-SN1"
  }
}
 
#Create a Public Subnet2
resource "aws_subnet" "publicsubnet2" {
   vpc_id =  aws_vpc.Main.id
   cidr_block = var.public_subnet2         # CIDR block of subnet2
   map_public_ip_on_launch = true
      availability_zone = "ap-south-1a"
   tags = {
    Name = "apisecurity-automation-SN2"
  }
}

#Create a Public Subnet3
resource "aws_subnet" "publicsubnet3" {
   vpc_id =  aws_vpc.Main.id
   cidr_block = var.private_subnet3         # CIDR block of subnet3
   map_public_ip_on_launch = true
   availability_zone = "ap-south-1b"
   tags = {
    Name = "apisecurity-automation-SN3"
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
    Name = "apisecurity-automation-RT"
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

terraform {
  required_version = "~> 1.3.3"
  required_providers {
    template = {
      source  = "hashicorp/template"
      version = ">2.1.2"
    }
    null = {
      source  = "hashicorp/null"
      version = ">2.1.2"
    }
  }
}

data "aws_ami" "nap_ami" {
  most_recent = true
  owners = ["679593333241"]

  filter {
    name   = "name"
    values = [var.NAP_image_name]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_security_group" "sg1" {
  vpc_id = aws_vpc.Main.id
  tags = {
      Name = "apisecurity-automation-securitygroup1"
    }
  ingress {
    description = "app"
    from_port   = 8080
    to_port     = 8080
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
      Name = "apisecurity-automation-securitygroup2"
    }
  ingress {
    description = "app"
    from_port   = 8080
    to_port     = 8080
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

resource "aws_instance" "nap" {
  key_name      = aws_key_pair.ubuntu.key_name
  count         = 2
  instance_type = "t3.large"
  ami           = data.aws_ami.nap_ami.id
  tags = {
    Name = "apisecurity-automation-nap"
	  role = "application"
  }
  subnet_id = aws_subnet.publicsubnet1.id
  vpc_security_group_ids = [aws_default_security_group.automn_default.id]
  user_data = "${file("user_data.sh")}"
}

# below code is for ALB 
resource "aws_lb" "alb" {
  name               = "automation-alb"
  internal           = false
  load_balancer_type = "application" 
  security_groups    = [aws_default_security_group.automn_default.id]
  subnets            = [aws_subnet.publicsubnet1.id, aws_subnet.publicsubnet3.id]
  enable_cross_zone_load_balancing = "true"
  tags = {
    Environment = "testing"
    Name        = "automation-alb"
  }
}

resource "aws_lb_target_group" "tg" {
  name               = "automation-alb"
  target_type        = "instance"
  port               = 80
  protocol           = "HTTP"
  vpc_id             = aws_vpc.Main.id
  health_check {
    healthy_threshold   = var.health_check["healthy_threshold"]
    interval            = var.health_check["interval"]
    unhealthy_threshold = var.health_check["unhealthy_threshold"]
    timeout             = var.health_check["timeout"]
    path                = var.health_check["path"]
    port                = var.health_check["port"]
}
}

resource "aws_lb_target_group_attachment" "tg_attachment_test" {
  target_group_arn = aws_lb_target_group.tg.arn
  target_id        = aws_instance.nap[0].id
  port             = 80
}
resource "aws_lb_target_group_attachment" "tg_attachment_test2" {
  target_group_arn = aws_lb_target_group.tg.arn
  target_id        = aws_instance.nap[1].id
  port             = 80
}

resource "aws_lb_listener" "lb_listener_http" {
  load_balancer_arn    = aws_lb.alb.arn
  port                 = "80"
  protocol             = "HTTP"
  default_action {
  target_group_arn = aws_lb_target_group.tg.arn
  type             = "forward"
  }
}

# save IP and DNS details in below files
resource "local_file" "nap1" {
  content = "${aws_instance.nap[0].public_ip}"
  filename = "./nap1"
}
resource "local_file" "nap2" {
  content = "${aws_instance.nap[1].public_ip}"
  filename = "./nap2"
}
resource "local_file" "alb" {
  content = "${aws_lb.alb.dns_name}"
  filename = "./alb_dns"
}
resource "local_file" "napid1" {
  content = "${aws_instance.nap[0].id}"
  filename = "./ins1"
}
resource "local_file" "napid2" {
  content = "${aws_instance.nap[1].id}"
  filename = "./ins2"
}

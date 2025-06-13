resource "aws_instance" "webserver_1" {
  ami                         = "ami-04f7a54071e74f488"
  instance_type               = "t2.micro"
  key_name                    = var.aws_key_name

  subnet_id                   = aws_subnet.external.id
  associate_public_ip_address = true
  private_ip                  = "10.0.12.101"
  security_groups             = [aws_security_group.webserver.id]

  user_data = <<-EOF
    #!/bin/bash
    apt-get update -y
    apt-get install -y nginx
  EOF
  
  tags = merge(var.tags, { "Name" = "webserver_1" })
}

resource "aws_instance" "webserver_2" {
  ami                         = "ami-04f7a54071e74f488"
  instance_type               = "t2.micro"
  key_name                    = var.aws_key_name

  subnet_id                   = aws_subnet.external.id
  associate_public_ip_address = true
  private_ip                  = "10.0.12.102"
  security_groups             = [aws_security_group.webserver.id]

  user_data = <<-EOF
    #!/bin/bash
    apt-get update -y
    apt-get install -y nginx
  EOF
  
  tags = merge(var.tags, { "Name" = "webserver_2" })
}

resource "aws_security_group" "webserver" {
  name        = "webserver"
  description = "allow http access to the webserver"
  vpc_id      = aws_vpc.vpc.id

  ingress {
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
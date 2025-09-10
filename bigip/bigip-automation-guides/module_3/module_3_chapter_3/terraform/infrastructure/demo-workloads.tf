

resource "aws_instance" "webserver_2" {
  ami                         = "ami-04f7a54071e74f488"
  instance_type               = "t2.micro"
  key_name                    = var.aws_key_name

  network_interface {
    network_interface_id = aws_network_interface.webserver_2.id
    device_index         = 0
  }


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

resource "aws_network_interface" "webserver_1" {
  subnet_id       = aws_subnet.internal.id
  private_ips     = ["10.0.11.101"]
  security_groups = ["${aws_security_group.webserver.id}"]

  tags = var.tags
}

resource "aws_network_interface" "webserver_2" {
  subnet_id       = aws_subnet.internal.id
  private_ips     = ["10.0.11.102"]
  security_groups = ["${aws_security_group.webserver.id}"]

  tags = var.tags
}

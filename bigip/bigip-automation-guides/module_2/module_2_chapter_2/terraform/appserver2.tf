# Deploy PAYG linux server instance for web application

#########################################################################
# This is App Server #2 - Availability Zone 2
#########################################################################

resource "aws_instance" "appsvr2" {
  ami                         = data.aws_ami.linux.id
  instance_type               = var.linux_instance_type
  subnet_id                   = aws_subnet.appsvr2.id
  vpc_security_group_ids      = [aws_security_group.appservers.id]
  key_name                    = aws_key_pair.generated_key.key_name
  private_ip                  = var.appsvr_netcfg["appsvr2"]["eth0"]
  associate_public_ip_address = false
  depends_on                  = [aws_ec2_transit_gateway_vpc_attachment.hub-vpc, aws_ec2_transit_gateway_vpc_attachment.app-vpc, aws_nat_gateway.hub_ngw, aws_internet_gateway.hub_igw, aws_route_table_association.hub_internal_ngw_az1, aws_route_table_association.hub_internal_ngw_az2, aws_main_route_table_association.hub]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              /sbin/chkconfig --add docker
              service docker start
              docker run -d --net host -e F5DEMO_APP=website -e F5DEMO_NODENAME="App Server 2 - AZ #2" --restart always --name f5demoapp chen23/f5-demo-app:latest
              EOF

  tags = {
    Name   = format("%s_appsvr2_etho", var.prefix)
    Owner  = var.emailid
    findme = "web"
  }

}


output "appsvr2_private_address" {
  value = aws_instance.appsvr2.private_ip
}

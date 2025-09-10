# NAT Gateway for outbound Internet access from private IPs

resource "aws_eip" "hub_ngw" {
  domain = "vpc"
}

# Note: NAT Gateway deployed into a single AZ to simplify this lab. Recommended practice is to
# deploy a NAT Gateway per AZ for fault tolerance.
resource "aws_nat_gateway" "hub_ngw" {
  allocation_id = aws_eip.hub_ngw.id
  subnet_id     = aws_subnet.hub_bigip1_mgmt.id

  tags = {
    Name  = format("%s_hub_ngw", var.prefix)
    Owner = var.emailid
  }
}

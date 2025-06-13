# Internet Gateway

resource "aws_internet_gateway" "hub_igw" {
  vpc_id = aws_vpc.hub-vpc.id

  tags = {
    Name  = format("%s_hub_igw", var.prefix)
    Owner = var.emailid
  }
}

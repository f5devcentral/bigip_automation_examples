# Select BIG-IP AMI to use

data "aws_ami" "bigip" {
  most_recent = true
  filter {
    name   = "name"
    values = [var.f5_ami_search_name]
  }
  owners = ["aws-marketplace"]
}

data "aws_ami" "linux" {
  most_recent = true
  filter {
    name   = "name"
    values = [var.linux_ami_search_name]
  }
}

output "f5_ami_name" {
  value = data.aws_ami.bigip.name
}

output "f5_ami_id" {
  value = data.aws_ami.bigip.id
}

output "linux_ami_name" {
  value = data.aws_ami.linux.name
}

output "linux_ami_id" {
  value = data.aws_ami.linux.id
}

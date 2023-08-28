provider "aws" {
  version = "3.57.0"
 }


data "aws_instance" "node_vm" {
  filter {
    name   = "tag:Name"
    values = ["automation-eks-cluster-0-eks_asg"]
  }
}

data "aws_instance" "bigip" {
  filter {
    name   = "tag:Name"
    values = ["graphql-automation-BIGIP"]
  }
}

# code to update SG ingress correctly
data "aws_security_group" "selected" {
  filter {
    name   = "tag:Name"
    values = ["automation-eks-cluster-eks_worker_sg"]
  }
}

resource "aws_security_group_rule" "allow_app" {
  type        = "ingress"
  from_port   = 30011
  to_port     = 30011
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = data.aws_security_group.selected.id
}

output node_public_ip {
  value = "${data.aws_instance.node_vm.public_ip}"
}

output bigip_private {
  value="${data.aws_instance.bigip.private_ip}"
}

output bigip_public_ip {
  value="${data.aws_instance.bigip.public_ip}"
}

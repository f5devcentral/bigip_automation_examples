
# Generate random password
resource "random_string" "password" {
  length      = 16
  min_upper   = 1
  min_lower   = 1
  min_numeric = 1
  special     = false
}

output "random_password" {
  value = random_string.password.result
}

# Generate AWS Key Pair
resource "tls_private_key" "generated_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "generated_key" {
  key_name   = var.aws_keypair_name
  public_key = tls_private_key.generated_key.public_key_openssh

  tags = {
    Name  = format("%s_aws_keypair", var.prefix)
    Owner = var.emailid
  }
}

resource "local_file" "private_key" {
  content         = tls_private_key.generated_key.private_key_pem
  filename        = "f5lab.key"
  file_permission = "0600"
}

resource "local_file" "public_key" {
  content         = tls_private_key.generated_key.public_key_openssh
  filename        = "f5lab.pub"
  file_permission = "0600"
}

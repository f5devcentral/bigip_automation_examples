# Create lab certificates
resource "null_resource" "ecdsa_certs" {
  provisioner "local-exec" {
    command = "bash ../scripts/create-ecdsa-certs.sh"
  }
}

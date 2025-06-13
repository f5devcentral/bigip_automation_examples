resource "aws_instance" "big_ip" {
  ami                         = var.bigip_ami
  instance_type               = var.bigip_instance_type
  key_name                    = var.aws_key_name

  network_interface {
    network_interface_id = aws_network_interface.mgmt.id
    device_index         = 0
  }

  network_interface {
    network_interface_id = aws_network_interface.external.id
    device_index         = 1
  }

  network_interface {
    network_interface_id = aws_network_interface.internal.id
    device_index         = 2
  }

  user_data                   = file("${path.module}/userdata.sh")
  user_data_replace_on_change = true
  
  tags = merge(var.tags, { "Name" = "bigip", "CostCenter" = "f5lab" })
}

resource "null_resource" "wait_for_bigip_http" {
  depends_on = [aws_instance.big_ip, aws_eip.eip_mgmt]

  provisioner "local-exec" {
    environment = {
      BIGIP_USER     = var.bigip_admin_user
      BIGIP_PASSWORD = var.bigip_admin_password
      AWS_EIP        = aws_eip.eip_mgmt.public_ip
    }

    command = <<-EOT
      retries=0
      max_retries=30
      until [ "$(curl -sk -u "$BIGIP_USER:$BIGIP_PASSWORD" https://$AWS_EIP/mgmt/shared/echo -o /dev/null -w "%%{http_code}")" -eq 200 ]; do
        echo "Waiting for BIG-IP to be ready (attempt: $((retries+1)))..."
        sleep 10
        retries=$((retries+1))
        if [ "$retries" -ge "$max_retries" ]; then
          echo "ERROR: BIG-IP did not become ready after $max_retries attempts."
          exit 1
        fi
      done
      echo "BIG-IP is ready."
    EOT
  }
}

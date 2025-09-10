# Determine the public IP address of the jump host and use it in the security
# group ACLs to restrict access to the lab resources.

data "http" "myip" {
  url = "https://ifconfig.me/ip"
}

output "jumphost_ip" {
  value = data.http.myip.response_body
}

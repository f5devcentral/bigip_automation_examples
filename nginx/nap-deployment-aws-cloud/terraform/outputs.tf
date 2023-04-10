output nap_ip1 {
  value = aws_instance.nap[0].public_ip
}

output nap_ip2 {
  value = aws_instance.nap[1].public_ip
}

output alb_dns {
  value = aws_lb.alb.dns_name
}

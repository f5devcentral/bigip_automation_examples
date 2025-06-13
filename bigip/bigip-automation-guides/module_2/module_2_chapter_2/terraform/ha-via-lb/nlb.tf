# LB-based failover between BIG-IP instances (active-active)

# Create AWS Network Load Balancer
resource "aws_lb" "nlb" {
  name               = format("%s-nlb", var.prefix)
  internal           = false
  load_balancer_type = "network"
  subnets            = [aws_subnet.hub_bigip1_external.id, aws_subnet.hub_bigip2_external.id]
  tags = {
    Name  = format("%s_nlb", var.prefix)
    Owner = var.emailid
  }
}

resource "aws_lb_target_group" "nlb_target" {
  name        = "tf-example-lb-tg"
  port        = 443
  protocol    = "TCP"
  target_type = "ip"
  vpc_id      = aws_vpc.hub-vpc.id
  health_check {
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 2
    interval            = 5
    protocol            = "TCP"
    port                = 443
  }
}

resource "aws_lb_listener" "front_end" {
  load_balancer_arn = aws_lb.nlb.arn
  port              = "443"
  protocol          = "TCP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.nlb_target.arn
  }
}

resource "aws_lb_target_group_attachment" "ips_of_virtual_servers" {
  target_group_arn = aws_lb_target_group.nlb_target.arn
  target_id        = var.bigip_netcfg["bigip1"]["app_vips"][0]
  port             = 443
}
resource "aws_lb_target_group_attachment" "ips_of_virtual_servers2" {
  target_group_arn = aws_lb_target_group.nlb_target.arn
  target_id        = var.bigip_netcfg["bigip2"]["app_vips"][0]
  port             = 443
}

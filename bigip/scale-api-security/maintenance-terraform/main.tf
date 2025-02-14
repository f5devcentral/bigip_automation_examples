# Define the LTM policy
resource "bigip_ltm_policy" "maintenance_policy" {
  name      = var.policy_name
  strategy  = "first-match"
  controls  = ["forwarding"]
  requires  = ["http"]

  rule {
    name = "maintenance_rule"

    condition {
      http_host = true 
      values    = [var.http_host_value]
    }

    action {
      forward     = true
      connection  = false
      pool        = var.policy_pool
    }
  }
}

resource "bigip_ltm_virtual_server" "http" {
  name        = var.virtual_server_name
  destination = var.virtual_server_destination
  profiles    = ["/Common/http", "/Common/tcp", "/Common/websecurity"]
  pool        = var.virtual_server_pool 
  depends_on  = [bigip_ltm_policy.maintenance_policy]

  policies    = [var.policy_name]
}

resource "volterra_origin_pool" "op-ip-internal" {
  name                   = "automation-ratelimit-originpool"
  //Name of the namespace where the origin pool must be deployed
  namespace              = "automation-apisec"
   origin_servers {
    public_ip {
      ip= var.backendip
    }
    labels= {}
  }
  no_tls = true
  port = var.backendport
  endpoint_selection     = "LOCALPREFERED"
  loadbalancer_algorithm = "LB_OVERRIDE"
}


resource "volterra_http_loadbalancer" "lb-http-tf" {
  depends_on = [volterra_origin_pool.op-ip-internal]
  //Mandatory "Metadata"
  name      = "automation-ratelimit-httplb"
  //Name of the namespace where the origin pool must be deployed
  namespace = "automation-apisec"
  //End of mandatory "Metadata" 
  //Mandatory "Basic configuration" with Auto-Cert 
  domains = [var.domain_name]
  http {
    dns_volterra_managed = true
  }
  default_route_pools {
      pool {
        name = "automation-ratelimit-originpool"
        namespace = "automation-apisec"
      }
      weight = 1
    }
  //Mandatory "VIP configuration"
  advertise_on_public_default_vip = true
  //End of mandatory "VIP configuration"
  //Mandatory "Security configuration"
  no_service_policies = true
  no_challenge = true
  //WAAP Policy reference, created earlier in this plan - refer to the same name
  rate_limit {
      rate_limiter {
        total_number = 1
        unit = "MINUTE"
        burst_multiplier = 1
      }
      no_ip_allowed_list = true
      no_policies = true
    }
  disable_waf = true
  multi_lb_app = true
  user_id_client_ip = true
  //End of mandatory "Security configuration"
  //Mandatory "Load Balancing Control"
  source_ip_stickiness = true
  //End of mandatory "Load Balancing Control" 
}

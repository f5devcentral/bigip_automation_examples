//Definition of the Origin, 1-origin.tf
resource "volterra_origin_pool" "op-ip-internal" {
  name                   = "automation-xss-originpool"
  //Name of the namespace where the origin pool must be deployed
  namespace              = var.namespace
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


//Definition of the WAAP Policy
resource "volterra_app_firewall" "waap-tf" {
  name      = "automation-xss-waf"
  namespace = var.namespace

  // One of the arguments from this list "allow_all_response_codes allowed_response_codes" must be set
  allow_all_response_codes = true
  // One of the arguments from this list "default_anonymization custom_anonymization disable_anonymization" must be set
  default_anonymization = true
  // One of the arguments from this list "use_default_blocking_page blocking_page" must be set
  use_default_blocking_page = true
  // One of the arguments from this list "default_bot_setting bot_protection_setting" must be set
  default_bot_setting = true
  // One of the arguments from this list "default_detection_settings detection_settings" must be set
  default_detection_settings = true
  // One of the arguments from this list "use_loadbalancer_setting blocking monitoring" must be set
  use_loadbalancer_setting = true
  // Blocking mode - optional - if not set, policy is in MONITORING
  blocking = true
}

// LB definition
resource "volterra_http_loadbalancer" "lb-http-tf" {
  depends_on = [volterra_origin_pool.op-ip-internal]
  //Mandatory "Metadata"
  name      = "automation-xss-httplb"
  //Name of the namespace where the origin pool must be deployed
  namespace = var.namespace
  //End of mandatory "Metadata" 
  //Mandatory "Basic configuration" with Auto-Cert 
  domains = [var.domain_name]
  http {
    dns_volterra_managed = true
  }
  default_route_pools {
      pool {
        name = "automation-xss-originpool"
        namespace = var.namespace
      }
      weight = 1
    }
  //Mandatory "VIP configuration"
  advertise_on_public_default_vip = true
  //End of mandatory "VIP configuration"
  //Mandatory "Security configuration"
  no_service_policies = true
  no_challenge = true
  disable_rate_limit = true
  //WAAP Policy reference, created earlier in this plan - refer to the same name
  app_firewall {
    name = "automation-xss-waf"
    namespace = var.namespace
  }
  multi_lb_app = true
  user_id_client_ip = true
  //End of mandatory "Security configuration"
  //Mandatory "Load Balancing Control"
  source_ip_stickiness = true
}

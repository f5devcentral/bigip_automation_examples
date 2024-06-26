terraform {
  required_providers {
    bigipnext = {
      source  = "F5Networks/bigipnext"
      version = "1.2.0"
    }
  }
}

provider "bigipnext" {
  username = "admin"
  password = "Welcome123!"
  host     = "https://10.1.1.5"
}

resource "bigipnext_cm_waf_policy_import" "waf_greenfield_demo_policy" {
  name        = "waf_greenfield_demo_policy"
  description = "Demo Policy for greenfield use-case"
  file_path   = "./policy.json"
  file_md5    = md5(file("./policy.json"))
}

resource "bigipnext_cm_as3_deploy" "waf_greenfield_demo_app" {
  depends_on = [bigipnext_cm_waf_policy_import.waf_greenfield_demo_policy]
  target_address = "10.1.1.11"
  as3_json       = <<EOT
{
    "class": "ADC",
    "schemaVersion": "3.45.0",
    "id": "waf_greenfield_demo_app",
    "label": "Demo application",
    "remark": "Simple HTTP application with round robin pool",
    "waf_greenfield_demo_tenant": {
        "class": "Tenant",
        "waf_greenfield_demo_app": {
            "class": "Application",
            "template": "http",
            "serviceMain": {
                "class": "Service_HTTP",
                "virtualAddresses": [
                    "10.0.12.10"
                ],
                "pool": "waf_greenfield_demo_pool",
                "policyWAF": {
                    "cm": "waf_greenfield_demo_policy"
                }
            },
            "waf_greenfield_demo_pool": {
                "class": "Pool",
                "monitors": [
                    "http"
                ],
                "members": [
                    {
                        "servicePort": 80,
                        "serverAddresses": [
                            "192.0.2.100",
                            "192.0.2.110"
                        ]
                    }
                ]
            }
        }
    }
}
EOT
}

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

resource "bigipnext_cm_waf_policy_import" "sample" {
  name        = "new_waf_policy"
  description = "new_waf_policy desc"
  file_path   = "./policy.json"
  file_md5    = md5(file("./policy.json"))
}

resource "bigipnext_cm_as3_deploy" "test_01" {
  depends_on = [bigipnext_cm_waf_policy_import.sample]
  target_address = "10.1.1.11"
  as3_json       = <<EOT
{
    "class": "ADC",
    "schemaVersion": "3.45.0",
    "id": "example-declaration-03",
    "label": "Sample 1",
    "remark": "Simple HTTP application with round robin pool",
    "next-cm-tenant02": {
        "class": "Tenant",
        "next-cm-app02": {
            "class": "Application",
            "template": "http",
            "serviceMain": {
                "class": "Service_HTTP",
                "virtualAddresses": [
                    "10.0.12.10"
                ],
                "pool": "next-cm-pool02",
                "policyWAF": {
                    "cm": "new_waf_policy"
                }
            },
            "next-cm-pool02": {
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

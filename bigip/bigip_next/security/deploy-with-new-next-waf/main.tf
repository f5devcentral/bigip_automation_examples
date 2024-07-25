resource "bigipnext_cm_waf_policy_import" "waf_greenfield_demo_policy" {
  name        = "waf_greenfield_demo_policy"
  description = "Demo Policy for greenfield use-case"
  file_path   = "./policy.json"
  file_md5    = md5(file("./policy.json"))
}

resource "bigipnext_cm_as3_deploy" "waf_greenfield_demo_app" {
  depends_on = [bigipnext_cm_waf_policy_import.waf_greenfield_demo_policy]
  target_address = var.target
  as3_json       = file("./app-as3.json") 
}

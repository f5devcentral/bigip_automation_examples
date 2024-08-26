resource "bigipnext_cm_waf_policy" "waf_greenfield_demo" {
  name                 	= "waf_greenfield_demo_policy"
  description		= "Demo Policy for greenfield use-case"
  enforcement_mode     	= "blocking"
  application_language 	= "utf-8"
  template_name        	= "Rating-Based-Template"
}

resource "bigipnext_cm_as3_deploy" "waf_greenfield_demo_app" {
  depends_on = [bigipnext_cm_waf_policy.waf_greenfield_demo]
  target_address = var.target
  as3_json       = file("./app-as3.json") 
}

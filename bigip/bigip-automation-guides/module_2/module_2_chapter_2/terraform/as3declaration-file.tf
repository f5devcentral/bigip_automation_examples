# Render as3certs Template File
data "template_file" "as3certs" {
  depends_on = [null_resource.ecdsa_certs]
  template   = file("./templates/as3certdeclarationtemplate.json")
  vars = {
    EXAMPLE01A_ECDSA_CERT = fileexists("example01a.f5lab.dev.cert") ? file("example01a.f5lab.dev.cert") : "null"
    EXAMPLE01A_ECDSA_KEY  = fileexists("example01a.f5lab.dev.key") ? file("example01a.f5lab.dev.key") : "null"
    EXAMPLE01B_ECDSA_CERT = fileexists("example01b.f5lab.dev.cert") ? file("example01b.f5lab.dev.cert") : "null"
    EXAMPLE01B_ECDSA_KEY  = fileexists("example01b.f5lab.dev.key") ? file("example01b.f5lab.dev.key") : "null"
  }
}


resource "local_file" "as3certs_rendered" {
  depends_on = [null_resource.ecdsa_certs]
  content    = data.template_file.as3certs.rendered
  filename   = "../ATC/AS3/Step3_as3_ecdsaCerts_Autodiscovery.json"
}

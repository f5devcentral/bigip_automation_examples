module "infrastructure" {
  source = "./infrastructure"
  providers = {
    aws = aws
  }
}

module "configuration" {
  source = "./configuration"

  providers = {
    bigip = bigip
  }

  depends_on = [ module.infrastructure ]
}

output "management_public_ip" {
  value = module.infrastructure.management_public_ip
}

output "external_public_ip" {
  value = module.infrastructure.external_public_ip
}

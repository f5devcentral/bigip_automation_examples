variable "api_cert" {
	type = string
	default = "certificate.cert"
}
        
variable "api_key" {
  	type = string
  	default = "private_key.key"
}

variable "backendip" {
  	type = string
}

variable "namespace" {
  	type = string
}

variable "backendport" {
  	type = string
  	default = "80"
}

variable "domain_name" {
  	type = string
}

variable "api_url" {
	type = string
}

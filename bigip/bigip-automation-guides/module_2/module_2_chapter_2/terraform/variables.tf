### Object name prefix
variable "prefix" {
  description = "Prefix for object creation"
  type        = string
}

### ID
variable "emailid" {
  description = "emailid"
}

### AWS Region
variable "aws_region" {
  description = "aws region"
  default     = "us-west-1"
  #  Tested in:
  #    us-west-2 (default - Oregon)
  #    us-east-1 (Virginia)
  #  If running this lab in a region other than the default, you must also edit 
  #  the region in ~/.aws/config.
}

### VPCs
variable "vpc_cidrs" {
  description = "VPC subnets (CIDR)"
  type        = map(map(string))
  default = {
    hub = {
      vpc             = "10.0.0.0/16"
      bigip1_mgmt     = "10.0.10.0/24"
      bigip1_internal = "10.0.11.0/24"
      bigip1_external = "10.0.12.0/24"
      bigip2_mgmt     = "10.0.20.0/24"
      bigip2_internal = "10.0.21.0/24"
      bigip2_external = "10.0.22.0/24"
    }
    app = {
      vpc     = "10.1.0.0/16"
      appsvr1 = "10.1.10.0/24"
      appsvr2 = "10.1.20.0/24"
    }
  }
}

### AWS Keypair
variable "aws_keypair_name" {
  description = "Name for AWS keypair"
  default     = "f5lab_aws_keypair"
}

### Cloudwatch Log Group
variable "aws_log_group" {
  description = "AWS log group name"
  default     = "studentf5labdev"
}

### App servers
variable "linux_ami_search_name" {
  type    = string
  default = "amzn2-ami-minimal-hvm*2023*x86*"
}

variable "linux_instance_type" {
  type    = string
  default = "t2.micro"
}

variable "app_admin" {
  type    = string
  default = "admin"
}

variable "appsvr_netcfg" {
  default = {
    appsvr1 = {
      eth0 = "10.1.200.80"
    }
    appsvr2 = {
      eth0 = "10.1.201.80"
    }
  }
}


### BIG-IPs
variable "f5_ami_search_name" {
  type    = string
  default = "F5 BIGIP-17.1.*PAYG-Adv WAF Plus 25Mbps*"
}

variable "bigip_instance_type" {
  type    = string
  default = "m5.xlarge"
}

variable "bigip_admin" {
  type    = string
  default = "admin"
}

variable "bigip_netcfg" {
  type = any
  default = {
    bigip1 = {
      az                 = "1"
      hostname           = "bigip1.f5lab.dev"
      tag                = "bigip1_3nic"
      mgmt               = "10.0.10.11/24"
      internal           = "10.0.11.11/24"
      external           = "10.0.12.11/24"
      external_secondary = "10.0.12.12/24"
      app_vips           = ["10.0.12.101", "10.0.12.102", "10.0.12.103", "10.0.12.104"]
    }
    bigip2 = {
      az                 = "2"
      hostname           = "bigip2.f5lab.dev"
      tag                = "bigip2_3nic"
      mgmt               = "10.0.20.11/24"
      internal           = "10.0.21.11/24"
      external           = "10.0.22.11/24"
      external_secondary = "10.0.22.12/24"
      app_vips           = ["10.0.22.101", "10.0.22.102", "10.0.22.103", "10.0.22.104"]
    }
  }
}


### AS3 declaration file paths (for module 5)
variable "as3_configs" {
  description = "AS3 declaration files to load"
  type = list(object({
    as3file = string
  }))
}


### F5 Automation Toolchain package download URLs

# Please check and update the latest runtime init URL from https://github.com/F5Networks/f5-bigip-runtime-init/releases/latest
# always point to a specific version in order to avoid inadvertent configuration inconsistency
variable "INIT_URL" {
  description = "URL to download the BIG-IP runtime init"
  type        = string
  default     = "https://github.com/F5Networks/f5-bigip-runtime-init/releases/download/1.6.1/f5-bigip-runtime-init-1.6.1-1.gz.run"
}

# Please check and update the latest DO URL from https://github.com/F5Networks/f5-declarative-onboarding/releases
# always point to a specific version in order to avoid inadvertent configuration inconsistency
variable "DO_URL" {
  description = "URL to download the BIG-IP Declarative Onboarding module"
  type        = string
  default     = "https://github.com/F5Networks/f5-declarative-onboarding/releases/download/v1.36.1/f5-declarative-onboarding-1.36.1-1.noarch.rpm"
}
variable "DO_VER" {
  type    = string
  default = "1.36.1"
}

# Please check and update the latest AS3 URL from https://github.com/F5Networks/f5-appsvcs-extension/releases/latest 
# always point to a specific version in order to avoid inadvertent configuration inconsistency
variable "AS3_URL" {
  description = "URL to download the BIG-IP Application Service Extension 3 (AS3) module"
  type        = string
  default     = "https://github.com/F5Networks/f5-appsvcs-extension/releases/download/v3.44.0/f5-appsvcs-3.44.0-3.noarch.rpm"
}
variable "AS3_VER" {
  type    = string
  default = "3.44.0"
}

# Please check and update the latest TS URL from https://github.com/F5Networks/f5-telemetry-streaming/releases/latest 
# always point to a specific version in order to avoid inadvertent configuration inconsistency
variable "TS_URL" {
  description = "URL to download the BIG-IP Telemetry Streaming module"
  type        = string
  default     = "https://github.com/F5Networks/f5-telemetry-streaming/releases/download/v1.32.0/f5-telemetry-1.32.0-2.noarch.rpm"
}
variable "TS_VER" {
  type    = string
  default = "1.32.0"
}

# Please check and update the latest Failover Extension URL from https://github.com/F5Networks/f5-cloud-failover-extension/releases/latest 
# always point to a specific version in order to avoid inadvertent configuration inconsistency
variable "CFE_URL" {
  description = "URL to download the BIG-IP Cloud Failover Extension module"
  type        = string
  default     = "https://github.com/F5Networks/f5-cloud-failover-extension/releases/download/v1.14.0/f5-cloud-failover-1.14.0-0.noarch.rpm"
}
variable "CFE_VER" {
  type    = string
  default = "1.14.0"
}

# Please check and update the latest FAST URL from https://github.com/F5Networks/f5-appsvcs-templates/releases/latest 
# always point to a specific version in order to avoid inadvertent configuration inconsistency
variable "FAST_URL" {
  description = "URL to download the BIG-IP FAST module"
  type        = string
  default     = "https://github.com/F5Networks/f5-appsvcs-templates/releases/download/v1.24.0/f5-appsvcs-templates-1.24.0-1.noarch.rpm"
}
variable "FAST_VER" {
  type    = string
  default = "1.24.0"
}

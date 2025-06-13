terraform {
  required_version = ">= 1.1.7"
  required_providers {
    bigip = {
      source = "F5Networks/bigip"
      version = "1.22"
    }
  }
}
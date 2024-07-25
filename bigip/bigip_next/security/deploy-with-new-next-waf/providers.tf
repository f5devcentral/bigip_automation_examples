terraform {
  required_providers {
    bigipnext = {
      source  = "F5Networks/bigipnext"
      version = ">= 1.2.0"
    }
  }
}

provider "bigipnext" {
  username = var.username
  password = var.password
  host     = var.cm
}

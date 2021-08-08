# All the variables are declared in this file match the parameter names for setting up VPC. 
# All the values come from ../../deploy/<env>/vpc.tf
variable "cidr_block" {
  type = string
}
variable "assign_generated_ipv6_cidr_block" {
  type = bool
  default = false
}

variable "enable_classiclink" {
  type = bool
  default = false
}

variable "enable_classiclink_dns_support" {
  type = bool
  default = false
}
variable "enable_dns_hostnames" {
  type = bool
  default = true
}

variable "enable_dns_support" {
  type = bool
  default = true
}

variable "tags" {
  type = map
  default = {
      "Name" = "io-cloud"
      "Organization" = "SRE"
      "Purpose" = "Lab"
      "Environment" = "Development"
  }
}
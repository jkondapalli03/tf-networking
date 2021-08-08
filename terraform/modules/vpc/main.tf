#Module for setting up vpc. all the variables are declared in variables.tf but come from ../../deploy/<env>/vpc.tf
resource "aws_vpc" "io-cloud" {
  cidr_block       = var.cidr_block
  instance_tenancy = "default"
  assign_generated_ipv6_cidr_block = var.assign_generated_ipv6_cidr_block
  enable_classiclink = var.enable_classiclink
  enable_classiclink_dns_support = var.enable_classiclink_dns_support
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support = var.enable_dns_support

  tags = {
    Name = var.tags["Name"]
    Organization = var.tags["Organization"]
    Purpose = var.tags["Purpose"]
    Environment = var.tags["Environment"]
  }
}
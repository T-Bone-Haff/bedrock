terraform {
  required_version = ">= 1.4, < 2.0"
}

variable "runtime_secret_payload" {
  type        = string
  sensitive   = true
  description = "Runtime-only value; Terraform must not pass it to a resource or output."
}

variable "secret_resource_name" {
  type = string
}

resource "terraform_data" "runtime_reference" {
  input = var.secret_resource_name
}

output "runtime_reference" {
  value = terraform_data.runtime_reference.output
}

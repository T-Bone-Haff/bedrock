terraform {
  required_version = ">= 1.4, < 2.0"
}

variable "secret_payload" {
  type      = string
  sensitive = true
}

resource "terraform_data" "materialized_secret" {
  input = var.secret_payload
}

output "materialized_secret" {
  value     = terraform_data.materialized_secret.output
  sensitive = true
}

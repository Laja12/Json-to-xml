terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.0.0"
    }
  }
}
provider "aws" {
  region = var.aws_region
}
module "s3_bucket" {
  source      = "./modules/s3"
  bucket_name = "json-to-xml-bucket-example"
}

module "iam_role" {
  source         = "./modules/iam_role"
  role_name      = "lambda-transform-role"
  s3_bucket_arn  = "arn:aws:s3:::json-to-xml-bucket-example"
}

module "lambda_function" {
  source           = "./modules/lambda_function"
  function_name    = "json_to_xml_transform"
  lambda_role_arn  = module.iam_role.role_arn
  s3_bucket_name   = module.s3_bucket.bucket_name
}

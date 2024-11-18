terraform {
  backend "s3" {
    bucket         = "ge-my-tf-website-state" #Created a new bucket
    key            = "global/s3/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "project-table" #Created a table

  }
}


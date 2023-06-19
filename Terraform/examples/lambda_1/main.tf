terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws",
      version = "5.2.0"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "archive_file" "lambda_python_file" {
  type = "zip"
  source_file = "src/main.py"
  output_path = "lambda_function_payload.zip"
}

resource "aws_lambda_function" "test_lambda_1" {
  function_name = "function_1"
  filename      = "lambda_function_payload.zip"
  role          = aws_iam_role.iam_for_lambda.arn
  runtime       = "python3.10"
  handler       = "main.helloworld"
  tags = {
    Owner = "Somebody"
  }
}

resource "aws_lambda_function" "test_lambda_2" {
  function_name = "function_2"
  filename      = "lambda_function_file_name.zip"
  role          = aws_iam_role.iam_for_lambda.arn
  runtime       = "python3.10"
  handler       = "lambda_function_file_name.main.hello"
}

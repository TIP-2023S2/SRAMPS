# Lambda Example in Terraform

## Pre-requisites

1. Terraform
2. AWS CLI
3. AWS configured using `AWS configure` command

## Steps
### cd into this example folder
```shell
cd Terraform/examples/lambda_1
```

### Initialize Terraform
```shell
terraform init
```

### See the plan using terraform
```shell
terraform plan
```

### Apply the plan
```shell
terraform apply
```
When prompted, type `yes`

### Verify created resources
Log in on your AWS Console and verify the following:
1. IAM Role `iam_for_lambda` was created
2. 2 lambda functions were created. Test them.

### Destroy the resources
When everything is verified, you can safely destroy the resources.
```shell
terraform destroy
```
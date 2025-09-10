## Terraform State Management for F5 BIG-IP Automation
### module 3 chapter 4

In this chapter, we will set up a remote backend for Terraform state management using AWS S3 and DynamoDB. This ensures that your Terraform state is stored securely, versioned, and locked to prevent concurrent modifications.

## Step 1: Create an S3 Bucket

Run the following command to create an S3 bucket. Replace `your-unique-bucket-name` with a globally unique name.

```bash
aws s3api create-bucket \
  --bucket your-unique-bucket-name \
  --region us-west-1 \
  --create-bucket-configuration LocationConstraint=us-west-1
```

Enable versioning on the bucket to preserve and recover previous state files:

```bash
aws s3api put-bucket-versioning \
  --bucket your-unique-bucket-name \
  --versioning-configuration Status=Enabled
```

## Step 2: Create a DynamoDB Table

This table will be used to manage state locking and prevent concurrent runs.

```bash
aws dynamodb create-table \
  --table-name demo-tf-lockid \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
  --region us-west-1
```

## Step 3: Update Terraform Configuration

Ensure your `versions.tf` file points to the correct bucket and table:

```hcl
backend "s3" {
  bucket         = "your-unique-bucket-name"
  key            = "terraform.tfstate"
  region         = "us-west-1"
  encrypt        = true
  dynamodb_table = "demo-tf-lockid"
}
```

## Step 4: Initialize Terraform

Run `terraform init` to configure the backend. Terraform will prompt you to migrate the state to the new backend if it was previously local.

```bash
terraform init
```

You can verify that the backend is set up correctly by checking the S3 bucket and DynamoDB table in the AWS Management Console.
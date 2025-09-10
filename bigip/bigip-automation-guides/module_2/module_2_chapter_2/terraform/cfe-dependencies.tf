# Create IAM Policy for CFE

# S3 Bucket for F5 Cloud Failover Extension
resource "aws_s3_bucket" "f5_cloud_failover_extension" {
  bucket        = "f5-cloud-failover-ext-${uuid()}"
  force_destroy = true

  lifecycle {
    ignore_changes = [
      bucket
    ]
  }

  tags = {
    Name                    = format("%s_cfe_s3_bucket", var.prefix)
    Owner                   = var.emailid
    f5_cloud_failover_label = "mydeployment"
  }
}


# IAM Role for F5 Cloud Failover Extension
resource "aws_iam_role" "f5_cloud_failover_role" {
  name = "f5_cloud_failover_role"

  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
        }
    ]
}
EOF
}

resource "aws_iam_policy" "sts_assume_role" {
  name = "sts_assume_role"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_policy" "ec2_all" {
  name = "ec2_all"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_policy" "s3_all" {
  name = "s3_all"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "attach1" {
  role       = aws_iam_role.f5_cloud_failover_role.name
  policy_arn = aws_iam_policy.sts_assume_role.arn
}
resource "aws_iam_role_policy_attachment" "attach2" {
  role       = aws_iam_role.f5_cloud_failover_role.name
  policy_arn = aws_iam_policy.ec2_all.arn
}
resource "aws_iam_role_policy_attachment" "attach3" {
  role       = aws_iam_role.f5_cloud_failover_role.name
  policy_arn = aws_iam_policy.s3_all.arn
}

resource "aws_iam_instance_profile" "f5_cloud_failover_profile" {
  name = "f5_cloud_failover_profile"
  role = aws_iam_role.f5_cloud_failover_role.name
}

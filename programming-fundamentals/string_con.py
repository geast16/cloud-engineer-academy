# Define the AW Account ID
account_id = "123456789012"

# Define the project name
project_name = "cloud_project1"

# Concatenate strings to form the S3 Bucket name
bucket_name = account_id + "-" + project_name + "-bucket"

# Print the resulting bucket name
print(f"S3 Bucket Name: {bucket_name}")


# Exercise EC2 string concatenation

# Environment name prod, dev, staging
environment = "dev"

# Application name
application = "appserver"

# Instance number
instance_number = "04"

# Concatenate
instance_name = environment + "-" + application + "-instance-" + instance_number

# Print
print("EC2 instance name: " + instance_name)

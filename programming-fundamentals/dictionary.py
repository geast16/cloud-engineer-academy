# Dictionaries
# -Store and retieve informasion
# - Key and Values

# EC2
ec2_instance = {
    "InstanceId": "i-123456abcde",
    "InstanceType": "t2.micro",
    "State": "running",
    #    "PublicIpAddress": "203.0.111.4",
}

instance_id = ec2_instance["InstanceId"]
print(f"this is a {instance_id} instance.")

public_ip = ec2_instance.get("PublicIpAddress", "No Public IP address is here")
print(f"the instance's public ip is: {public_ip}")

# Adding a new key-value pair
ec2_instance["AvailabilityZone"] = "us-east-1"  # Creates a new key-value pair
ec2_instance["State"] = "stopped"  # Updates/changes the value uses for the State value

print(ec2_instance)


# Removing values via pop() or Del

# Using pop()
rm_instance_type = ec2_instance.pop("InstanceType")
print(f"removed instance type: {rm_instance_type}")
print(ec2_instance)

# using Del
del ec2_instance["AvailabilityZone"]
print(ec2_instance)

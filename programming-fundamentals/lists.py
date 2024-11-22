# List of EC2 instance
instance_ids = ["i-1234", "i-9012", "i-5678"]

# List of IP addresses for a security group
ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]

# List of availability zones in a region
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

# Print the lists
print(f"EC2 instances to terminate: {instance_ids}")
print(f"First IP addresses: {ip_addresses}")
print(f"Number of AZs: {availability_zones}")

# Add new EC2 instance ID via Append
instance_ids.append("i-3456")
print("After adding a new instance ID")
print("EC2 Instances:", instance_ids)

# Remove EC2 instance ID
instance_ids.remove("i-1234")
print("After removing an instance")
print("EC2 instances:", instance_ids)

# Check if an item is in a list via the in methof
if "10.0.0.4" in ip_addresses:
    print("Yes 10.0.0.4 is in and allowed")
else:
    print("No 10.0.0.4 is not in the allowed list")
print("IP addresses:", ip_addresses)

# Slicing a List
# First two AZs
first_two_azs = availability_zones[:2]
print("First two AZs:", first_two_azs)


# Sorting
instance_ids.sort()
print("Sorted EC2 Instances", instance_ids)

# Length of IP addresses, of a list
number_of_ips = len(ip_addresses)
print(f"Number of IP addresses: {number_of_ips}")


# Accessing list of Items by Index
first_az = availability_zones[0]
last_az = availability_zones[2]
print(f"First Az:", first_az)
print(f"Last Az:", last_az)

# # Control Structures / Control Flow
# instance_running = "stopped"
# # If Statements
# if instance_running == "running":
#     print("This EC2 is running")
#     # code to execute if confition is True

# elif instance_running == "stopped":
#     print("the EC2 is stopped ...")
#     # code to execute if another_conditon is True

# else:
#     print("the EC2 instance is in an unexpected state.")
#     # code to execute if all confition are False


public_access_block = False

# Write the if statement
# if
if public_access_block == True:
    print("s3 bucket is secured.")
else:
    print("S3 bucket is not secure.")

# Check if an IP Address is public or private

import ipaddress

# create a variable with an array of ip addresses
address = ["192.168.0.1", "54.240.197.239"]

# Evaluate the type of ip address
for i in address:
    if ipaddress.IPv4Address(i).is_private is True:
        print(f"The ip address, {i} is private")
    elif ipaddress.IPv4Address(i).is_global is True:
        print(f"The ip address, {i} is global")


# returns
# The ip address, 192.168.0.1 is private
# The ip address, 54.240.197.239 is global

# Documentation https://docs.python.org/3/library/ipaddress.html



#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# first items
print("The first item in the list (IP): " + my_list[0] )

# second item
print("The second item in the list (port): " + str(my_list[1]) )

# third item in the list
print("The last item in the list (state): " + my_list[2] )

# the ip addresses only
print("The following are the IP addresses in iplist:")
for item in iplist:
    if "." in str(item): 
        print(item)

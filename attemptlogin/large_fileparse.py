#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
get_requests = 0
post_requests = 0
# open the file for reading

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r") as keystone_file:
    for line in keystone_file:
        if "Authorization failed" in line:
            loginfail += 1
        if "GET" in line:
            get_requests += 1
        if "POST" in line:
            post_requests += 1

    print("The number of failed login attempts is", loginfail)
    print("The number of GET requests is", get_requests)
    print("The number of POST requests is", post_requests)

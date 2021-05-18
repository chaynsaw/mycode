#!/usr/bin/python3
from datetime import datetime
from pprint import pprint

import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    try:
        startdate = input("Please enter YYYY-MM-DD for startdate (Optional): ")
        if startdate == "":
            startdate = "2019-11-11"
        else:
            valid_startdate = datetime.fromisoformat(startdate)
    except:
        print(f"Start Date: {startdate} is invalid.")

    try:
        enddate = input("Please enter YYYY-MM-DD for enddate (Optional): ")
        if enddate == "":
            pass
        else:
            valid_enddate = datetime.fromisoformat(enddate)
    except:
        print(f"End Date: {enddate} is invalid.")



    # make a request with the request library
    payload = {
        "api_key": nasacreds,
        "start_date": startdate,
        "end_date": enddate
    }
    print(payload)
    neowrequest = requests.get(NEOURL, params=payload)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    potentially_hazardous_asteroids = 0
    largest_asteroid_diameter = 0.0
    largest_asteroid_name = ""
    closest_asteroid_distance = 0.0
    closest_asteroid_name = ""

    try:
        for date in neodata['near_earth_objects']:
            for neo in neodata['near_earth_objects'][date]:
                if neo['is_potentially_hazardous_asteroid']:
                    potentially_hazardous_asteroids += 1
                if neo['estimated_diameter']['kilometers']['estimated_diameter_max'] > largest_asteroid_diameter:
                    largest_asteroid_name = neo['name']
                    largest_asteroid_diameter = neo['estimated_diameter']['kilometers']['estimated_diameter_max']
                if closest_asteroid_distance == 0 or closest_asteroid_distance > neo['close_approach_data'][0]['miss_distance']['astronomical']:
                    closest_asteroid_distance = neo['close_approach_data'][0]['miss_distance']['astronomical']
                    closest_asteroid_name = neo['name']
        print(f"Number of potentially hazardous asteroids: {potentially_hazardous_asteroids}")
        print(f"The largest asteroid was {largest_asteroid_name}")
        print(f"The closest asteroid was {closest_asteroid_name}")
    except:
        print("Something went wrong. Please check your dates.")

    pprint(neodata)
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]



def return_agriculture_from_farm(farms=farms, animals_only=False):
    allowed_farms = [item['name'].lower() for item in farms]

    if animals_only is False:
        restricted_list = []
    else:
        restricted_list = ['carrots', 'celery']

    if len(farms) == 1:
        print(f"Only one farm specified, returning all farms from {farms[0]['name']}")
        for element in farms[0]['agriculture']:
            if element not in restricted_list:
                print(element, end=" ")
        return

    function2input = input(f"Choose from {allowed_farms} animals_only is set to {animals_only}. ").lower()
    while True:
        if function2input in allowed_farms:
            for farm in farms:
                if farm['name'].lower() == function2input:
                    for element in farm['agriculture']:
                        if element not in restricted_list:
                            print(element, end=" ")
                    return
        else:
            function2input = input(f"Please try again. Choose from {allowed_farms}. ").lower()


if __name__ == "__main__":
    return_agriculture_from_farm(farms=[item for item in farms if item['name'] == "NE Farm"])
    print('\n')
    return_agriculture_from_farm(animals_only=False)
    print('\n')
    return_agriculture_from_farm(animals_only=True)
    print('\n')


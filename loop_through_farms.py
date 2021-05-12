#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def return_agriculture_from_farm(animals_only=False):
    if animals_only is False:
        restricted_list = []
    else:
        restricted_list = ['carrots', 'celery']

    function2input = input(f"Choose NE Farm, W Farm, or SE Farm. animals_only is set to {animals_only}. ").lower()
    while True:
        if function2input in ["ne farm", "w farm", "se farm"]:
            for farm in farms:
                if farm['name'].lower() == function2input:
                    for element in farm['agriculture']:
                        if element not in restricted_list:
                            print(element, end=" ")
                    return
        else:
            function2input = input("Please try again. Choose NE Farm, W Farm, or SE Farm: ").lower()


if __name__ == "__main__":
    for farm in farms:
        for element in farm['agriculture']:
            print(element, end=" ")
    print('\n')
    return_agriculture_from_farm(animals_only=False)
    print('\n')
    return_agriculture_from_farm(animals_only=True)
    print('\n')


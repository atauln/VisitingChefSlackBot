from datetime import date
import requests

def get_all_dining(tod = date.today()):
    url = f'https://tigercenter.rit.edu/tigerCenterApp/tc/dining-all?date={str(tod)}'
    response = requests.get(
        url
    ).json()
    return response

def find_dining_loc(loc_search: str, tod = date.today()) -> list[dict]:
    locations = []
    foodstuffs = get_all_dining(tod)
    for item in foodstuffs['locations']:
        for menu in item['menus']:
            if loc_search in menu['name']:
                locations.append({
                    'name': menu['name'],
                    'location': item['name']
                })
    return locations

def find_visiting_chefs(tod = date.today()) -> list[dict]:
    locations = []
    foodstuffs = get_all_dining(tod)
    for item in foodstuffs['locations']:
        for menu in item['menus']:
            if menu['category'] == "Visiting Chef":
                locations.append({
                    'name': menu['name'],
                    'location': item['name'],
                    'description': menu['description']
                        if menu['description'] != None else ''
                })
    return locations

def find_visiting_chefs_fmt(tod = date.today()) -> str:
    locations = find_visiting_chefs(tod)
    base_str = "Here are the visiting chefs for today:\n"
    for chef in locations:
        base_str += f"*{chef['name']}* is at _{chef['location']}_.\n"
        base_str += f">_{chef['description']}_\n"
    return base_str if len(locations) != 0 else "*There are no visiting chefs today!*"

def main():
    print(find_visiting_chefs())

if __name__ == "__main__":
    main()

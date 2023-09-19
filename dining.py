from datetime import date
import requests

def get_all_dining(tod = date.today()):
    url = f'https://tigercenter.rit.edu/tigerCenterApp/tc/dining-all?date={str(tod)}'
    response = requests.get(
        url
    ).json()
    return response

def find_good_food(tod = date.today()) -> list[str]:
    locations = []
    foodstuffs = get_all_dining(tod)
    for item in foodstuffs['locations']:
        for menu in item['menus']:
            if 'Pakistan' in menu['name']:
                locations.append({
                    'name': menu['name'],
                    'location': item['name']
                })
    return locations

def main():
    print(find_good_food())

if __name__ == "__main__":
    main()
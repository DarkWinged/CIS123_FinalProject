import os
from Mail_Manager import MailManager
from API_Manager import APIManager
from Restaurant import RestaurantList


def write_to_file(file, write_text):
    with open(file, "w+") as local_File:
        local_File.write(write_text)


if __name__ == '__main__':
    end_point = 'https://api.yelp.com/v3/businesses'
    api_key = os.environ.get('YELP_API')
    query = {
        'term': ['restaurant'],
        'limit': 50,
        'radius': 10000,
        'location': 'Grand+Rapids'
    }

    yelp_api = APIManager(end_point, api_key)
    response = yelp_api.search(query)
    result = RestaurantList.from_json(response.json())
    filtered_results = []
    for restaurant in result.restaurants:
        if 'pickup' in restaurant.transactions:
            filtered_results.append(restaurant)
    for restaurant in result.restaurants:
        if 'delivery' in restaurant.transactions:
            if restaurant not in filtered_results:
                filtered_results.append(restaurant)

    write_to_file("restaurants_unfiltered.txt", result.print())

    filtered = ''
    for business in filtered_results:
        filtered += business.print()

    write_to_file("restaurants_filtered.txt", filtered)

    Jerry = MailManager()
    recipient = input('Enter the recipient\'s email address: ')
    title = "Search results"
    text = 'Total restaurants collected: ' + str(len(result.restaurants))
    text += '\nRestaurants with pickup and/or delivery: ' + str(len(filtered_results))
    Jerry.send_letter(recipient, title, text, "restaurants_filtered.txt", "restaurants_unfiltered.txt")

    print(text + '\n')
    print(result.print())

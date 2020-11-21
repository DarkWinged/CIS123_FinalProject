class Restaurant:
    def __init__(self, yelp_id=None, alias=None, name=None, is_closed=None, url=None,
                 categories=None, rating=None, transactions=None,
                 location=None, display_phone=None):
        if transactions is None:
            transactions = []
        if categories is None:
            categories = []
        self.yelp_id = yelp_id
        self.alias = alias
        self.name = name
        self.is_closed = is_closed
        self.url = url
        self.categories = categories
        self.rating = rating
        self.transactions = transactions
        self.location = location
        self.display_phone = display_phone

    @staticmethod
    def from_json(json_dict) -> 'Restaurant':
        yelp_id = json_dict['id']
        alias = json_dict['alias']
        name = json_dict['name']
        is_closed = json_dict['is_closed']
        url = json_dict['url']
        categories = []
        for category in json_dict['categories']:
            categories.append(category['title'])
        rating = json_dict['rating']
        transactions = []
        for transaction in json_dict['transactions']:
            transactions.append(transaction)
        location = json_dict['location']['display_address']
        display_phone = json_dict['display_phone']
        return Restaurant(yelp_id, alias, name, is_closed, url, categories,
                          rating, transactions, location, display_phone)

    def print(self):
        result = ''
        result += 'Business: ' + self.name + '\n'
        result += '\tID: ' + self.yelp_id + '\n'
        result += '\tAlias: ' + self.alias + '\n'
        result += '\tIs_closed: ' + str(self.is_closed) + '\n'
        result += '\tURL: ' + self.url + '\n'
        result += '\tCategories:\n'
        for category in self.categories:
            result += '\t\t' + category + '\n'
        result += '\tRating: ' + str(self.rating) + '\n'
        result += '\tTransactions:\n'
        for transaction in self.transactions:
            result += '\t\t' + transaction + '\n'
        result += '\tLocation: ' + self.location[0] + ', ' + self.location[1] + '\n'
        result += '\tDisplay_phone: ' + self.display_phone + '\n'
        return result


class RestaurantList:
    def __init__(self, restaurants=None):
        if restaurants is None:
            restaurants = []
        self.restaurants = restaurants

    @staticmethod
    def from_json(json_dict) -> 'RestaurantList':
        restaurants = []
        for restaurant in json_dict['businesses']:
            restaurants.append(Restaurant.from_json(restaurant))
        return RestaurantList(restaurants)

    def print(self):
        result = ''
        for restaurant in self.restaurants:
            result += restaurant.print()
        return result

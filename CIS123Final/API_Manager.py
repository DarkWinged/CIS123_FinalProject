import requests


class APIManager:
    def __init__(self, end_point, api_key):
        self.end_point = end_point
        self.api_key = api_key

    def search(self, query=None):
        if query is None:
            query = {'location': 'Grand+Rapids'}
        authorization = {'Authorization': 'bearer %s' % self.api_key}

        print('Querying:', self.end_point + '/search?term=' + str(query['term'][0]) +
              '&limit=' + str(query['limit']) + '&radius=' + str(query['radius']) +
              '&location=' + str(query['location']))
        response = requests.get(url=self.end_point + '/search', params=query, headers=authorization)

        print('Response Status:', str(response.status_code) + '\n')
        return response

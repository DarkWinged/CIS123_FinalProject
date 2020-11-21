import requests


if __name__ == '__main__':
    response = requests.get("http://api.cis_final.com/")
    print(response.status_code)

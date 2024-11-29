import requests
import json
import time

example_route_list = [3031, 3069]
base_url = "https://mbus.ltp.umich.edu/bustime/api/v3/getpredictions?key=XK7KWXPKfR8bYGqUTQrJcgV7i&format=json&stpid=C250"
full_url = base_url

def make_request(url):
    data = requests.get(url)
    print(data)
    json_data = data.json()
    print(json_data)
    json_string = json.dumps(json_data, indent=4)
    print(json_string)
    return(json_data)

bustime_data = make_request(full_url)

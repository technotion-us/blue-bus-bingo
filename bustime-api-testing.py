import requests
import json
import time

route_list = ['BB', 'NW']
base_url = "https://mbus.ltp.umich.edu/bustime/api/v3/getvehicles?key=XK7KWXPKfR8bYGqUTQrJcgV7i&format=json&rt=BB,NW"


# for item in route_list:
#     if item == route_list[-1]:
#         print(f'Getting route: {item}.')
#         extra_bit = item
#         url = base_url + extra_bit
#         data = requests.get(url)
#         print(data)
#         json_data = data.json()
#         print(json_data)
#         json_string = json.dumps(json_data, indent=4)
#         print(json_string)
#     else:
#         print(f'Getting route: {item}.')
#         extra_bit = item
#         url = base_url + extra_bit
#         data = requests.get(url)
#         print(data)
#         json_data = data.json()
#         print(json_data)
#         json_string = json.dumps(json_data, indent=4)
#         print(json_string)
#         print('Waiting 15s before next call')
#         time.sleep(15)
    

import requests
import json
import time


# Dani, please figure out how to ask the user for which routes they want to ride, then based on that response, put the route 2 letter codes (BB, NW, etc) into the example_route_list variable

# EXAMPLE DATA
example_ridden_bus_list = [3031, 3028, 3050, 3010]
example_route_list = ['BB', 'NW', 'CN']

# Base URL to make request, route string to concat route codes together, full URL to make entire request
base_url = "https://mbus.ltp.umich.edu/bustime/api/v3/getvehicles?key=XK7KWXPKfR8bYGqUTQrJcgV7i&format=json&rt="
route_str = ",".join(example_route_list)
full_url = base_url + route_str

def make_request(url):
    data = requests.get(url)
    print(data)
    json_data = data.json()
    # print(json_data)
    # json_string = json.dumps(json_data, indent=4)
    # print(json_string)
    return(json_data)

bustime_data = make_request(full_url)

# Master dictionary of buses on routes not yet ridden
vid_dict = {}

# Creates list in dictionary for each requested route
for route in example_route_list:
    vid_dict[route] = []

# Gets info for all active vehicles on requested routes
vehicle_info = bustime_data['bustime-response']['vehicle']

# For vehicle in vehicle info, get vehicle ID (vid) and check which route it is on. If it is on requested route,
# and has not been ridden yet, print that you found it and append it to the list inside the dictionary.
for i in vehicle_info:
    vid = int(i['vid'])
    if vid not in example_ridden_bus_list:
        for route in example_route_list:
            if i['rt'] == route:
                print(f'Found bus # {vid} on route {route}. Adding to list.')
                vid_dict[route].append(vid)
                vid_dict.get(route, vid)

# Print final results
print(f'Buses active that are not yet ridden: {vid_dict}')

import requests
import json
import time

example_ridden_bus_list = [3031, 3028, 3050, 3010]
example_route_list = ['BB', 'NW', 'OS']
example_stop = "C250"

# INPUT - string identifying which technique to use, "route" or "stop"
# INPUT 2 - string identifying list of routes or stop to query buses on

# Return - JSON in either route or pred format
# Route Return -
# Stop (pred) Return -

# Example call - get_vehicles(route, example_route_list) OR get_vehicles(stop, "C250")

def get_vehicles(inp, inp2):

    if inp == "route":

        # Base URL to make request, route string to concat route codes together, full URL to make entire request
        base_url = "https://mbus.ltp.umich.edu/bustime/api/v3/getvehicles?key=XK7KWXPKfR8bYGqUTQrJcgV7i&format=json&rt="
        route_str = ",".join(inp2)
        full_url = base_url + route_str

        data = requests.get(full_url)
        print(data)
        json_data = data.json()
        # print(json_data)
        # json_string = json.dumps(json_data, indent=4)
        # print(json_string)
        return(json_data)

    elif inp == "stop":

        # Base URL to make request, route string to concat route codes together, full URL to make entire request
        base_url = "https://mbus.ltp.umich.edu/bustime/api/v3/getpredictions?key=XK7KWXPKfR8bYGqUTQrJcgV7i&format=json&stpid="
        user_stop = inp2
        full_url = base_url + user_stop

        data = requests.get(full_url)
        print(data)
        json_data = data.json()
        # print(json_data)
        # json_string = json.dumps(json_data, indent=4)
        # print(json_string)

        return(json_data)

# INPUT - BUS FEED
# INPUT 2 - ROUTE LIST
# COMPARE RIDEN BUSES VS ALL BUSES

def calc_pred(data, routes):

    # Master dictionary of buses on routes not yet ridden
    vid_dict = {}

    # Creates list in dictionary for each requested route
    for route in example_route_list:
        vid_dict[route] = []

    # Gets info for all active vehicles on requested routes
    if "vehicle" in data['bustime-response']:
        vehicle_info = data['bustime-response']['vehicle']
    elif 'prd' in data['bustime-response']:
        vehicle_info = data['bustime-response']['prd']
    else:
        print("bad data")
        return

    ridden_buses = example_ridden_bus_list

    # For vehicle in vehicle info, get vehicle ID (vid) and check which route it is on. If it is on requested route,
    # and has not been ridden yet, print that you found it and append it to the list inside the dictionary.
    for i in vehicle_info:
        vid = int(i['vid'])
        pred = i['prdtm']
        pred_time = (f"{(int(pred[-2:]) - int(i['tmstmp'][-2:]))} min")
        bus_tuple = (vid, pred_time)
        if vid not in ridden_buses:
            for route in routes:
                if i['rt'] == route:
                    if bus_tuple not in vid_dict[route]:
                        print(f'Found bus # {vid} on route {route}. Arrving in {pred_time}. Adding to list.')
                        vid_dict[route].append(bus_tuple)
                        # vid_dict.get(route, vid)
    # Print final results
    print(f'Buses active that are not yet ridden: {vid_dict}')
    return(vid_dict)

def calc_buses(data, routes):

    # Master dictionary of buses on routes not yet ridden
    vid_dict = {}

    # Creates list in dictionary for each requested route
    for route in routes:
        vid_dict[route] = []

    # Gets info for all active vehicles on requested routes
    if "vehicle" in data['bustime-response']:
        vehicle_info = data['bustime-response']['vehicle']
    elif 'prd' in data['bustime-response']:
        vehicle_info = data['bustime-response']['prd']
    else:
        print("bad data")
        return

    ridden_buses = example_ridden_bus_list

    # For vehicle in vehicle info, get vehicle ID (vid) and check which route it is on. If it is on requested route,
    # and has not been ridden yet, print that you found it and append it to the list inside the dictionary.
    for i in vehicle_info:
        vid = int(i['vid'])
        if vid not in ridden_buses:
            for route in routes:
                if i['rt'] == route:
                    print(f'Found bus # {vid} on route {route}. Adding to list.')
                    vid_dict[route].append(vid)
                    # vid_dict.get(route, vid)

    # Print final results
    print(f'Buses active that are not yet ridden: {vid_dict}')
    return(vid_dict)

vid_data = get_vehicles("stop", "C250")
active_list = calc_pred(vid_data, example_route_list)
"""
Created on Monday, Nov 25 2019
Author: Ejona Kocibelli
Project Description: Using Web API's and JSON
"""

import json
import urllib.error
import urllib.parse
import urllib.request
from math import pi, sin, cos, sqrt, asin
import sys


def lookup_address(street_name, city_name, state_name, zip_code):
    """lookup_address function get's the parameters from the user input and gets them ready for encoding"""
    parameters = {'street': street_name, 'city': city_name, 'state': state_name, 'zip': zip_code,
                  'benchmark': 'Public_AR_Current', 'format': 'json'}
    parameters = urllib.parse.urlencode(parameters)  # encode the params
    url = 'https://geocoding.geo.census.gov/geocoder/locations/address'
    url = url + '?' + parameters  # append the params to the URL
    try:
        json_ = urllib.request.urlopen(url).read()  # raise an URLError if the request cannot take place
    except urllib.error.URLError:
        print('An error occurred while looking up the address!')
    else:
        json_ = json_.decode()  # decode the response and return the json back
        return json_


def parse_address_json(json_data):
    """parse_address_json takes the json response from lookup_address and parses out the coordinates from the json"""
    try:
        json_data = json.loads(json_data)
        coordinates = json_data['result']['addressMatches'][0]['coordinates']
        return coordinates
    except IndexError:
        print('The address could not be found! Please check the address and try again.')
        sys.exit()


def find_address():
    """find_address function gets user input address, and Whitehouse address and calculates the distance between them"""
    street_name = input('Enter your house number and street name: ')
    city_name = input('Enter your city: ')
    state_name = input('Enter your state: ')
    zip_code = input('Enter your zip code: ')

    if len(street_name) == 0 or len(city_name) == 0 or len(state_name) == 0 or len(zip_code) == 0:
        print('One or more of your inputs was blank. All fields are required. Please try again!')
    else:
        user_address_json = lookup_address(street_name, city_name, state_name, zip_code)  # lookup user address
        user_coordinates = parse_address_json(user_address_json)  # parse user address json to coordinates

        user_longitude = float(user_coordinates['x'])
        user_latitude = float(user_coordinates['y'])

        street_name = "1600 Pennsylvania Ave NW"  # White House address
        city_name = "Washington"
        state_name = "DC"
        zip_code = "20500"

        white_house_address_json = lookup_address(street_name, city_name, state_name, zip_code)
        white_house_coordinates = parse_address_json(white_house_address_json)
        white_house_longitude = float(white_house_coordinates['x'])
        white_house_latitude = float(white_house_coordinates['y'])

        try:
            user_lon_radians = user_longitude * pi / 180
            user_lat_radians = user_latitude * pi / 180
            white_house_lon_radians = white_house_longitude * pi / 180
            white_house_lat_radians = white_house_latitude * pi / 180
        except UnboundLocalError:
            print('An unexpected error occurred! Please try again.')
        else:
            earth_radius = 3956  # approximate radius of earth in miles
            distance_longitude = user_lon_radians - white_house_lon_radians  # longitude distance
            distance_latitude = user_lat_radians - white_house_lat_radians   # latitude distance

            a = sin(distance_latitude / 2) ** 2 + cos(white_house_lat_radians) * cos(user_lat_radians) * sin(distance_longitude / 2) ** 2
            c = 2 * asin(min(1, sqrt(a)))

            distance = earth_radius * c
            distance = round(distance)  # round to the nearest mile
            print(f'The distance between your home and The White House is about {distance} miles.')


def main():
    find_address()


if __name__ == '__main__':
    main()

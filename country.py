import requests
import json

from Python_data.robot.new_class.module.Tony.functions import talk, listen


def country_api(country) -> object:
    items = ['name', 'capital', 'population', 'region', 'flag', 'currency']
    my_dict = {}
    values = []

    url = f'https://restcountries.eu/rest/v2/name/{country}'
    response = requests.get(url)

    if response.ok:
        values = json.loads(response.text)
    else:
        return False
    for key, value in values[0].items():
        if key in items:
            my_dict[key] = value
    return my_dict


def country_name():
    talk('what is the name of your country?')
    country = listen()
    print(country)
    return country_api(country)


def country_highlights():
    result = country_name()
    if result:
        name, capital, region, population, flag = result.values()
        response = f'the capital of {name} is {capital}, it has {population} amount of citizens and the region is in ' \
                   f'{region}'
        talk(response)
    return 'the country doesnt exist'


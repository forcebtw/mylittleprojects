from requests import get

city1 = input()
city2 = input()
cities = [city1,city2]


def weatherpr(cities):
    for city in cities:
        try:
            weather = get(f'http://wttr.in/{city}')
            weather.raise_for_status()
        except Exception as err:
            print(f'error occurred: {err}')
        else:
            print(weather.text)
        print(weather)

weatherpr(cities)

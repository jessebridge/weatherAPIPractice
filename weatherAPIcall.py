import requests


def get_temperature(json_data):
    temp_in_celcius = json_data['main']['temp']
    return temp_in_celcius

def get_weather_type(json_data):
    weather_type = json_data['weather'][0]['description']
    return weather_type

def get_wind_speed(json_data):
    wind_speed = json_data['wind']['speed']
    return wind_speed



def get_weather_data(json_data, city):
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = ''
    return weather_details + ("The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} km/ph".format(city, weather_type, temperature, wind_speed))


def main():
    city = input("City Name : ")
    units_format = "&units=metric"
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
    final_url = api_address + units_format
    json_data = requests.get(final_url).json()
    weather_details = get_weather_data(json_data, city)
    # print the json_object
    print(json_data)
    # print formatted data
    print(weather_details)



main()

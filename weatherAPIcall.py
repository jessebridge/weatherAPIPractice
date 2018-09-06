
def main():
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Sydney,au&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
    city = input("City Name : ")
    final_url = api_address + city
    # json_data = requests.get(final_url)




main()

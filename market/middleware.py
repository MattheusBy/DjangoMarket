import requests
import json
from bs4 import BeautifulSoup
import os
import django
from django.contrib.auth.models import User

from market.models import CustomUser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_server.settings")
django.setup()


def get_user_city(get_response):
    def middleware(request):
        if request.user == User.objects.get(username="admin"):
            request.city = "Минск"
        else:
            if request.user.is_authenticated:
                request.city = CustomUser.objects.get(user_for_city=request.user)
            else:
                request.city = "Минск"

        url = "http://api.openweathermap.org/geo/1.0/direct?q={0},BY&limit=1&appid=b09bd89bc931d83516a203e87c35997d". \
            format(request.city)

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
        }

        req = requests.get(url, headers=headers)
        src = req.text
        with open("parsed_weather.html", "w") as file:
            file.write(src)

        with open("parsed_weather.html", "r") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        name_city = soup.find("p")  # find tag p
        temp = json.loads(name_city.text)  # get value from soap
        temp_dict = temp[0]  # transform from soap to python obj
        city_user_lat = temp_dict.get('lat')  # get values
        city_user_lon = temp_dict.get('lon')
        coord_user = (city_user_lat, city_user_lon,)

        url_2 = 'https://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid=b09bd89bc931d83516a203e87c35997d'.format(
            coord_user[0], coord_user[1])
        headers_2 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
        }

        req2 = requests.get(url_2, headers=headers_2)
        src2 = req2.text
        with open("parsed_weather_2.html", "w") as file:
            file.write(src2)

        with open("parsed_weather_2.html", "r") as file:
            src2 = file.read()

        soup2 = BeautifulSoup(src2, "lxml")
        data_weather = soup2.find("p")  # find tag p
        data_weather_text = json.loads(data_weather.text)
        get_weather = data_weather_text.get('main')

        temp_kelvin = get_weather.get('temp')
        temp_celsius = round(float(temp_kelvin) - 273.15, 1)
        temp_feels_like_kelvin = get_weather.get('feels_like')
        temp_feels_like_celsius = round(float(temp_feels_like_kelvin) - 273.15, 1)
        request.weather_final = (temp_celsius, temp_feels_like_celsius,)

        print(request.weather_final, request.city)
        response = get_response(request)
        return response

    return middleware

"""
Custom middleware to get information about user's city from DB.
The module get information about weather in user's city according
OpenWeatherAPI
"""

import requests
import os
import django
from django.contrib.auth.models import User

from market.models import CustomUser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_server.settings")
django.setup()
# API-key to access OpenWeatherAPI-service
API_key = "b09bd89bc931d83516a203e87c35997d"


def get_user_city(get_response):
    # custom middleware
    def middleware(request):
        # check user's authorization
        if not request.user:
            request.city = "Минск"
        else:
            if request.user == User.objects.get(username="admin"):
                request.city = "Минск"
            else:
                if request.user.is_authenticated:
                    # get user's city from DB
                    request.city = CustomUser.objects.get(
                        user_for_city=request.user
                    )
                else:
                    request.city = "Минск"

                url = "http://api.openweathermap.org/geo/1.0/" \
                      "direct?q={0},BY&limit=1&" \
                      "appid=b09bd89bc931d83516a203e87c35997d".format(
                    request.city
                )
                # url OpenWeatherAPI to get coordinates of
                # user's city

                headers = {
                    "Accept": "text/html,application/xhtml+xml,"
                              "application/xml;q=0.9,image/avif,"
                              "image/webp,*/*;q=0.8",
                    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; "
                                  "Linux x86_64; rv:95.0) "
                                  "Gecko/20100101 Firefox/95.0"
                }

                req = requests.get(url, headers=headers)
                # get coordinates of user's city
                lat = req.json()[0]['lat'] # user's city latitude
                lon = req.json()[0]['lon'] # user's city longitude

                # send API-key, user's city longitude and latitude
                url_weather = f"https://api.openweathermap.org" \
                              f"/data/2.5/weather?" \
                              f"lat={lat}&lon={lon}&appid={API_key}"

                req = requests.get(url_weather, headers=headers)
                # get real temperature in city
                request.real_temp = round(
                    int(req.json()['main']['temp']) - 273.15
                )
                # get feels like temperature in city
                request.feels_temp = round(
                    int(req.json()['main']['feels_like']) - 273.15
                )
                #get humidity in city
                request.humidity = req.json()['main']['humidity']

                response = get_response(request)
                return response

    return middleware

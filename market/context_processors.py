"""This file provides tempretures and user's city for context processor. Then it displays in base.html """
def weather_parsed(request):
    return {
            "city": request.city,
            'real_temperature': request.weather_final[0],
            'feels_like_temperature': request.weather_final[1]
        }

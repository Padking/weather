from typing import Dict

import requests


URLOptions = Dict[str, str]

cities = ["Лондон", "Шереметьево", "Череповец"]
payload = {"mnTqu": "", "lang": "ru"}


def get_weather_forecast_info(city: str, payload: URLOptions):
    """
    Выполняет http-з для получения информации
    о погоде в конкретном городе с учётом опций (согласно http://wttr.in)

    :param location: местоположение
    :param payload: опции

    """

    url_template = "http://wttr.in/{}?{}"
    url = url_template.format(city, payload)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    info = response.text
    return info


for city in cities:
    info = get_weather_forecast_info(city, payload)
    print(info)

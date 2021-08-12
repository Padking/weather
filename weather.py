from typing import Dict

import requests


URLOPTIONS = Dict[str, str]


def get_weather_forecast(location: str, payload: URLOPTIONS):
    """Получает сведения о погоде.

    Выполняет http-запрос для получения информации
    о погоде в конкретном месте пространства
    с учётом опций (согласно http://wttr.in)

    :param location: местоположение
    :param payload: опции
    :return: прогноз погоды
    """

    url_template = "http://wttr.in/{}"
    url = url_template.format(location)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    weather_forecast = response.text
    return weather_forecast


def main():
    """Выполняет основную логику модуля."""

    locations = ["Лондон", "Шереметьево", "Череповец"]
    payload = {"mnTq": "", "lang": "ru"}
    for location in locations:
        weather_forecast = get_weather_forecast(location, payload)
        print(weather_forecast)


if __name__ == "__main__":
    main()

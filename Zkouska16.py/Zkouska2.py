# Příklad 2: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `fetch_weather_data`, která:
# 1. Přijme jako parametr město (`city`), s tímto městem a klíčem `api_key` získejte aktuální teplotu z url `http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}`.
# 2. Teplota je uložená v slovníku `main` pod klíčem `temp` v Kelvinech.
# 3. Funkce vrátí teplotu v °C zaokrouhlenou na dvě desetinná místa (273.15 °K = 0 °C).


import requests


# API klíč pro OpenWeatherMap
api_key = 'a023a3be26e530f37924110734b494b1'


def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)  # Posíláme požadavek na API -> uložený do response
    if response.status_code == 200:  # Kontrola, zda API odpovědělo správně
        data = response.json()  # Převedení JSON na Python slovník
        temp_kelvin = data["main"]["temp"]  # Načtení teploty v Kelvinech
        temp_celsius = temp_kelvin - 273.15  # Převod na stupně Celsia
        return round(temp_celsius, 2)  # Vrací zaokrouhlenou teplotu
    else:
        print(f"Nepodařilo se načíst data o počasí.Stavový kód: {response.status_code}")   
        return None



if __name__ == "__main__":
    city = input("Enter city name: ")
    temperature = fetch_weather_data(city)
    print(f"Current temperature in {city}: {temperature} °C")
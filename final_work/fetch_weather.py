import requests
import pandas as pd
from datetime import datetime, timedelta

# Ваш API-ключ
API_KEY = ''
# Список городов
cities = ['London', 'New York', 'Tokyo', 'Moscow', 'Paris']
# Базовый URL API
base_url = 'http://api.openweathermap.org/data/2.5/'

# Функция для получения данных о погоде
def get_weather(city):
    url = f"{base_url}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        'city': city,
        'temperature': data['main']['temp'],
        'date': datetime.utcfromtimestamp(data['dt'])
    }

# Собираем данные за последний месяц
end_date = datetime.utcnow()
start_date = end_date - timedelta(days=30)

weather_data = []

for city in cities:
    try:
        data = get_weather(city)
        weather_data.append(data)
    except Exception as e:
        print(f"Ошибка при получении данных для {city}: {e}")

# Создаем DataFrame
df = pd.DataFrame(weather_data)

# Сохраняем в файл
df.to_csv('weather_data.csv', index=False)

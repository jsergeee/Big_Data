Вот подробный пошаговый план выполнения задания по сбору, анализу, визуализации и работе с данными о погоде в рамках курса по Big Data.

---

## Шаг 1. Сбор данных о погоде за последний месяц

### 1.1. Выбор источника данных
- Используйте открытые API погодных сервисов, например:
  - OpenWeatherMap (https://openweathermap.org/api)
  - WeatherAPI (https://www.weatherapi.com/)
- Зарегистрируйтесь и получите API-ключ.

### 1.2. Выбор городов
- Определите список городов мира, например: Москва, Нью-Йорк, Лондон, Токио, Париж.
- Можно взять 5-10 городов для разнообразия.

### 1.3. Получение данных через API
- Используйте Python и библиотеки `requests` для обращения к API.
- Пример кода для получения данных о погоде:

```python
import requests
import json
from datetime import datetime, timedelta

API_KEY = 'ваш_api_ключ'
cities = ['Moscow', 'New York', 'London', 'Tokyo', 'Paris']
results = {}

for city in cities:
    # Получение координат города или использование прямых запросов
    # Для OpenWeatherMap можно использовать их эндпоинт для исторических данных, но он платный.
    # Альтернативно, используйте предсохранённые данные или API с историей.
    # Для примера возьмем текущие данные (или симулируем за последний месяц).
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    # Обработка данных: собираем температуру по датам
    temps = []
    for entry in data['list']:
        dt = datetime.fromtimestamp(entry['dt'])
        temp = entry['main']['temp']
        temps.append({'date': dt, 'temp': temp})
    results[city] = temps
```

**Примечание:** Для исторических данных потребуется платный API или использование данных из других источников. Для учебных целей можно сгенерировать или использовать архивные данные.

### 1.4. Альтернатива: Веб-скрейпинг
- Если API недоступен, используйте `BeautifulSoup` для парсинга сайтов с погодой.
- Например, сайт `https://www.worldweatheronline.com/` или любой другой, предоставляющий исторические данные.

---

## Шаг 2. Анализ и визуализация данных

### 2.1. Построение графика изменения температуры по датам для каждого города
- Используйте Python и библиотеки `matplotlib` или `seaborn`.
- Пример кода:

```python
import matplotlib.pyplot as plt

for city, data in results.items():
    dates = [entry['date'] for entry in data]
    temps = [entry['temp'] for entry in data]
    plt.plot(dates, temps, label=city)

plt.xlabel('Дата')
plt.ylabel('Температура (°C)')
plt.title('Изменение температуры за последний месяц')
plt.legend()
plt.show()
```

### 2.2. Построение распределения температуры
- Соберите все температуры в один массив.
- Постройте гистограмму:

```python
all_temps = []
for data in results.values():
    all_temps.extend([entry['temp'] for entry in data])

plt.hist(all_temps, bins=20, alpha=0.7)
plt.xlabel('Температура (°C)')
plt.ylabel('Количество случаев')
plt.title('Распределение температуры за последний месяц')
plt.show()
```

---

## Шаг 3. Сохранение результатов в HDFS

### 3.1. Установка и настройка Hadoop
- Убедитесь, что Hadoop установлен и настроен локально или на сервере.

### 3.2. Подготовка данных для сохранения
- Сохраните собранные данные в файл в формате CSV или JSON:

```python
import json

with open('weather_data.json', 'w') as f:
    json.dump(results, f)
```

или

```python
import csv

with open('weather_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['City', 'Date', 'Temperature'])
    for city, data in results.items():
        for entry in data:
            writer.writerow([city, entry['date'].strftime('%Y-%m-%d'), entry['temp']])
```

### 3.3. Загрузка файла в HDFS
- Используйте команду `hadoop fs -put`:

```bash
hadoop fs -mkdir /user/ваш_пользователь/weather_data
hadoop fs -put weather_data.json /user/ваш_пользователь/weather_data/
```

или для CSV файла:

```bash
hadoop fs -put weather_data.csv /user/ваш_пользователь/weather_data/
```

---

## Шаг 4. Выгрузка результатов из HDFS на локальный компьютер

### 4.1. Использование команды `hadoop fs -get`
- Выполните команду:

```bash
hadoop fs -get /user/ваш_пользователь/weather_data/weather_data.json ./local_folder/
```

или для CSV:

```bash
hadoop fs -get /user/ваш_пользователь/weather_data/weather_data.csv ./local_folder/
```

- После этого файл будет скопирован в локальную папку `local_folder`.

---

## Итоги:
- Собрали данные о погоде с помощью API или скрейпинга.
- Построили графики изменений температуры и распределения.
- Сохранили результаты в файл и загрузили их в HDFS.
- Выгрузили файлы из HDFS на локальный компьютер.

---

Если потребуется помощь с конкретным кодом или настройками — обращайтесь!

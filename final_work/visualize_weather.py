import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_csv('weather_data.csv', parse_dates=['date'])

# График изменения температуры по дням для каждого города
plt.figure(figsize=(12, 6))
for city in df['city'].unique():
    city_df = df[df['city'] == city]
    plt.plot(city_df['date'], city_df['temperature'], label=city)

plt.xlabel('Дата')
plt.ylabel('Температура (°C)')
plt.title('Изменение температуры в городах за последний месяц')
plt.legend()
plt.tight_layout()
plt.savefig('temperature_trends.png')
plt.show()

# Гистограмма распределения температуры
plt.figure(figsize=(8, 6))
plt.hist(df['temperature'], bins=20)
plt.xlabel('Температура (°C)')
plt.ylabel('Количество записей')
plt.title('Распределение температуры за последний месяц')
plt.savefig('temperature_distribution.png')
plt.show()

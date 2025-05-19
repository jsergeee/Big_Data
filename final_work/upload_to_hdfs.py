from hdfs import InsecureClient

# Подключение к HDFS
client = InsecureClient('http://localhost:9870', user='hadoop')  # замените URL и пользователя при необходимости

# Пути локальных файлов
local_files = ['weather_data.csv', 'temperature_trends.png', 'temperature_distribution.png']

# Папка на HDFS
hdfs_dir = '/user/your_username/weather_data/'

# Создаем директорию на HDFS (если не существует)
client.makedirs(hdfs_dir)

# Загружаем файлы
for file in local_files:
    with open(file, 'rb') as f:
        filename = file.split('/')[-1]
        client.write(f'{hdfs_dir}{filename}', f, overwrite=True)
    print(f'Загружено {file} в {hdfs_dir}')

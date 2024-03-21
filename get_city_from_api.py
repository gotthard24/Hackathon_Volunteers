import json
import requests
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'rfrfirf1234'
DATABASE = 'Israel_citys'

# URL базового запроса к API GeoNames для поиска городов
base_url = 'http://api.geonames.org/searchJSON'
# Параметры запроса для поиска всех городов Израиля
params = {
    'country': 'IL',    # Код страны Израиль (IL)
    'featureCode': 'PPL',  # Код фичи (PPL) обозначает город
    'maxRows': 1000,     # Максимальное количество результатов (максимум 1000)
    'username':'flet1234',  # Ваш пользовательский API ключ GeoNames
    'startRow': 0
}

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()


while True:
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()

        # Вставка данных о городах в таблицу
        for city in data['geonames']:
            name = city['name']
            latitude = city['lat']
            longitude = city['lng']
            insert_query = 'INSERT INTO israel_citys (name, latitude, longitude) VALUES (%s, %s, %s)'
            cursor.execute(insert_query, (name, latitude, longitude))
            connection.commit()

        # Проверка, есть ли еще страницы результатов
        if len(data['geonames']) < 1000:
            break  # Выход из цикла, если это последняя страница результатов
        else:
            params['startRow'] += 1000  # Увеличение начальной строки для следующего запроса
    else:
        print('Error:', response.status_code)
        break

# Закрытие соединения с базой данных
cursor.close()
connection.close()

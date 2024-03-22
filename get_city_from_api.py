import json
import requests
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'rfrfirf1234'
DATABASE = 'Israel_citys'

# URL
base_url = 'http://api.geonames.org/searchJSON'
# Params iwth only Israely places
params = {
    'country': 'IL',    
    'maxRows': 1000,    
    'username':'flet1234', 
    'startRow': 0
}

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()


while True:
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()

        # Insert and filter via repeated names, and population
        if 'geonames' in data:
            for city in data['geonames']:
                search_query = f'SELECT name FROM israel_citys WHERE name = %s'
                cursor.execute(search_query, (city['name'],))
                result=cursor.fetchone()
                if result is None:
                    if city['population']>0:
                        name = city['name']
                        latitude = city['lat']
                        longitude = city['lng']
                        insert_query = 'INSERT INTO israel_citys (name, latitude, longitude) VALUES (%s, %s, %s)'
                        cursor.execute(insert_query, (name, latitude, longitude))
                        connection.commit()
                    else:
                        continue
                else:
                    continue
        else:
            break

        # Checking if we have more variants
        if len(data['geonames']) < 1000:
            break  # If not
        else:
            params['startRow'] += 1000  # next page
    else:
        print('Error:', response.status_code)
        break

# Closing connection
cursor.close()
connection.close()

# # Test cases for me>>>
# response = requests.get(base_url, params=params)
# data = response.json()
# print(data['geonames'])
# # for x in data['geonames']:
# #     print(x['name'])
# #     print(x['lng'])
# #     print(x['lat'])

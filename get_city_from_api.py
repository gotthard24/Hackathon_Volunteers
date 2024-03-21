import json
import requests
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'rfrfirf1234'
DATABASE = 'Israel_citys'

url = 'https://parseapi.back4app.com/classes/Israelcities_City?order=name&keys=name,country,population,location'
headers = {
    'X-Parse-Application-Id': 'Xx464w5mp7nzAquK06LbZupSLd21EYgT4Bor3BOV', # This is your app's application id
    'X-Parse-REST-API-Key': '6TQXHUmMUASJJ7dibLJEUpVyk92RdKIRRDBRP0wa' # This is your app's REST API key
}

params = {
    'limit':200,
    'order':'name',
    'keys':'name,country,location',
    'skip':0
}

all_results=[]

while True:
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.content.decode('utf-8')) # Here you have the data that you need
    all_results.extend(data['results'])
    if len(data['results'])<params['limit']:
        break
    params['skip']+=params['limit']

# print(f'Total:{len(all_results)}')
# print(all_results[0]['cityId'])


# for x in range(len(all_results)):
#     try:
#         connection=psycopg2.connect(host=HOSTNAME,user=USERNAME,password=PASSWORD,dbname=DATABASE)
#         cursor=connection.cursor()
#         query = f"""INSERT INTO israel_citys (name, latitude, longitude, cityid)
#         VALUES (%s, %s, %s, %s)"""
#         cursor.execute(query, (all_results[x]['name'], all_results[x]['location']['latitude'],all_results[x]['location']['longitude'],all_results[x]['cityId']))
#         connection.commit()
#     except psycopg2.Error as e:
#         print("Eror while conecting!")
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()


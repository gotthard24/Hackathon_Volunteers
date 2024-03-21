import config
import psycopg2

city_name='Haifa'

def find_latitude(city_name):
    connection=config.create_connection()
    cursor=connection.cursor()
    query = f"""SELECT latitude FROM israel_citys WHERE name = '{city_name}'"""
    cursor.execute(query)
    user_latitude=cursor.fetchone()[0]
    return user_latitude

def find_longitude(city_name):
    connection=config.create_connection()
    cursor=connection.cursor()
    query = f"""SELECT longitude FROM israel_citys WHERE name = '{city_name}'"""
    cursor.execute(query)
    user_longitude=cursor.fetchone()[0]
    return user_longitude

def make_city_list():
    citylist=[]
    connection=config.create_connection()
    cursor=connection.cursor()
    query = f"""SELECT city FROM organisations"""
    cursor.execute(query)
    result=cursor.fetchall()
    result=set(result)
    for city in result:
        citylist.append(city[0])
    return citylist

# newdik={}
# user_latitude=find_latitude(city_name)
# user_longitude=find_longitude(city_name)
# for city in make_city_list():
#     city_longitude=find_longitude(city)
#     city_latitude=find_latitude(city)
#     sub_longitude=user_longitude-city_longitude
#     sub_latitude=user_latitude-city_latitude
#     far_index=sub_latitude+sub_longitude
#     newdik[city]=far_index
# print(newdik)





# connection=config.create_connection()
# cursor=connection.cursor()
# query = f"""INSERT INTO israel_citys (name, latitude, longitude, cityid)
# VALUES (%s, %s, %s, %s)"""
# cursor.execute(query, (all_results[x]['name'], all_results[x]['location']['latitude'],all_results[x]['location']['longitude'],all_results[x]['cityId']))
# connection.commit()

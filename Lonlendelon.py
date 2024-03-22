import configdk

def find_latitude(city_name):
    connection=configdk.create_connection()
    cursor=connection.cursor()
    query = f"""SELECT latitude FROM israel_citys WHERE name = %s"""
    cursor.execute(query,(city_name,))
    user_latitude=cursor.fetchone()[0]
    return user_latitude


def find_longitude(city_name):
    connection=configdk.create_connection()
    cursor=connection.cursor()
    query = f"""SELECT longitude FROM israel_citys WHERE name = %s"""
    cursor.execute(query ,(city_name,))
    user_longitude=cursor.fetchone()[0]
    return user_longitude


def make_city_list():
    citylist=[]
    connection=configdk.create_connection()
    cursor=connection.cursor()
    query = f"""SELECT city FROM organisations"""
    cursor.execute(query)
    result=cursor.fetchall()
    result=set(result)
    for city in result:
        citylist.append(city[0])
    return citylist

# print(make_city_list())
def make_result_list(city_name):
    newdik={}
    user_latitude=find_latitude(city_name)
    user_longitude=find_longitude(city_name)
    for city in make_city_list():
        if city=='Tzfat':
            city='Safed'
        city_longitude=find_longitude(city)
        city_latitude=find_latitude(city)
        sub_longitude=user_longitude-city_longitude
        sub_latitude=user_latitude-city_latitude
        far_index=sub_latitude+sub_longitude
        newdik[city]=abs(far_index)
    result=list(newdik.items())
    return sorted(result, key=lambda x:x[1])

def test():
    print("I'm in!")




# print(find_latitude('Haifa'))
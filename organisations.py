import psycopg2
import random

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '474747kk'
DATABASE = 'W4Hackathon'
ORGS = 'organisations'
CITIES = 'israel_citys'

def execute_query(query, parameters=None):
        results = []
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()       
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        try:    
            results = cursor.fetchall()
        except:
            pass
        connection.commit()
        connection.close()
        if len(results) > 0:
            return results      
        
def create_insert_query(name,topic,url,donate_url,description):
    query = f"""
        INSERT INTO {ORGS} (name, city, topic, url, donate_url,discription)
        VALUES
            ('{name}', %s,'{topic}', '{url}','{donate_url}', '{description}');
        """
    return query

def add_org_to_db(query, cities):
    for i in range(random.randint(100, 150)):
        execute_query(query,(cities[i][1],))
        
def select_volunteers():
    pass

def select_donate():
    pass

def test():
    print("OK")
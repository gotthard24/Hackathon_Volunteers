import random
import configdk

def execute_query(query, parameters=None):
        results = []
        connection = configdk.create_connection()
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
        INSERT INTO {configdk.ORGS} (name, city, topic, url, donate_url,discription)
        VALUES
            ('{name}', %s,'{topic}', '{url}','{donate_url}', '{description}');
        """
    return query

def add_org_to_db(query, cities):
    for i in range(random.randint(100, 150)):
        execute_query(query,(cities[i][1],))
        
def select_city(city):
    query = f"""
        SELECT DISTINCT name FROM israel_citys
        WHERE name ILIKE '%{city}';
        """
        
    result = execute_query(query)
    return result
        
def select_volunteers(cities, topic):
    results = []
    for city in cities:
        if "'" in city:
            for i in range(len(city)):
                if city[i] == "'":
                    new_word = city[:i] + "'" + city[i:]
                    city = new_word
                    break
        query = f"""
            SELECT DISTINCT name, city, url, discription FROM organisations
            WHERE topic = '{topic}' AND city ILIKE '%{city}%';
            """
        result = execute_query(query)
        results.append(result)
            
    return results

def select_donate(topic):
    query = f"""
        SELECT DISTINCT name, donate_url FROM organisations
        WHERE topic = '{topic}';
        """
        
    result = execute_query(query)
    return result

def test():
    print("test")
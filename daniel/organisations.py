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
    
        
# select_cities_query = f"""
#             SELECT * FROM {CITIES}
#         """       
# magen_david_query = create_insert_query('Magen David Adom','Health', 'https://www.mdais.org/en/volunteers','https://www.mdais.org/en/donation', 'Magen David Adom (MDA), Israel''s national emergency medical service and blood bank, offers a dynamic Volunteer Program that engages individuals in various aspects of lifesaving and community support. As a Magen David Adom volunteer, participants receive comprehensive training in emergency medical response, first aid, and disaster relief, enabling them to serve as vital assets during crises and everyday emergencies. Volunteers contribute their time and skills across a range of activities, including ambulance assistance, blood drives, community education, and humanitarian aid efforts. Through their dedication and commitment, Magen David Adom volunteers play a crucial role in safeguarding public health and safety, making a meaningful difference in communities across Israel.')
# latet_query = create_insert_query('Latet','Social', 'https://www.latet.org.il/en/volunteering/','https://www.latet.org.il/en/2024purim/', 'Latet, one of Israel''s largest charitable organizations, offers impactful Volunteer Programs that address poverty and promote social justice throughout the country. Through Latet''s Volunteer Programs, individuals have the opportunity to engage in a variety of initiatives aimed at assisting disadvantaged populations. Volunteers play a crucial role in distributing food aid, organizing events, conducting outreach activities, and providing support to vulnerable individuals and families. Latet empowers volunteers to make a tangible difference in their communities by fostering connections, promoting empathy, and creating positive change. Through their dedication and collective efforts, Latet volunteers contribute to building a more equitable and compassionate society in Israel.')
# yad_sarah_query = create_insert_query('Yad Sarah','Health', 'https://yadsarah.org/about-us/','https://donation.asakimerp.com/Campaing/?CampaingID=51361', 'Yad Sarah, a prominent Israeli organization dedicated to assisting individuals with disabilities and the elderly, offers enriching Volunteer Programs that embody compassion and community support. Through Yad Sarah''s Volunteer Programs, individuals have the opportunity to engage in a range of impactful activities, including assisting with medical equipment rentals, providing transportation services, offering companionship to those in need, and participating in educational and recreational programs. Volunteers play a vital role in enhancing the quality of life for those served by Yad Sarah, fostering connections, and promoting independence and well-being. With their dedication and kindness, Yad Sarah volunteers contribute to creating a more inclusive and supportive society in Israel.')
# wwoof_query = create_insert_query('WWOOF','Animals', 'http://www.wwoof.org.il/guide/en','https://www.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-60453201HF760035N&useraction=COMMIT', 'WWOOF (World Wide Opportunities on Organic Farms) offers transformative Volunteer Programs that connect individuals with sustainable agriculture and organic farming practices worldwide. Through WWOOF Volunteer Programs, participants have the unique opportunity to live and work on organic farms, gaining hands-on experience in various aspects of farming, permaculture, and sustainable living. Volunteers engage in tasks such as planting, harvesting, animal care, and eco-building, while immersing themselves in the local culture and community. WWOOF empowers volunteers to learn new skills, foster connections with nature, and contribute to environmental stewardship and food sovereignty efforts globally. With WWOOF, volunteers embark on meaningful journeys of discovery, growth, and purposeful engagement in sustainable agriculture.')
# hadassah_query = create_insert_query('Hadassah-Israel','Social', 'https://hadassah-israel.org/','https://hadassah-israel.org/donate-now', 'Are you looking for a connection with other English speaking women who have made Aliyah?Want to make new friends, be part of a dynamic social group with regular meetings, support and volunteer at the Hadassah hospitals?Are you a life member of Hadassah in America? Life membership of Hadassah is transferrable to Hadassah-Israel, and you will continue to receive the quality Hadassah Magazine.Hadassah-Israel is a volunteer, Zionist, non-partisan women’s organization with chapters and groups all over the country. The organization works toward improving the quality of life in Israel in regards to health, education, new-immigrant absorption, women’s status and children at risk. Annual conferences, health study days, and national meetings provide stimulating topics and social interaction with members throughout the country.Join us -we will direct you to a chapter near your home.')

# cities = execute_query(select_cities_query)

# add_org_to_db(magen_david_query, cities)
# add_org_to_db(latet_query, cities)
# add_org_to_db(yad_sarah_query, cities)
# add_org_to_db(wwoof_query, cities)
# add_org_to_db(hadassah_query, cities)
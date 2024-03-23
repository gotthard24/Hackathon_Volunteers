import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '474747kk'
DATABASE = 'W4Hackathon'
ORGS = 'organisations'
CITIES = 'israel_citys'

def create_connection():
    return psycopg2.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    dbname=DATABASE)
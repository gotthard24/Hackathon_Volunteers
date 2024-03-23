import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'rfrfirf1234'
DATABASE = 'Israel_citys'
ORGS = 'organisations'
CITIES = 'israel_citys'

def create_connection():
    return psycopg2.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    dbname=DATABASE)


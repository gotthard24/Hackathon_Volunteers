import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '474747kk'
DATABASE = 'W4Hackathon'

def create_connection():
    return psycopg2.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    dbname=DATABASE)
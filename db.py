import psycopg2
import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()

db_params={
    'database': os.getenv('db_name'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'port': os.getenv('port'),
}


# def create():
#     conn=psycopg2.connect(**db_params)
#     cur=conn.cursor()
#     a="""create table talaba_query(
#     id serial PRIMARY KEY,
#     name varchar(20),
#     age int)"""
#     cur.execute(a)
#     conn.commit()
# create()




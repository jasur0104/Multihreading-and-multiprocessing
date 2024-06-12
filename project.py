from db import db_params
import psycopg2
import multiprocessing
import time
from datetime import datetime

def insert_data(query):
    conn = psycopg2.connect(**db_params)
    cur=conn.cursor()
    time.sleep(3)
    cur.execute(query)
    conn.commit()
def menyu():
    insert1="""insert into talaba_query(name,age) values ('jasur',19)"""
    insert2="""insert into talaba_query(name,age) values ('hikmat',19)"""
    insert3="""insert into talaba_query(name,age) values ('samandar',18)"""
    insert4="""insert into talaba_query(name,age) values ('akmal',20)"""
    insert5="""insert into talaba_query(name,age) values ('raxmonali',21)"""
    insert6="""insert into talaba_query(name,age) values ('sardor',22)"""
    insert7="""insert into talaba_query(name,age) values ('ali',19)"""
    insert8="""insert into talaba_query(name,age) values ('vali',25)"""
    insert9="""insert into talaba_query(name,age) values ('sevinch',17)"""

    process1=multiprocessing.Process(target=insert_data,args=(insert1,))
    process2=multiprocessing.Process(target=insert_data,args=(insert2,))
    process3=multiprocessing.Process(target=insert_data,args=(insert3,))
    process4=multiprocessing.Process(target=insert_data,args=(insert4,))
    process5=multiprocessing.Process(target=insert_data,args=(insert5,))
    process6=multiprocessing.Process(target=insert_data,args=(insert6,))
    process7=multiprocessing.Process(target=insert_data,args=(insert7,))
    process8=multiprocessing.Process(target=insert_data,args=(insert8,))
    process9=multiprocessing.Process(target=insert_data,args=(insert9,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    process9.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()
    process9.join()

if __name__ == "__main__":
    print(datetime.now())
    menyu()
    print(datetime.now())
""" izoh sifatida:bir vaqtni uzida  3 sekundda 9 ta malumot qushildi maulumotlat tipi bir xil lekn hajmi har xil qaytaradigan maulot ham
har hil shu sababali multiprocessing bizga ush quvvatni taqsimlayabdi yani bazisiga koproq bazilariga kamroq qilib
usha uchun xotiradan yutqazamiz vaqtdan yutamiz"""



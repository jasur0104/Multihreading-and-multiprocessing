""" Multihreadung >> bu xotiradan qoshimcha foydalangan holatda bizga javob qaytaradi
yani bu biror bir malumotni bittada yani bir nechta malumotmizni bittada uqish uchun vaqtdan yutishga yordam beradi
"""
import threading
import time
from datetime import datetime
def read_file(file_name:str):
    time.sleep(3)
    print(f'{file_name}> read')
    with open(file_name,'r') as file:
        data=file.read()
        print(f'{file_name} => {data} ga teng')
def menyu():
    file1='file1.txt'
    file2='file2.txt'
    file3='file3'
    file4='file4'
    file5='file5'
    file6='file6'
    file7='fil7'
    file8='file8'

    theding1=threading.Thread(target=read_file,args=(file1,))
    theding2=threading.Thread(target=read_file,args=(file2,))
    theding3=threading.Thread(target=read_file,args=(file3,))
    theding4=threading.Thread(target=read_file,args=(file4,))
    theding5=threading.Thread(target=read_file,args=(file5,))
    theding6=threading.Thread(target=read_file,args=(file6,))
    theding7=threading.Thread(target=read_file,args=(file7,))
    theding8=threading.Thread(target=read_file,args=(file8,))

    #start()
    theding1.start()
    theding2.start()
    theding3.start()
    theding4.start()
    theding5.start()
    theding6.start()
    theding7.start()
    theding8.start()

    #join()
    theding1.join()
    theding2.join()
    theding3.join()
    theding4.join()
    theding5.join()
    theding6.join()
    theding7.join()
    theding8.join()

if __name__ == "__main__":
    print(datetime.now())
    menyu()
    print(datetime.now())










import threading
import time
from datetime import datetime
def read_file(file_name:str):
    time.sleep(3)
    print(f'{file_name}> read')
    with open(file_name) as file:
        data=file.read()
        print(f'{file_name} => {data} ga teng')
def menyu():
    file1='file1.txt'
    file2='file2.txt'
    file3='file3'

    theding1=threading.Thread(target=read_file,args=(file1,))
    theding2=threading.Thread(target=read_file,args=(file2,))
    theding3 = threading.Thread(target=read_file, args=(file3,))
    theding1.start()
    theding2.start()
    theding3.start()
    theding1.join()
    theding3.join()
    theding2.join()
if __name__ == "__main__":
    print(datetime.now())
    menyu()
    print(datetime.now())






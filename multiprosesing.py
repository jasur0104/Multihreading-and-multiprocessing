""" Multiprocessinh  => bu ishlamay yotgan proseesorlarni ishlatib bizga javob qaytaradi
yani bir nechta file larga uzgartirish kiritsak bittada javob olamiz u filemiz
katta roq kichikroq file lar bulsa ham bittada natija olishimiz mumkun buladi yani prosessorimiz quvvatni
file hajmi katta kichikligiga qarab quvvatni buladi"""
import multiprocessing
import time
from datetime import datetime

def write_to_file(file_path, data):
    time.sleep(3)
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"Data written to {file_path}")

def main():
    file_path1 = 'file1.txt'
    file_path2 = 'file2.txt'
    file_path3 = 'file3.txt'
    file_path4 = 'file4.txt'
    data1 = 'Hello from Process 1!'
    data2 = 'Greetings from Process 2!'
    data3 ='Hello from Process 3!'
    data4 = 'Hello from Process 4!'
    # Create processes
    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2, data2))
    process3=multiprocessing.Process(target=write_to_file, args=(file_path3, data3))
    process4=multiprocessing.Process(target=write_to_file, args=(file_path4, data4))

    # Start processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())
from datetime import datetime
import os

while True:
    if os.stat("C:/Users/jonjw/PycharmProjects/cs-361 - Assignment 7/time.txt").st_size != 0:
        f = open("C:/Users/jonjw/PycharmProjects/cs-361 - Assignment 7/time.txt", "r+")
        start_array = f.readline().split()
        end_array = f.readline().split()
        
        f.close()
        time_1 = datetime.strptime(start_array[0],"%H:%M:%S")
        time_2 = datetime.strptime(end_array[0],"%H:%M:%S")

        difference = time_2 - time_1
        seconds = difference.total_seconds()
        assigned_num = seconds/3600

        t = open("C:/Users/jonjw/PycharmProjects/cs-361 - Assignment 7/translated-num.txt", "w")
        t.write(str(assigned_num))
        t.close()

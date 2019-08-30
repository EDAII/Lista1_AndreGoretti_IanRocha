import csv
import random

def nomes_reader():
    with open('nomes.csv') as csvfile:
        nomesCSV = csv.reader(csvfile, delimiter=',')
        for row in nomesCSV:
            print(row[1])

def cpfs_reader():
    with open('cpfs.csv') as csvfile:
        cpfsCSV = csv.reader(csvfile, delimiter=',')
        for row in cpfsCSV:
            print(row)

def random_date():
    day = random.randint(1,31)
    month = random.randint(1,12)
    year = random.randint(1980, 2019)

    print(day,"/",month,"/",year)
        

#nomes_reader()
#cpfs_reader()
for x in range(50):
    random_date()
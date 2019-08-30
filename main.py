import csv
import random

def nomes_reader():
    with open('nomes.csv') as csvfile:
        nomesCSV = csv.reader(csvfile, delimiter=',')
        aux = random.randint(1,100)
        auxs = str(aux)
        for x in nomesCSV:
            if auxs == x[0]:
                return x[1]

def cpfs_reader():
    with open('cpfs.csv') as csvfile:
        cpfsCSV = csv.reader(csvfile, delimiter=',')
        for row in cpfsCSV:
            return row[1]

def random_date():
    # day = random.randint(1,31)
    # month = random.randint(1,12)
    year = random.randint(1980, 2019)

    return year
        

# nomes_reader()
# cpfs_reader()
# for x in range(50):
#     random_date()

person = []
date = []
for k in range(51):
    person.append(nomes_reader())
    date.append(random_date())

teste = 1
while teste <= 50:
    print(person[teste])
    print(date[teste])
    teste += 1

    

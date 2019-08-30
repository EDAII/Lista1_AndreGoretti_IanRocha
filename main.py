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

def random_year():
    year = random.randint(1960, 2001)
    return year

def random_day():
    day = random.randint(1, 31)
    return day

def random_month():
    month = random.randint(1, 12)
    return month

def random_tel1():
    tel = random.randint(100, 999)
    return 3000 + int(tel)

def random_tel2():
    tel2 = random.randint(1000, 9999)
    return tel2

person = []
year = []
cpf = []
month = []
day = []
age = []
tel1 = []
tel2 = []
teste = 1

for k in range(51):
    person.append(nomes_reader())
    year.append(random_year())
    cpf.append(cpfs_reader())
    month.append(random_month())
    day.append(random_day())
    age.append(2019 - int(year[k]))
    tel1.append(random_tel1())
    tel2.append(random_tel2())

while teste <= 50:
    print("-----------------CADASTRO NÚMERO",teste,"----------------------")
    print("Nome:",person[teste])
    print("Nascimento:",day[teste],"/",month[teste],"/",year[teste])
    print("Idade:",age[teste])
    print("Número de Telefone:",tel1[teste],":",tel2[teste])
    teste += 1

    

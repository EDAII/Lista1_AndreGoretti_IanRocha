import csv
import random
from tkinter import *

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

def random_city():
    with open('cidades.csv') as csvfile:
        cidadesCSV = csv.reader(csvfile, delimiter=',')
        aux = random.randint(1, 20)
        for x in cidadesCSV:
            if str(aux) == x[0]:
                return x[1]

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
city = []
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
    city.append(random_city())

while teste <= 50:
    print("-----------------CADASTRO NÚMERO",teste,"----------------------")
    print("Nome:",person[teste])
    print("CPF:", cpf[teste])
    print("Nascimento:",day[teste],"/",month[teste],"/",year[teste])
    print("Idade:",age[teste])
    print("Número de Telefone:",tel1[teste],":",tel2[teste])
    print("Cidade:",city[teste])
    teste += 1

window = Tk()
 
window.title("Agenda")
 
#window.geometry('350x200')
 
lbl = Label(window, text="Nome")
 
lbl.grid(column=1, row=0)
 
EntradaN = Entry(window,width=10)
 
EntradaN.grid(column=2, row=0)
 
def clicked():
    Contato.config(state="normal")

    Contato.insert(INSERT, "apertei\n")
 
btn = Button(window, text="Buscar", command=clicked)
 
btn.grid(column=3, row=0)

Contato = Text(window, width = 30)

Contato.grid(column=0, row=0)

Contato.config(state="disabled")
 
window.mainloop()


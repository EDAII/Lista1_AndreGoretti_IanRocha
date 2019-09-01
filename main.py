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

def BuscaNome(nome):    
    achou = False
    i = 0
    while i <= 50:
        if person[i] == nome:
            achou = True
            return i
            break
        i += 1
        #print(nome)

window = Tk()
 
window.title("Agenda")
 
#window.geometry('350x200')
 
lblN = Label(window, text="Nome")
 
lblN.grid(column=0, row=1)

lblA = Label(window, text="Idade")
 
lblA.grid(column=0, row=2)
 
EntradaN = Entry(window,width=10)
 
EntradaN.grid(column=1, row=1)

EntradaA = Entry(window,width=10)
 
EntradaA.grid(column=1, row=2)
 
def clickedN():

    nomeB = EntradaN.get()

    i = BuscaNome(nomeB) 

    print(i)   

    Contato.config(state="normal")

    if(i != None):
        Contato.insert(INSERT, "Nome: ")
        Contato.insert(INSERT, person[i])
        Contato.insert(INSERT, "\n ")

        Contato.insert(INSERT, "CPF: ")
        Contato.insert(INSERT, cpf[i])
        Contato.insert(INSERT, "\n ")

        Contato.insert(INSERT, "idade: ")
        Contato.insert(INSERT, age[i])
        Contato.insert(INSERT, "\n ") 

        Contato.insert(INSERT, "Cidade: ")
        Contato.insert(INSERT, city[i])
        Contato.insert(INSERT, "\n ") 

        Contato.insert(INSERT, "Numero Telefone: ")
        Contato.insert(INSERT, tel1[i])
        Contato.insert(INSERT, "-")
        Contato.insert(INSERT, tel2[i])
        Contato.insert(INSERT, "\n ") 

        Contato.insert(INSERT, "Nascimento: ")
        Contato.insert(INSERT, day[i])
        Contato.insert(INSERT, "/")
        Contato.insert(INSERT, month[i])
        Contato.insert(INSERT, "/")
        Contato.insert(INSERT, year[i])           

    #Contato.insert(INSERT, )

def clickedA():

     Contato.config(state="normal")

     AgeB = int(EntradaA.get())
     
     j = 0
     while(j <= 50):
         
         if age[j] == AgeB:
            
            Contato.insert(INSERT, "Nome: ")
            Contato.insert(INSERT, person[j])
            Contato.insert(INSERT, "\n ")

            Contato.insert(INSERT, "CPF: ")
            Contato.insert(INSERT, cpf[j])
            Contato.insert(INSERT, "\n ")

            Contato.insert(INSERT, "idade: ")
            Contato.insert(INSERT, age[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Cidade: ")
            Contato.insert(INSERT, city[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Numero Telefone: ")
            Contato.insert(INSERT, tel1[j])
            Contato.insert(INSERT, "-")
            Contato.insert(INSERT, tel2[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Nascimento: ")
            Contato.insert(INSERT, day[j])
            Contato.insert(INSERT, "/")
            Contato.insert(INSERT, month[j])
            Contato.insert(INSERT, "/")
            Contato.insert(INSERT, year[j])
            Contato.insert(INSERT, "\n")
         j += 1        


 
btnNome = Button(window, text="Buscar", command=clickedN)

btnAge = Button(window, text="Buscar", command=clickedA)

btnAge.grid(column=2, row=2)
 
btnNome.grid(column=2, row=1)

Contato = Text(window, width = 30, height = 30)

Contato.grid(column=4, row=0)

Contato.config(state="disabled")
 
window.mainloop()


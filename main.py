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

def random_city():
    with open('cidades.csv') as csvfile:
        cidadesCSV = csv.reader(csvfile, delimiter=',')
        aux = random.randint(1, 20)
        for x in cidadesCSV:
            if str(aux) == x[0]:
                return x[1]

def random_cpf():
    cpf1 = random.randint(100, 999)
    cpf2 = random.randint(100, 999)
    cpf3 = random.randint(100, 999)
    cpf4 = random.randint(0,99)

    cpf = str(cpf1) + "." + str(cpf2) + "." + str(cpf3) + "-" + str(cpf4)
    return cpf

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
    cpf.append(random_cpf())
    month.append(random_month())
    day.append(random_day())
    age.append(2019 - int(year[k]))
    tel1.append(random_tel1())
    tel2.append(random_tel2())
    city.append(random_city())

window = Tk()
 
window.title("Agenda")
 
window.geometry('470x550')
 
lblN = Label(window, text="Nome")
 
lblN.place(x = 1, y = 15)

lblA = Label(window, text="Idade")
 
lblA.place(x = 1, y = 40)

lblC = Label(window, text="Cidade")

lblC.place(x = 1, y = 70)
 
EntradaN = Entry(window,width=10)
 
EntradaN.place(x = 50, y = 15)

EntradaA = Entry(window,width=10)
 
EntradaA.place(x = 50, y = 40)

EntradaC = Entry(window,width=10)

EntradaC.place(x = 50, y = 70)
 
def clickedN():

     Contato.delete('1.0', END)

     Contato.config(state="normal")

     Nome = EntradaN.get()
     
     i = 0
     while(i <= 50):
         
         if person[i] == Nome:
            
            Contato.insert(INSERT, "--------------------")
            Contato.insert(INSERT, "\n ")
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
            Contato.insert(INSERT, "\n")
         i += 1                   

    #Contato.insert(INSERT, )

def clickedA():

     Contato.delete('1.0', END)

     Contato.config(state="normal")

     AgeB = int(EntradaA.get())
     
     j = 0
     while(j <= 50):
         
         if age[j] == AgeB:
            Contato.insert(INSERT, "--------------------")
            Contato.insert(INSERT, "\n ")
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

def clickedC():

     Contato.delete('1.0', END)

     Contato.config(state="normal")

     Cidade = EntradaC.get()
     
     j = 0
     while(j <= 50):
         
         if Cidade == city[j]:
            Contato.insert(INSERT, "--------------------")
            Contato.insert(INSERT, "\n ")
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

def clickedG():

    Contato.delete('1.0', END)

    Contato.config(state="normal")

     
    j = 0
    while(j <= 50):

        Contato.insert(INSERT, "--------------------") 
        Contato.insert(INSERT, "\n ")      
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

btnGeral = Button(window, text="Listar Todos Contatos", command=clickedG)

btnCity = Button(window, text="Buscar", command=clickedC)

btnAge.place(x = 140, y = 40)
 
btnNome.place(x = 140, y = 10)

btnGeral.place(x = 26, y = 430)

btnCity.place(x = 140, y = 70)

Contato = Text(window, width = 30, height = 30)

Contato.place(x = 220, y = 0)

Contato.config(state="disabled")
 
window.mainloop()


from datetime import datetime
from collections import Counter

clients ={
'Смирнова':['Окрашивание', '1000',  '23.04.2020'],
'Казанцева':['Стрижка', '500','22.03.2020'],
'Волкова':['Депеляция',  '1500','2.03.2020'],
'Павлова':['Депеляция',  '1500','23.03.2020']}

#Добавление клиента

print(clients)
new_clients = (input("Введите фамилию? "))
slovar=[(input("Услуга? ")),(input("Стоимость услуги? ")),(input("Дата? "))]
upgrade={new_clients:slovar}
clients.update(upgrade)
print(clients)
 
def del_client():
   
#Удаление клиента

 print(clients)
Name = input("Фамилия? ")
clients.pop(Name)
print(clients)
print('\n') 
def add_element():
    
#Добавление элемента
    
 print(clients) 
Name = input("Фамилия? ")
Service = input("Услуга? ")
Price = input("Стоимость? ")
Date= input("Дата? ")
clients[Name].append({'Услуга': Service, 'Стоимость': Price, 'Дата': Date})
print(clients)
    
def sum_price():
    
#Найти Сумму потраченных денег

 print(clients)
Name = input("Фамилия? ")
sum=0
for i in range(len(d[Name])):
 sum=sum+d[Name][i]['Стоимость']
print(sum)

def client_find():

#Найти самого частого клиента
 
 print(clients)
Name = ["Павлова", "Волкова"]
number = 0
for i in range(len(d)): 
    if len(d[Name[i]]) > number:
            number = len(d[Name[i]])
            Name_Find = Name[i]
    print(Name_Find)

def client_rich():
    Name = ["Павлова", "Волкова"]
    n=0
    sum=0
    for i in range(len(d)):
        for j in range(len(d[Name[i]])):
            sum=sum+d[Name[i]][j]['Стоимость']
        if sum>n:
            n=sum
            rich=Name[i]
    print(rich)
            

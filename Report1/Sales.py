import random
import time
from datetime import timedelta
import datetime

Item = ['Espresso','Americano','Latte','Cappuccino','Mocha','Macchiato','Dolce latte', 'Cold brew', 'Green tea','Milk']
Price = ['3600','4100','4600','4700','5100','5200','5600','5800','4200','4000']
Cashier = ['Lee','SU','MIN']
Payment = ['card','cash']

Sales = []
print('Bill num Cashier items\tQuant\tUnit Price\tTotal Price\tPayment\tDate')
#print('Cashier: %s'%choiceCashier)

print('------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------')
#D = time.strftime('%Y-%m-%d-%X', time.localtime(time.time()))
D = datetime.datetime.now()   
D = D.replace(second=0, microsecond=0)
for i in range(100):
    Q = random.randint(1,3)
    J = random.randint(0,9)
    D+=datetime.timedelta(hours=1)
    Total = Q*int(Price[J])
    choiceCashier = random.choice(Cashier)
    choicePayment = random.choice(Payment)
    Salesline = f'{i+1},{choiceCashier}, {Item[J]}, {Q}, {Price[J]},{Total},{choicePayment},{D}.\n'
    Sales.append(Salesline)
       
for i in Sales:
     print(i)
f = open('C:/Users/csos/Desktop/2021-1/과제/오픈소스활용/Sales_이수민.csv','w')
f.write('Bill num,Cashier,items,Quant,Unit Price,Total Price,Payment,Date\n')
f.writelines(Sales)
f.close()

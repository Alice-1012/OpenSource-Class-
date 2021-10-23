f = open('C:/Users/csos/Desktop/2021-1/과제/오픈소스활용/Sales_이수민.csv','r')
lines = f.readlines()
cashier_1_total = 0
cashier_2_total = 0
cashier_3_total = 0
item_total=[0]*10
payment_total=[0]*2
date_total =[0]*5

for line in lines:
    if 'Lee' in line:
        cashier_1_total += int(line.split(',')[5])
    elif 'SU' in line:
        cashier_2_total += int(line.split(',')[5])
    elif 'MIN' in line:
        cashier_3_total += int(line.split(',')[5])
        
    for i in range(10):
        if Item[i] in line:
            item_total[i]+=int(line.split(',')[5])
    for i in range(2):
        if Payment[i] in line:
            payment_total[i]+=int(line.split(',')[5]) 
        
    for i in range(5):
        if date_list[i] in line.split(',')[7]:
            date_total[i]+=int(line.split(',')[5])
            if date_list[i] == '27':
                print(line)
    
print(cashier_1_total)
print(cashier_2_total)
print(cashier_3_total)
print(item_total)


f.close()


f = open('C:/Users/csos/Desktop/2021-1/과제/오픈소스활용/Salesreport_이수민.csv','w')
f.write('항목별, 금액\n')
f.write(f'Cashier : {Cashier[0]}, {cashier_1_total}\n')
f.write(f'Cashier : {Cashier[1]}, {cashier_2_total}\n')
f.write(f'Cashier : {Cashier[2]}, {cashier_3_total}\n')

for i in range(10):
    f.write(f'Item : {Item[i]},{item_total[i]},\n')
    
for i in range(2):
    f.write(f'Payment : {Payment[i]},{payment_total[i]},\n')
    
for i in range(5):
    f.write(f'Date : {date_list[i]}일,{date_total[i]},\n')
    



f.close()

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

//
Bill num Cashier items	Quant	Unit Price	Total Price	Payment	Date
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
1,MIN, Cold brew, 1, 5800,5800,cash,2021-10-23 16:05:00.

2,MIN, Espresso, 3, 3600,10800,card,2021-10-23 17:05:00.

3,SU, Milk, 2, 4000,8000,card,2021-10-23 18:05:00.

4,SU, Cappuccino, 1, 4700,4700,card,2021-10-23 19:05:00.

5,MIN, Dolce latte, 2, 5600,11200,cash,2021-10-23 20:05:00.

6,SU, Latte, 1, 4600,4600,cash,2021-10-23 21:05:00.

7,MIN, Dolce latte, 3, 5600,16800,cash,2021-10-23 22:05:00.

8,MIN, Cold brew, 2, 5800,11600,cash,2021-10-23 23:05:00.

9,Lee, Cappuccino, 3, 4700,14100,card,2021-10-24 00:05:00.

10,MIN, Milk, 2, 4000,8000,cash,2021-10-24 01:05:00.

11,MIN, Mocha, 1, 5100,5100,card,2021-10-24 02:05:00.

12,SU, Dolce latte, 1, 5600,5600,card,2021-10-24 03:05:00.

13,MIN, Espresso, 2, 3600,7200,card,2021-10-24 04:05:00.

14,MIN, Dolce latte, 2, 5600,11200,card,2021-10-24 05:05:00.

15,Lee, Espresso, 1, 3600,3600,card,2021-10-24 06:05:00.

16,Lee, Americano, 1, 4100,4100,card,2021-10-24 07:05:00.

17,SU, Latte, 3, 4600,13800,card,2021-10-24 08:05:00.

18,Lee, Latte, 3, 4600,13800,cash,2021-10-24 09:05:00.

19,MIN, Cold brew, 1, 5800,5800,cash,2021-10-24 10:05:00.

20,MIN, Americano, 3, 4100,12300,card,2021-10-24 11:05:00.

21,MIN, Cappuccino, 3, 4700,14100,card,2021-10-24 12:05:00.

22,Lee, Mocha, 3, 5100,15300,card,2021-10-24 13:05:00.

23,SU, Milk, 2, 4000,8000,card,2021-10-24 14:05:00.

24,SU, Dolce latte, 2, 5600,11200,cash,2021-10-24 15:05:00.

25,SU, Latte, 2, 4600,9200,cash,2021-10-24 16:05:00.

26,Lee, Green tea, 3, 4200,12600,card,2021-10-24 17:05:00.

27,MIN, Milk, 3, 4000,12000,card,2021-10-24 18:05:00.

28,MIN, Espresso, 3, 3600,10800,card,2021-10-24 19:05:00.

29,SU, Macchiato, 2, 5200,10400,cash,2021-10-24 20:05:00.

30,MIN, Milk, 2, 4000,8000,cash,2021-10-24 21:05:00.

31,MIN, Mocha, 3, 5100,15300,cash,2021-10-24 22:05:00.

32,Lee, Dolce latte, 2, 5600,11200,cash,2021-10-24 23:05:00.

33,Lee, Green tea, 2, 4200,8400,cash,2021-10-25 00:05:00.

34,MIN, Americano, 1, 4100,4100,card,2021-10-25 01:05:00.

35,SU, Mocha, 2, 5100,10200,card,2021-10-25 02:05:00.

36,MIN, Americano, 2, 4100,8200,card,2021-10-25 03:05:00.

37,SU, Macchiato, 1, 5200,5200,card,2021-10-25 04:05:00.

38,SU, Cappuccino, 3, 4700,14100,card,2021-10-25 05:05:00.

39,Lee, Cold brew, 3, 5800,17400,cash,2021-10-25 06:05:00.

40,MIN, Dolce latte, 1, 5600,5600,card,2021-10-25 07:05:00.

41,Lee, Dolce latte, 1, 5600,5600,cash,2021-10-25 08:05:00.

42,SU, Americano, 3, 4100,12300,card,2021-10-25 09:05:00.

43,Lee, Cold brew, 2, 5800,11600,cash,2021-10-25 10:05:00.

44,Lee, Macchiato, 3, 5200,15600,card,2021-10-25 11:05:00.

45,MIN, Macchiato, 1, 5200,5200,card,2021-10-25 12:05:00.

46,MIN, Green tea, 2, 4200,8400,card,2021-10-25 13:05:00.

47,MIN, Cappuccino, 1, 4700,4700,card,2021-10-25 14:05:00.

48,SU, Dolce latte, 1, 5600,5600,cash,2021-10-25 15:05:00.

49,SU, Cappuccino, 2, 4700,9400,cash,2021-10-25 16:05:00.

50,MIN, Cappuccino, 2, 4700,9400,cash,2021-10-25 17:05:00.

51,MIN, Americano, 2, 4100,8200,card,2021-10-25 18:05:00.

52,Lee, Latte, 3, 4600,13800,cash,2021-10-25 19:05:00.

53,SU, Cold brew, 2, 5800,11600,cash,2021-10-25 20:05:00.

54,MIN, Americano, 2, 4100,8200,card,2021-10-25 21:05:00.

55,Lee, Mocha, 2, 5100,10200,cash,2021-10-25 22:05:00.

56,Lee, Espresso, 3, 3600,10800,cash,2021-10-25 23:05:00.

57,SU, Macchiato, 1, 5200,5200,cash,2021-10-26 00:05:00.

58,Lee, Espresso, 3, 3600,10800,cash,2021-10-26 01:05:00.

59,Lee, Cappuccino, 2, 4700,9400,card,2021-10-26 02:05:00.

60,SU, Green tea, 1, 4200,4200,card,2021-10-26 03:05:00.

61,SU, Milk, 1, 4000,4000,cash,2021-10-26 04:05:00.

62,MIN, Espresso, 2, 3600,7200,card,2021-10-26 05:05:00.

63,SU, Milk, 2, 4000,8000,cash,2021-10-26 06:05:00.

64,MIN, Milk, 2, 4000,8000,cash,2021-10-26 07:05:00.

65,MIN, Milk, 2, 4000,8000,card,2021-10-26 08:05:00.

66,MIN, Cold brew, 1, 5800,5800,cash,2021-10-26 09:05:00.

67,SU, Green tea, 2, 4200,8400,cash,2021-10-26 10:05:00.

68,SU, Espresso, 2, 3600,7200,card,2021-10-26 11:05:00.

69,Lee, Mocha, 1, 5100,5100,card,2021-10-26 12:05:00.

70,Lee, Mocha, 1, 5100,5100,cash,2021-10-26 13:05:00.

71,SU, Dolce latte, 2, 5600,11200,card,2021-10-26 14:05:00.

72,MIN, Cold brew, 1, 5800,5800,cash,2021-10-26 15:05:00.

73,Lee, Green tea, 3, 4200,12600,card,2021-10-26 16:05:00.

74,Lee, Green tea, 2, 4200,8400,cash,2021-10-26 17:05:00.

75,Lee, Macchiato, 1, 5200,5200,card,2021-10-26 18:05:00.

76,Lee, Latte, 2, 4600,9200,cash,2021-10-26 19:05:00.

77,MIN, Latte, 2, 4600,9200,card,2021-10-26 20:05:00.

78,SU, Americano, 1, 4100,4100,cash,2021-10-26 21:05:00.

79,MIN, Americano, 3, 4100,12300,card,2021-10-26 22:05:00.

80,SU, Milk, 2, 4000,8000,card,2021-10-26 23:05:00.

81,Lee, Macchiato, 3, 5200,15600,card,2021-10-27 00:05:00.

82,SU, Cold brew, 3, 5800,17400,cash,2021-10-27 01:05:00.

83,MIN, Macchiato, 2, 5200,10400,cash,2021-10-27 02:05:00.

84,Lee, Green tea, 2, 4200,8400,card,2021-10-27 03:05:00.

85,MIN, Cappuccino, 3, 4700,14100,card,2021-10-27 04:05:00.

86,SU, Espresso, 1, 3600,3600,card,2021-10-27 05:05:00.

87,Lee, Cold brew, 1, 5800,5800,card,2021-10-27 06:05:00.

88,Lee, Milk, 3, 4000,12000,cash,2021-10-27 07:05:00.

89,SU, Mocha, 3, 5100,15300,card,2021-10-27 08:05:00.

90,SU, Espresso, 1, 3600,3600,cash,2021-10-27 09:05:00.

91,SU, Latte, 3, 4600,13800,cash,2021-10-27 10:05:00.

92,MIN, Milk, 2, 4000,8000,cash,2021-10-27 11:05:00.

93,MIN, Cold brew, 3, 5800,17400,cash,2021-10-27 12:05:00.

94,Lee, Milk, 1, 4000,4000,card,2021-10-27 13:05:00.

95,SU, Mocha, 1, 5100,5100,cash,2021-10-27 14:05:00.

96,Lee, Milk, 1, 4000,4000,cash,2021-10-27 15:05:00.

97,Lee, Latte, 3, 4600,13800,cash,2021-10-27 16:05:00.

98,Lee, Cappuccino, 2, 4700,9400,cash,2021-10-27 17:05:00.

99,MIN, Americano, 1, 4100,4100,card,2021-10-27 18:05:00.

100,Lee, Mocha, 1, 5100,5100,cash,2021-10-27 19:05:00.

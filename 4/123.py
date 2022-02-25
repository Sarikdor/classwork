year = int(input())
if year % 400 == 0:
    print('високосный') 
elif year % 4 == 0:
    if year % 100 != 0:
        print('високосный') 
    else:
        print('невисокосный') 
else: 
    print('невисокосный')
       
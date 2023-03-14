primo = int(input('Ingrese la cantidad de primos que desea: '))
n = 2; j = 2; x=0
print('1')
while x <= primo-2:
     div = n % j
     if div==0:
         if n == j:
             print(n, end=',')
             x += 1
         j=2
         n += 1
     

     else:
       j += 1
   

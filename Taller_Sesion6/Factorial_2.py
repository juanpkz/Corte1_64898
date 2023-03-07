
def factorial(x):
    num=1
    for i in range(1,x+1):
        num*=i

    return num 

n=int(input('Ingrese el numero de elementos: '))
m=int(input('Ingrese el numero de muestras sin orden: '))

b=n-m

C=factorial(n)/(factorial(m)*factorial(b)) 

print('El numero de combinaciones que se pueden dar es: ',int(C))
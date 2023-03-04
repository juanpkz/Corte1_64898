print('Escoja una de las siguiente opciones:\n')
print('1. numero entero positivo ')
print('2. numero factorial')
print('3. numero primo')


opc = int(input('Escoja una opcion: '))

if opc == 1:
    numero = int(input("Ingrese un número entero positivo: "))
    impares=[]
    for i in range(1, numero+1, 2):

        impares.append(str(i))
    print(",".join(impares))


elif opc == 2:
    from math import factorial as fac
    factorial= int(input("Ingrese el numero: ")) 
    a=fac(factorial)
    print(a)

elif opc == 3:
     num = int(input("Ingrese un número: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "no es un número primo")
            break
    else:
        print(num, "es un número primo")
        
print("Números primos hasta", num, ":")
for i in range(2, num + 1):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print(i, end=' ')
      
     
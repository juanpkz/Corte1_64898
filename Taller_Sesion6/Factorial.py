
n=int(input("Ingrese un numero de elementos: "))
r=int(input("Ingrese el numero de muestras sin orden: "))
b=n-r
fact=1
fact2=1
fact3=1
for i in range(1, n + 1):
        fact *= i
for j in range(1, r + 1):
      fact2 *= j
for f in range(1,b +1):
     fact3 *= f
C=fact/(fact2*(fact3))
print("el numero de combinaciones binomiales que pueden darse es de,",int(C))



    

 


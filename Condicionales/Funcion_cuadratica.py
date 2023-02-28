from math import sqrt as raizc

a=eval(input('ingrese el valor de a : '))
b=eval(input('ingrese el valor de b : '))
c=eval(input('ingrese el valor de c : '))
if((b**2)-4*a*c)<0:
    print('La solucion es imaginaria')
else: 
    x1 = (-b +raizc((b**2)-4*a*c))/(2*a)
    x2 = (-b -raizc((b**2)-4*a*c))/(2*a)
    print('El primer resultado es : ', x1)
    print('El segundo resultado es : ', x2)



def Area (r):
    pi = 3.1416
    A = pi*(r**2)
    return A

def Volumen(h,A):
    # A = Area(r)
    V = A*h
    return V

r=eval(input('Ingrese el radio: '))
h=eval(input('Ingrese la altura: '))

A = Area(r)
V = Volumen(h,A)

print (f'El area es {A} y el volumen es {V}')
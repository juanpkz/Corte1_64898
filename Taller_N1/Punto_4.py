print('Costo anual del consumo de combustible')
a=eval(input('Ingrese la distancia recorrida en km : '))
b=eval(input('Ingrese el consumo de combustible anual en litros por cada 100km : '))
c=eval(input('Ingrese el costo del combustible por litro : '))
d=(a*b)/100
f=d*c
print('El costo anual del consumo de combistible es : ',round(f,1),'$')
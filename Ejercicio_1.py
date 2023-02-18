print('Determinar el tipo de triangulo segun la longitud de sus lados ')
a=eval(input('Ingrese la longitud del primer lado : '))
b=eval(input('Ingrese la longitud del segundo lado : '))
c=eval(input('Ingrese la longitud del tercer lado : '))
if a==b==c:
    print('Su triangulo es Equilatero')
elif a==b or b==c or a==c:
    print('Su triangulo es Isósceles')
else:
    print('Su triangulo es Escaleno')

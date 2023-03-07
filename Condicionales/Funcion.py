
def suma (a,b):
    resultado = a + b
    return resultado

def imprimir(nombre):
    print(nombre,',Su resultado es: ')

n = 'si'
nombre = input('Ingrese su nombre: ')
while n == 'si':
    
    a =int(input('Ingrese un numero: '))
    b =int(input('Ingrese un numero: '))
    res = suma(a,b)
    imprimir(nombre)
    print(res)
    n = input('¿quiere sumar otro numero? (si/no) ')

from Primer_punto import Separar as s
from Segundo_punto import Primos as P

print('Escoja una de las siguiente opciones:\n')
print('1. numero  ')
print('2. numero primo')

opc = int(input('Escoja una opcion: '))

if opc == 1:
 def main():

    n=int(input('Ingrese un numero: '))
    if n < 1000:
     print("No es un nuemero aceptado: ")
    elif n > 1000000000:
        print("No es un nuemero aceptado: ")
    else:
       res=s(n)

    if __name__=="__main__":
        main() 

elif opc==2:
  def main():
    p=input('Ingrese la cantidad de numero primos que desea')
    result=P(p)
    print(result)

    if __name__=="__main__":
        main() 
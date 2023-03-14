n = int(input('Ingrese un numero: '))
digit_equal_five = 0
digit_different_five =0
if n < 10:
    print('No es valido')
elif n > 99999999:
    print('No es valido')
    while n != 0:
         x=(n//10)
         y=x*10
         dig=n-y
         n=x
         if dig == 5:
          digit_equal_five += 1
         print("salto")
    else:
          print(dig)
          digit_different_five += 1
    print(f'Iguales a 5: {digit_equal_five}') 
    print(f'diferente a 5: {digit_different_five}') 
    print(f'nuemor de digitos: {digit_equal_five+digit_different_five}') 
       
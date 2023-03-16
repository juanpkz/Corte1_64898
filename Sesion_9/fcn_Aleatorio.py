import random as r


for i in range(5):
  numero = r.randint(10,20)#numero aleatorio entre esos dos parametros 

  real = round(r.uniform(10,20),2)# solicita un numero flotante aleatoriamente entre el valor de inicio y final 
  
  letra = r.choice("murcielago")#solicita datos tipo str de una cadena establecida aleatoriamente 

  print(numero, end="   ")
  print(real, end="   ")
  print(letra, '\n')

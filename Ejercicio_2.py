suma = 0 
notas = eval(input("¿Cuántas notas desea introducir? "))
for x in range(notas):
    suma += eval(input("Introduzca la nota: ") )
    prom=suma/notas
print("Se han introducido", notas, "notas que en total han sumado", 
        suma, "el promedio del estudiante es", prom)
if prom >= 3:
  print('El estudiante aprueba la materia')
else:
  print('El estudiante pierde la materia ')
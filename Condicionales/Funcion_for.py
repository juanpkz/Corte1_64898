print('Escoja una de las siguiente opciones:\n')
print('1. for in range(final)')
print('2. for in range(inicio, final)')
print('3. for in range(inicio, final, paso)')


opc = int(input('Escoja una opcion: '))

if opc == 1:
    for i in range(10):
       print(i+1)
    print('Fin del proceso')

elif opc == 2:
    for i in range(5,10):
        print(i)
    print('Fin del proceso')

elif opc == 3:
    for i in range(10,1,-2):
        print(i)
    print('Fin del proceso')

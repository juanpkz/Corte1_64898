print('Calculo del IVA')
a=eval(input('Ingrese el valor del producto : '))
bruto=a/1.19
IVA=bruto*0.19
print('El valor del IVA es : ',round(IVA,2))
print('El valor bruto es : ',round(bruto,2))
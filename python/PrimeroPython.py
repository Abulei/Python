salario = int(input('salario?'))
imposto = float(input('Imposto em %(ex: 27.5)?'))
if not imposto :
    imposto = 27.5
else:
    imposto = float(imposto)

print("valor real:{0}".format(salario - (salario * (imposto * 0.01))))
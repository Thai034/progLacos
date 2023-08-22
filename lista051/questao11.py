'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de b elevado a e. (Sem usar Math.pow();)
'''

b = float(input("Informe a base da potência: "))
e = float(input("Informe o expoente da potência: "))


#usuário -> b = 3, e = 4
#no papel você faria 3 * 3 * 3 * 3

cont = 1
acumulador = 1 #0 para somas e 1 para divisão e multplicação
while (cont <= e):
    acumulador = acumulador * b
    cont = cont + 1

print(f"A {b:.0f} elevado a {e:.0f} = {acumulador:.0f}")

'''
pot = b ** e
print(f"A {b:.0f} elevado a {e:.0f} = {pot:.0f}")
'''
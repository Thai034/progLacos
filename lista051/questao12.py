'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média.
'''

num = float(input("Informe um número: "))
maior = num
menor = num
acumulador = num
media = 1

while (num != -1 ):
    num = float(input("Informe um número: "))

    if (num != -1):
        acumulador = acumulador + num
        media = media + 1

        if (maior < num):
            maior = num

        if(menor > num):
            menor = num

if (maior == -1):
    print("Você inderiu o número -1 na primeira resposta.\n FIM DO PROGRAMA!")

print(f"O maior número é {maior} e o menor número é {menor}")
print(f"A media entre os números é de {acumulador / media:.1f}")
print("FIM DO PROGRAMA!")


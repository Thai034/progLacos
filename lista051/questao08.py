'''
Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo.
'''

'''
primeiro parte - definir um contador que vai mudando de números até o final
segunda parte - while, testada ate o final
terceira parte - precisa somar mais um para o codigo não engasgar
'''

#Isso é a obrigação um da estrutura de repetição
# declarar variável contador no valor inicial da repetição
cont = 0

#regra 2, testar a estrutura (while com var contador) no valor fim da repetição
while (cont <= 20):
    #bloco que será repetido várias vezes
    resto = cont % 2
    if (resto == 1):
        print(cont)


    #regra 3 - incrementar a var contador na última linha dentro do bloco
    cont = cont + 1



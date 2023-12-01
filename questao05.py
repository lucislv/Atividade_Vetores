##### Atividade Vetores
## Questão 05
# Elabore um algoritmo que leia 10 números e escreva primeiro os 
# pares e depois os ímpares.

n = 10 ## declaração da variável "n", recebe 10 elementos.
par = [] ## declaração do vetor que armazenará os números pares.
impar = [] ## declaração do vetor que armazenará os números ímpares.

print("Digite 10 valores") ## função print exibe texto entre aspas ao usuário.

for i in range(0, n):
 ## com a função for, a variável "i" percorre o intervalo de 0 até "n", 
 #  gerado pela função range, e itera os comandos do laço até o final do intervalo.
    valor = int(input(f"\aDigite o {i+1}º valor: "))
    ## comando no laço for, declaração da variável "valor", do tipo int, recebe o número 
    #  digitado pelo usuário através da função input.

    if valor % 2 == 0 :
     ## condicional no laço for, verifica se a variável "valor" possui o resto da 
     #  divisão por 2 igual a 0.
        par.append(valor)
        ## comando na condicional if, vetor "par" armazena a variável "valor", através 
        #  da função append, caso o retorno da verificação seja verdadeiro.

    else:
     ## condicional no laço for, bloco de comando para caso o retorno da verificação na 
     #  condicional anterior seja falso.
        impar.append(valor)
        ## comando na condicional else, vetor ímpar armazena a variável "valor", através 
        #  da função append.

print(f"""Numeros pares: {par}
Numeros impares: {impar}""")
## função print exibe o texto entre aspas triplas ao usuário, em conjunto com a 
#  função f, para formatação e exibição dos números em cada índice dos vetores.

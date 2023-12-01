##### Atividade Vetores
## Questão 03
# Faça um algoritmo que leia um vetor de doze elementos numéricos inteiros, 
# calcule e mostre:
# a) A quantidade de números pares;
# b) Quais os números pares;
# c) A quantidade de números ímpares;
# d) Quais os números ímpares.

n = 12 ## declaração da variável "n", recebe valor 12.
par = [] ## declaração do vetor que armazenará os números pares.
impar = [] ## declaração do vetor que armazenará os números ímpares.

print("\nDigite 12 valores") ## função print exibe texto entre aspas ao usuário.

for i in range(0, n):
 ## com a função for, a variável "i" percorre o intervalo de 0 até "n", 
 #  gerado pela função range, e itera os comandos do laço até o final do intervalo.
    valor = int(input(f"Digite o {i+1}º valor: "))
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


print(f"""\nQuantidade de números pares: {len(par)}
Números pares: {par}

Quantidade de números ímpares: {len(impar)}
Números ímpares: {impar}""") 
## função print exibe o texto entre aspas triplas ao usuário, em conjunto com 
#  as funções f e len, para formatação e exibição dos números de cada índice dos 
#  vetores e a quantidade de números em cada vetor.
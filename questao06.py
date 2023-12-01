##### Atividade Vetores
## Questão 06
# Crie um algoritmo que leia um número de elementos informado pelo usuário e 
# armazene em um vetor e mostre o vetor e logo após o vetor de forma invertida, 
# o primeiro elemento deve ser o último e assim por diante.

n = int(input("Quantos valores serão digitados? (Informe até 20): "))
## declaração da variável "n", do tipo int, recebe o valor digitado pelo usuário 
#  através da função input.

vetor = [] ## declaração do vetor que armazenará os números.

for i in range(0, n):
## com o loop for, a variável "i" percorre o intervalo de 0 até "n", gerado pela 
#  função range, e itera os comandos do laço até o final do intervalo.
    valor = float(input(f"\aDigite o {i+1}º valor: "))
    ## comando no laço for, declaração da variável "valor", do tipo float, exibe um
    #  texto ao usuário e recebe o valor digitado através da função input.
    vetor.append(valor)
    ## comando no laço for, vetor armazena a variável "valor" através da função append.

print(f"\aNúmeros digitados: {vetor}")
## função print exibe texto entre aspas ao usuário em conjunto com a função f, 
#  para formatação e exibição dos valores do vetor.

vetor.reverse()
## função reverse organiza os valores no vetor em ordem reversa.

print(f"\aNúmeros digitados em ordem reversa: {vetor}")
## função print exibe texto entre aspas ao usuário em conjunto com a função f, 
#  para formatação e exibição dos valores do vetor.
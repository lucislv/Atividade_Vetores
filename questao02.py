##### Atividade Vetores
## Questão 02
# Escreva um algoritmo que receba dez números do usuário e armazene em um vetor 
# a metade de cada número. Após isso, o algoritmo deve imprimir todos os valores 
# armazenados.

n = 10 ## declaração da variável "n", recebe valor 10.
vetor = [] ## declaração do vetor que armazenará os números.
print("Digite 10 valores") ## função print exibe texto entre aspas ao usuário.

for i in range(0, n): 
 ## com a função for, a variável "i" percorre o intervalo de 0 até "n", gerado 
 #  pela função range, e itera os comandos do laço até o final do intervalo.
    valor = float(input(f"Digite o {i+1}º valor: "))
    ## comando no laço for, variável "valor", do tipo float, recebe o número digitado 
    #  pelo usuário através da função input.
    vetor.append(valor/2) 
    ## comando no laço for, vetor armazena a variável "valor" dividida por 2, através da função 
    #  append, tendo assim a metade do valor.

print(vetor) ## função print exibe os valores do vetor ao usuário.








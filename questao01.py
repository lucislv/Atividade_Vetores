##### Atividade Vetores
## Questão 01
# Faça um algoritmo que carregue um vetor com 15 posições, calcule e mostre:
# a) O maior elemento do vetor e em que posição esse elemento se encontra;
# b) O menor elemento do vetor e em que posição esse elemento se encontra.


n = int(input("Quantos valores serão digitados? (Informe até 15 ou digite 0 para encerrar): "))
## declaração da variável "n", do tipo int, recebe o valor digitado pelo usuário 
#  através da função input.

while n > 15:
## função de loop while, verifica se o valor da variável "n" é maior que 15 e 
#  executa os comandos que estão no laço até que o retorno da verificação 
#  seja falso.
    n = int(input("Valor informado inválido. Digite novamente (Informe até 15 ou digite 0 para encerrar): "))
    ## comando no laço while: variável "n", do tipo int, recebe o novo valor digitado 
    #  pelo usuário através da função input.
    if n == 0:
    ## condicional no laço while, verifica se a variável "n" possui valor igual a 0
        break
        ## comando na condicional if, função break interrompe o loop while caso o retorno 
        #  da verificação seja verdadeiro.

if n > 0 or n <= 15:
## condicional verifica se a variável "n" possui valor maior que 0 ou menor/igual a 15
#  e executa os comandos do laço caso o retorno da verificação seja verdadeiro.
    vetor = [] 
    ## declaração do vetor que armazenará os valores.

    for i in range(0, n):
    ## com a função for, a variável "i" percorre o intervalo de 0 até "n", gerado pela 
    #  função range, e itera os comandos do laço até o final do intervalo.
        valor = int(input(f"Digite o valor da posição {i+1}: "))
        ## comando no laço for, declaração da variável "valor", do tipo int, exibe um
        #  texto ao usuário e recebe o valor digitado através da função input.
        vetor.append(valor)
        ## comando no laço for, vetor armazena a variável "valor" através da função append.

    maior = vetor[0] 
    ## declaração da variável "maior", recebe o valor que está no índice 0 do vetor.
    menor = vetor[0]
    ## declaração da variável "menor", recebe o valor que está no índice 0 do vetor.
    posicaomaior = posicaomenor = 0
    ## declaração da variável "posicamaior", recebe a variável "posicaomenor", que 
    # recebe o valor 0.

    for i in range(1, len(vetor)):
    ## com a função for, a variável "i" percorre o intervalo, gerado pela função range, 
    #  de 1 até a extensão total do vetor, dado pela função len, e itera os comandos no 
    #  laço até o final do intervalo.

        if vetor[i] > maior:
        ## condicional no laço for, verifica se o valor do vetor, no índice em que a variável 
        #  "i" fez a iteração, é maior que o valor da variável "maior".
            maior = vetor[i]
            ## comando na condicional if, variável "maior" recebe o valor do vetor, no índice em 
            #  que variável "i" fez a iteração, caso o retorno da verificação seja verdadeiro.
            posicaomaior = i
            ## comando na condicional if, variável "posicaomaior" recebe a variável "i", que possui
            #  o índice do vetor, caso o retorno da verificação seja verdadeiro.

        elif vetor[i] < menor:
        ## condicional no laço for, verifica se o valor do vetor, no índice em que a variável 
        #  "i" fez a iteração, é menor que o valor da variável "menor".
            menor = vetor[i]
            ## comando na condicional if, variável "menor" recebe o valor do vetor, no índice em que 
            #  variável "i" fez a iteração, caso o retorno da verificação seja verdadeiro.
            posicaomenor = i
            ## comando na condicional if, variável "posicaomenor" recebe a variável "i", que que possui
            #  o índice do vetor, caso o retorno da verificação seja verdadeiro.
      
    print(f"""Maior elemento: {maior}; Posição: {posicaomaior+1}
Menor elemento: {menor}; Posição: {posicaomenor+1}""")
    ## função print exibe o texto entre aspas ao usuário, em conjunto com as funções f e len, para
    #  formatação e exibição dos valores nas variáveis "maior", "posicaomaior", "menor" e "posicaomenor".


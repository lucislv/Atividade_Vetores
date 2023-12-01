##### Atividade Vetores
## Questão 04
# Dado um vetor qualquer com 20 números reais, informe se há ou não números 
# repetidos nesse vetor.

vetor = [] ## declaração do vetor que armazenará os números.
num_repetido = [] ## declaração do vetor que armazenará os números repetidos.

n = int(input("Quantos valores serão digitados? (Informe até 20 ou digite 0\ para sair): "))
## declaração da variável "n", do tipo int, recebe o valor digitado pelo usuário 
#  através da função input.

while n > 20:
## função de loop while, verifica se o valor da variável "n" é maior que 20 e 
# executa os comandos que estão no laço até que o retorno da verificação 
# seja falsa.
    
    n = int(input("Valor inválido. Digite novamente (Informe até 20 ou digite 0 para sair): "))
    ## comando no laço while, variável "n", do tipo int, recebe o novo valor digitado 
    #  pelo usuário através da função input.
    
    if n == 0:
    ## condicional no laço while, verifica se a variável "n" possui valor igual a 0
        break
        ## comando na condicional if, função break interrompe o loop while caso o retorno 
        #  da verificação seja verdadeiro.

if n > 0 or n <= 20:
## condicional verifica se a variável "n" possui valor maior que 0 ou menor/igual a 15.
#  e executa os comandos do laço caso o retorno da verificação seja verdadeiro.
    for i in range(0, n):
     ## com o loop for, a variável "i" percorre o intervalo de 0 até "n", gerado pela 
     #  função range, e itera os comandos no laço até o final do intervalo.
        valor = float(input(f"\nDigite o {i+1}º valor: "))
        ## comando no laço for, declaração da variável "valor", do tipo float, exibe um
        #  texto ao usuário e recebe o valor digitado através da função input.
        vetor.append(valor)
        ## comando no laço for, vetor armazena a variável "valor" através da função append.

    vetor.sort()
    ## função sort organiza os valores no vetor em ordem crescente.

    for i in range(0, len(vetor)):
     ## com a função for, a variável "i" percorre o intervalo, gerado pela função range, 
     #  de 0 até a extensão total do vetor, dado pela função len, e itera os comandos do 
     #  laço até o final do intervalo.
        aux = vetor[i-1]
        ## comando no laço for, declaração da variável "aux", recebe o valor do vetor que 
        #  está no índice anterior à iteração atual da variável "i". 
    
        if vetor[i] == aux:
         ## condicional no laço for, verifica se o valor do vetor, no índice em que a variável 
         #  "i" fez a iteração, é igual ao valor da variável "aux".
            num_repetido.append(vetor[i])
            ## comando na condicional if, vetor "num_repetido" armazena o valor do vetor "vetor", 
            #  no índice em que a variável "i" fez a iteração, caso o retorno da verificação seja 
            #  verdadeiro.

    if len(num_repetido) > 0:
     ## condicional if verifica se a extensão do vetor "num_repetido", dada pela função len, 
     #  é maior que 0. 
        print("\nHá repetições.")
        print(f"Números repetidos: {num_repetido}")
        ## função print exibe texto entre aspas ao usuário, em conjunto com a função f, para 
        #  formatação e exibição dos valores do vetor, caso o retorno da verificação seja
        #  verdadeiro.

    else:
        print("\nNão há repetições.")
     ## condicional no laço for, bloco de comando caso o retorno da verificação na condicional 
     #  anterior seja falso.
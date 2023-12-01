### Atividade Vetores
## Questão 07
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um 
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos 
# elementos intercalados dos dois outros vetores

n = 20
vetor1 = []
vetor2 = []
vetor3 = []

print("Digite 20 elementos")

for i in range(0, n):
    elemento = input(f"Digite o {i+1}º elemento: ")
    if len(vetor1) < 10:
        vetor1.append(elemento)
    else:
        vetor2.append(elemento)
    
for v1, v2 in zip(vetor1, vetor2):
    vetor3.append(v1)
    vetor3.append(v2)

print(vetor3)



    


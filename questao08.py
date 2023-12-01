### Atividade Vetores
## Questão 08
# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
n = 30
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

print("Digite 30 elementos")

for i in range(0, n):
    elemento = input(f"Digite o {i+1}º elemento: ")
    
    if len(vetor1) < 10:
        vetor1.append(elemento)
    elif len(vetor1) == 10 and len(vetor2) < 10:
        vetor2.append(elemento)
    else:
        vetor3.append(elemento)
    
for v1, v2, v3 in zip(vetor1, vetor2, vetor3):
    vetor4.append(v1)
    vetor4.append(v2)
    vetor4.append(v3)

print(vetor4)
### Atividade Vetores
##  Questão 09
# Faça um programa que receba a temperatura média de cada mês do ano e
# armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e 
# mostre todas as temperaturas acima da média anual, e em que mês elas 
# ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
"Julho", "Agosto","Setembro", "Outubro", "Novembro", "Dezembro"]
total_temp = 0

for mes in meses:
    temp_mes = int(input(f"Informe a temperatura média do mês de {mes}: "))
    temperaturas.append(temp_mes)
    total_temp += temp_mes

media_anual_temp = total_temp / 12

# print(meses)
# print(temperaturas)
# print(total_temp)
# print(media_anual_temp)

print(f"\nMédia anual das temperaturas: {media_anual_temp:.2f}°C")
print("")
for t, m in zip(temperaturas, meses):
    if t > media_anual_temp:
        print(f"Temperatura acima da média anual: {t}°C  Mês: {m}")




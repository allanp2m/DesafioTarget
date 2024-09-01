import json


#Questão 3

def faturamento(n):
    h = []
    for dia in n:
        if dia["valor"] > 0:
            h.append(dia["valor"])

    #Faturamento min e max
    faturamento_min = min(h)
    faturamento_max = max(h)

    #Média do faturamento
    media = sum(h) / len(h)

    #Dias a cima da média
    i = 0
    for valor in h:
        if valor > media:
            i += 1

    return faturamento_min, faturamento_max, i, media

with open('faturamento_mensal.json', 'r') as file:
    n = json.load(file)

faturamento_min, faturamento_max, i, media = faturamento(n)
print(f"Média do faturamento: {media}")
print(f"O menor valor de faturamento ocorrido em um dia do mês: {faturamento_min}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: {faturamento_max}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {i}")
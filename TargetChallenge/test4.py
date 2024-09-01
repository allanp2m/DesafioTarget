import json

#Questão 4

def faturamento_distribuidora(n):
    total_faturamento = sum(n.values())

    calculo_percentual = {estado: (valor / total_faturamento) * 100 for estado, valor in n.items()}

    return calculo_percentual

with open('faturamento.json', 'r') as file:
    n = json.load(file)

calculo_percentual = faturamento_distribuidora(n)

for estado, percentual in calculo_percentual.items():
    print(f"{estado}: {percentual:.2f}%")
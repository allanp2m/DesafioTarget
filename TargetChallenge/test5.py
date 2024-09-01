#Questão 5

def inverter_string(n):
    target_inverse = ""

    for i in range(len(target)-1, -1, -1):
        target_inverse += target[i]

    return target_inverse

target = input("Insira uma palavra: ")
target_inverse = inverter_string(target)
print(target_inverse)
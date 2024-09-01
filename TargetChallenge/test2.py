#Questão 2

def fibonacci(n):
    h = 0
    i = 1
    
    while h < n:
        h, i = i, h + i

    if h == n:
        return(print("O número está na sequência de Fibonacci"))
    else: 
        return(print("O número não está na sequência de Fibonacci"))
    
n = int(input("Informe o número desejado: "))
result = fibonacci(n)
print(result)
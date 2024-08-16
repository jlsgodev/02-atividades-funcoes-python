# 15. **Função para Calcular Fibonacci**:
# - Crie uma função chamada `fibonacci` que receba um número `n`
# como argumento e retorne o `n`-ésimo número da sequência de Fibonacci.

def fibonacci(n):           # função fibonacci com um argumento n
    if n <= 0:              # se n for menor ou igual a 0
        return 0
    elif n == 1:            # se n for igual a 1
        return 1
    else:
        return fibonacci(n -  1) + fibonacci(n - 2)     # retorna a soma de fibonacci(n - 1) e fibonacci(n - 2)

print(fibonacci(19))



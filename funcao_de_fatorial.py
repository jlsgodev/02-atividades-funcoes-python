#  6. **Função de Fatorial**:
# - Crie uma função chamada `fatorial` que receba um número 
# como argumento e retorne o fatorial desse número.

def fatorial (num):  # função fatorial com um argumento num 
    fat = 1          # variável fat recebe 1
    for i in range(1, num + 1): # para i no intervalo de 1 até num + 1  
        fat *=i               # fat recebe fat vezes i
    return fat              # retorna fat
print(fatorial (5))       # printa a função fatorial com o argumento 2


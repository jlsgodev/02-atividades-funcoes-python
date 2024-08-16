#  25. **Função para Filtrar Números Pares**:
# - Crie uma função chamada `filtrarPares` que receba um array
#  de números como argumento e retorne um novo array contendo apenas os números pares.

def filtrarPares(array): # função para filtrar números pares
    pares = [ ] # inicializa um array vazio para armazenar os números pares
    for i in array: # percorre todo o array
        if i % 2 == 0:
            pares.append(i) # se o número for par, adiciona ao array pares
    return pares

print(filtrarPares([1, 2, 36, 47, 55, 68, 72, 83, 91, 100])) 
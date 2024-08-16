# 23. **Função para Encontrar o Maior Número em um Array**:
#- Crie uma função chamada `maiorNumero` que receba um array
# de números como argumento e retorne o maior número do array.

def maiorNumero(array):    # Função para encontrar o maior número em um array de números
    maior = array[0]       # Inicializa a variável maior com o primeiro elemento do array
    for i in range(1, len(array)):    # Percorre o array
        if array[i] > maior:          # Se o elemento atual for maior que o maior
            maior = array[i]          # Atualiza o maior
    return maior

print(maiorNumero([111, 22, 3, 444, 55]))
    


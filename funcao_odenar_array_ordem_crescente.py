#   24. **Função para Ordenar um Array em Ordem Crescente**:
#- Crie uma função chamada `ordenarArray` que receba um array
#  de números como argumento e retorne o array ordenado em ordem crescente.

def ordenarArray(array):  # Função para ordenar um array de números em ordem crescente
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array  # O return deve estar fora do loop for

print(ordenarArray([111, 22, 3, 444, 55]))

            
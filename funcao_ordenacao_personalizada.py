#  34. **Função de Ordenação Personalizada**:
# - Crie uma função chamada `ordenarPersonalizado`
#  que receba um array de objetos e uma função de 
# comparação (callback) como argumentos e retorne o array ordenado.

def ordenarPersonalizado(array, callback): 
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if callback(array[i], array[j]):
                array[i], array[j] = array[j], array[i]
    return array

print(ordenarPersonalizado([{'nome': 'João', 'idade': 25}, {'nome': 'Maria', 'idade': 20}, {'nome': 'Pedro', 'idade': 30}], lambda a, b: a['idade'] > b['idade']))
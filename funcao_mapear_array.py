# 33. **Função para Mapear um Array**:
# - Crie uma função chamada `mapearArray`
#  que receba um array e uma função de mapeamento (callback) 
# como argumentos e retorne um novo array com os resultados 
# da função de mapeamento aplicada a cada elemento.

def mapearArray(array, callback): # função para mapear um array
    resultado = [ ] # inicializa um array vazio para armazenar os resultados
    for i in array: # percorre todo o array
        resultado.append(callback(i)) # adiciona o resultado da função de mapeamento ao array de resultados
    return resultado
print(mapearArray([1, 2, 3, 4, 5], lambda a: a * 2))


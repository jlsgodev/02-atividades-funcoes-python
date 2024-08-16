#  30. **Função para Reduzir um Array**:
# - Crie uma função chamada `reduzirArray`
#  que receba um array de números e uma função 
# de redução (callback) como argumentos e retorne o valor reduzido.

def reduzirArray(array, callback): # função para reduzir um array
    resultado = array[0] # inicializa a variável resultado com o primeiro elemento do array
    for i in range(1, len(array)): # percorre o array
        resultado = callback(resultado, array[i]) # chama a função de redução passando o resultado e o elemento atual
    return resultado # retorna o valor reduzido

print(reduzirArray([1, 2, 3, 4, 5], lambda a, b: a + b)) 
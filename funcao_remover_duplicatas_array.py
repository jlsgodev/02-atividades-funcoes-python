# 31. **Função para Remover Duplicatas de um Array**:
# - Crie uma função chamada `removerDuplicatas` que receba
#  um array como argumento e retorne um novo array sem duplicatas.

def removerDuplicatas(array): # função para remover duplicatas de um array
    semDuplicatas = [ ] # inicializa um array vazio para armazenar os elementos sem duplicatas
    for i in array: # percorre todo o array
        if i not in semDuplicatas: # se o elemento não estiver no array semDuplicatas
            semDuplicatas.append(i) # adiciona o elemento ao array semDuplicatas
    return semDuplicatas

print(removerDuplicatas([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10])) 
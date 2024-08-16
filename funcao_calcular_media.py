#  8. **Função para Calcular Média**:
#- Crie uma função chamada `media` que receba um array de 
# números como argumento e retorne a média dos números.


def media(numeros):
    total = 0
    for i in numeros:       # para i em numeros usando for para percorrer a lista    
        total += i          # total recebe total mais i

    if len(numeros) > 0:                 # se o tamanho da lista numeros for maior que 0
        return total  /  len(numeros)     # retorna total dividido pelo tamanho da lista numeros
    else:
        media  = 0                       # senão media recebe 0


print(media([91, 95, 95, 80, 90]))        # printa a função media com a lista


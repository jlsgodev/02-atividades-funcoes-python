# 21. **Função para Contar Vogais**:
# - Crie uma função chamada `contarVogais`
# que receba uma string como argumento e retorne
# o número de vogais na string

def contarVogais( string):
    vogais = "aeiouAEIOU"           # vogais em maiúsculas e minúsculas
    contador = 0
    for letra in string:            # para cada letra na string
        if letra in vogais:         # se a letra for uma vogal
            contador +=  1
    return contador


print(contarVogais("Eu gosto de programar em Python!"))


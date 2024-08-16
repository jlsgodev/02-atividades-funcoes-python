#  10. **Função para Contar Caracteres**:
# - Crie uma função chamada `contarCaracteres` que receba uma string 
# e um caractere como argumentos e retorne o número de vezes que o caractere aparece na string.



def contarCaracteres(texto,  caractere): # função contarCaracteres com dois argumentos texto e caractere
    contador = 0                         # variável contador recebe 0

    for char in texto:                      # para cada char em texto
        if char == caractere:               # se char for igual a caractere   
            contador += 1                   # contador recebe contador + 1

    return contador

print(contarCaracteres("Bora codar", "a"))



    



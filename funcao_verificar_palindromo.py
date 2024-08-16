#  22. **Função para Verificar Palíndromo**:
#- Crie uma função chamada `ePalindromo` que receba uma string
# como argumento e retorne `true` se a string
# for um palíndromo e `false` caso contrário.


def ePalindromo(string):
    string = string.lower()             # converte a string para minúsculas
    string = string.replace(" ", "")    # remove os espaços da string
    return string == string [::-1]      # Usa List Slicing para inverter a string e compara com a string original

print(ePalindromo("anotaram a data da maratona"))


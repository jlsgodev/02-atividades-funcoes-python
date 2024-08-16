#  9. **Função para Inverter String**:
# - Crie uma função chamada `inverterString` 
# que receba uma string como argumento e retorne a string invertida.

def inverterString(string):
    stringInvertida = ""                    # variável stringInvertida recebe uma string vazia

    for i in range(len(string) -1, -1, -1):     # para i no intervalo do tamanho da string -1 até -1  com passo -1
        stringInvertida += string[i]            # stringInvertida recebe stringInvertida mais string[i]

    return stringInvertida                      

print(inverterString("python é massa!"))            # printa a função inverterString 


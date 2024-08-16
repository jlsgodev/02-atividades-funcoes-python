# 28. **Função para Verificar Substring**:
# - Crie uma função chamada `contemSubstring`
#  que receba duas strings como argumentos e 
# retorne `true` se a primeira string contiver
#  a segunda string, e `false` caso contrário.

def contemSubstring (string1, string2): # função para verificar se a primeira string contém a segunda string
    if string2 in string1: # se a segunda string estiver contida na primeira string
        return True
    else:
        return False
    
print(contemSubstring("bora codar", "codar")) 
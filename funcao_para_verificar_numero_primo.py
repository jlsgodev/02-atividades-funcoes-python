# 7. **Função para Verificar Número Primo**:
# - Crie uma função chamada `ePrimo` que receba um número como 
# argumento e retorne `true` se o número for primo e `false` caso contrário.


def ePrimo(numero):                   # Função para verificar se um número é primo
    if numero <= 1:                     # Se o número for menor ou igual a 1, não é primo
        return False                    
    if numero == 2:                     # Se o número for igual a 2, é primo
        return True
    if numero % 2 == 0:                 # Se o número for par, não é primo, pois o único número primo par é o 2 
     return False                       
    
    for i in range(3 , int(numero ** 0.5 ) + 1,  2):   # for para verificar se o número é primo. Se o número for divisível por algum número entre 3 e a raiz quadrada do número, não é primo
     if numero % i == 0:                                    # Se o número for divisível por i, não é primo = False
       return False
    return True

print(ePrimo(91))                                   # Teste da função
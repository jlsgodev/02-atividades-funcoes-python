# 12. **Função de Ordem Superior**:
# - Crie uma função chamada `operacao` que receba dois números e uma função como argumentos.
#  A função deve aplicar a função fornecida aos dois números e retornar o resultado.


def operacao(num1 , num2, funcao):             # função operacao com três argumentos num1, num2 e funcao

    return funcao(num1, num2)                   # retorna a função com os argumentos num1 e num2

def dividir(num1, num2):                        # função dividir com dois argumentos num1 e num2
    return num1 / num2

def multiplicar(num1 , num2):                   # função multiplicar com dois argumentos num1 e num2
    return num1 * num2

print(operacao(50, 5, dividir ))                
print(operacao(50, 15, multiplicar))


# 18. **Função para Verificar Paridade**:
#- Crie uma função chamada `ePar` que receba um número
# como argumento e retorne `true` se o número for par e `false` caso contrário.


def ePar(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(ePar(91))
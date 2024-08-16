#   14. **Função Recursiva**:
# - Crie uma função chamada `contagemRegressiva` que receba
#  um número como argumento e exiba uma contagem regressiva
#  a partir desse número até 0, usando recursão.


def contagemRegressiva(num):
    if num <= 0:            # se num for menor ou igual a 0
        print("0")          # imprime 0
    else:
        print(num)
        contagemRegressiva(num - 1)         # chama a função contagemRegressiva com num - 1

contagemRegressiva(19)


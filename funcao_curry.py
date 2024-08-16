# 29. **Função de Curry**:
# - Crie uma função chamada `currySoma`
#  que usa currying para somar três números.
#  A função deve ser chamada assim: `currySoma(a)(b)(c)`.

def currySoma(a):   # Função de curry para somar três números
    return lambda b: lambda c: a + b + c       # retorna função lambda que recebe b e retorna outra função lambda que recebe c e retorna a + b + c

print(currySoma(3)(2)(1))  
#   32. **Função de Composição**:
# - Crie uma função chamada `compor`
#  que receba duas funções como argumentos
#  e retorne uma nova função que é a composição das duas.

def compor(funcao1, funcao2): # função de composição
    def nova_funcao(*args, **kwargs): # nova função que recebe argumentos e palavras-chave
        return funcao1(funcao2(*args, **kwargs)) # retorna a composição das duas funções
    return nova_funcao 

def quadrado(x): # função que retorna o quadrado de um número
    return x * x

print(compor(quadrado, quadrado)(2)) 
#13. **Função de Retorno**:
#- Crie uma função chamada `criarSaudacao` que receba uma saudação 
# como argumento e retorne uma nova função. A função retornada deve 
# receber um nome como argumento e exibir a saudação seguida pelo nome.

def criarSaudacao(saudacao):  # função criarSaudacao com um argumento saudacao
    def saudar(nome):         # função saudar com um argumento nome
        print(saudacao, nome)
    return saudar             # retorna saudar

ola = criarSaudacao('Olá')    # ola recebe criarSaudacao com o argumento 'Olá'
ola('jhon')







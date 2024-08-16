#  27. **Função de Memoização para Fatorial**:
#- Crie uma função chamada `memoFatorial` que usa
#  memoização para otimizar o cálculo do fatorial.

def memoFatorial (n, memo = {}):   # Função de memoização para fatorial
    if n == 0: return 1             # Se n for igual a 0, retorna 1
    if n in memo: return memo[n]        # Se n estiver no dicionário memo, retorna memo[n]
    memo[n] = n * memoFatorial(n - 1, memo)     # memo[n] recebe n multiplicado pelo resultado da chamada recursiva de memoFatorial(n - 1, memo)
    return memo[n]

print(memoFatorial(3)) 
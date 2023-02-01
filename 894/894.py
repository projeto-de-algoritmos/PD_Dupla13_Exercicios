# Definição de nó do próprio leetcode
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    # Não existe árvore com 0 nós e a com 1 nó é simplemente ele mesmo
    solucoes = {0: [], 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in Solution.solucoes:
            resultados = []
            
            # Loop de 0 a n-1
            for x in range(n):
                # o y decai de n-1 até 0
                y = n - 1 - x
                
                # Chama a função utilizando o x, ou seja, a esquerda do nó
                for left in self.allPossibleFBT(x):
                    # Chama a função utilizando o y, ou seja, a direita do nó
                    for right in self.allPossibleFBT(y):
                        # Cria um nó de vlaor 0 para o indice atual
                        node = TreeNode(0)
                        # Define o left e o right do nó como o left e o right atual
                        node.left = left
                        node.right = right
                        # Adiciona este resultado à lista de resultados
                        resultados.append(node)
                # Atribui o resultado no dicionário de solucoes
                Solution.solucoes[n] = resultados
        
        return Solution.solucoes[n]
from collections import defaultdict


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        # Verifica se todas as posições do grid são iguais a 0;
        # Se for o caso, retorna 0, pois existem 0 cerejas a serem pegas.
        self.grid = grid
        soma = 0
        for linha in grid:
            soma += sum(linha)
        if soma == 0:
            return 0
        
        # Cria um dicionário com as soluções para o problema
        self.solucoes = defaultdict(int)
        # Parâmetros: a linha em que os robôs estao, a coluna do R1, a coluna do R2
        return self.rec(0, 0, len(grid[0])-1) 

    
    def rec(self, l, c1, c2):
        # Se é a última linha, os robôs alcançaram o final do greed. 
        if l == len(self.grid): 
            return 0
        
        # Se os robôs estão no mesmo quadrado, essa é uma posição inválida
        if c1 == c2: 
            return float('-inf')

        # Se o R1 e o R2 estão em uma posição válida dentro do greed 
        if 0 <= c1 < len(self.grid[0]) and 0 <= c2 < len(self.grid[0]):
            maxCerejas = 0
            # Possíveis movimentos do R1 (Ir pra esquerda, frente ou direita)
            for y1 in [c1-1, c1, c1+1]:
                # Possíveis movimentos do R2 (Ir pra esquerda, frente ou direita)
                for y2 in [c2-1, c2, c2+1]:
                    # Se esses movimentos já foram analisados para a próxima linha,
                    # O número de cerejas é o que já foi calculado
                    if self.solucoes.get((l+1, y1, y2)): 
                        cerejas = self.solucoes[(l+1, y1, y2)]
                    # Se a análise ainda não foi feita a função é chamada de novo com
                    # a próxima linha, a possivel coluna do R1 e a possivel coluna do R2
                    else: 
                        cerejas = self.rec(l+1, y1, y2)
                    # Verifica se o números de cerejas não é -inf
                    maxCerejas = max(maxCerejas, cerejas)

            # Adiciona o número de cerejas encontradas para a próxima linha com a da linha
            # atual e armazena no dicionário.         
            self.solucoes[(l, c1, c2)] = self.grid[l][c1] + self.grid[l][c2] + maxCerejas
            # Retorna o total de cerejas encontrados na interação 
            return self.grid[l][c1] + self.grid[l][c2] + maxCerejas
        
        return float('-inf')
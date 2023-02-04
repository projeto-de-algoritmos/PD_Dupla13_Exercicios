class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Dicionário para o armazenamento dos valores já analisados
        solucoes = {}

        def rec(amount):
            # Se o valor a ser alcançado já foi analisado, a 
            # resposta já está contida no dicionário de soluções
            if amount in solucoes:
                return solucoes[amount]
            
            # Se o valor a ser alcançado é 0, a resposta é 0 pois
            # serão utilizadas 0 moedas
            if amount == 0:
                return 0

            moedasUtilizadas = []
            # Analisa cada uma das possiveis moedas
            for coin in coins:
                # Se a moeda não ultrapassar o valor a ser alcançado,
                # armazena-se o número de moedas necessárias para o 
                # valor menos o valor da moeda atual
                if amount - coin >= 0:
                    moedasUtilizadas.append(rec(amount - coin))
                # Se não for esse o caso, adiciona o valor de inf, pois 
                # essa moeda não poderá ser utilizada 
                else:
                    moedasUtilizadas.append(float('inf'))

            # Adiciona-se 1 ao menor número encontrado para cobrir o valor,
            # correspondendo a moeda que foi utilizada para "zerar" o montante 
            menorQuantidade = min(moedasUtilizadas) + 1
            # Adiciona ao dicionário de soluções o número de moedas necessárias 
            # para o valor atual
            solucoes[amount] = menorQuantidade
            # Retorna o menor número de moedas para suprir o valor atual
            return menorQuantidade

        resultado = rec(amount)

        # Se o resultado não for infinito, foi encontrada uma solução    
        if resultado != float('inf'):
            return resultado
        # Se não foi encontrada uma solução, retorna -1
        return -1
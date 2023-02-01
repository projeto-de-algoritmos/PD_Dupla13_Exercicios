# Classe utilizada para contar a ocorrência de um valor em uma lista
from collections import Counter as cnt

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def analiseRecursiva(ocorrenciaLetras, idx):
            # Caso o dicionário com a ocrrencia das letras esteja vazio, retorna False pois não existem mais
            # letras para serem usadas;

            # Caso idx não seja menor que o tamanho da lista de palavras, retorna 0 pois já foram analisadas
            # todas as palavras;

            # Não sendo este o caso, retorna a soma dos scores
            return (
                ocorrenciaLetras
                # Verifica se todas as palavras já foram analisadas
                and idx < len(words)
                and max(
                    # Realiza a análise para a próxima palavra sem remover as letras da palavra atual
                    # Ou seja, verifica se a próxima palavra possuí maior score que o score obtido até então
                    analiseRecursiva(ocorrenciaLetras, idx + 1),
                    # Realiza a contagem das letras na palavra que está sendo analisada e subtrai 
                    # a ocorrencia das letras na lista de letras disponíveis. Se o resultado não for uma lista vazia,
                    # significa que a palavra possui letras que não estão disponíveis na lista de ocorrências. 
                    # Neste caso a operação not {lista não vazia} e and (valor retornado na próxima operacao), vai retornar
                    # False, resultando em score 0.
                    not cnt(words[idx]) - ocorrenciaLetras
                    # Utiliza a função ord para obter o unicode das letras da palavra analisada, subtraindo
                    # o unicode de 'a', obtendo a posição da letra na lista de scores; Realiza a soma dos scores;
                    and sum(score[ord(c) - ord("a")] for c in words[idx])
                    # Soma o score obtido na palavra atual com o retorno da próxima análise, utilizando
                    # a ocorrencia das letras subtraída das letras que foram usadas nesta palavra 
                    + analiseRecursiva(ocorrenciaLetras - cnt(words[idx]), idx + 1),
                )
            )
        # Inicia a recursão usando a ocorrência de cada letra na lista de letras
        return int(analiseRecursiva(cnt(letters), 0))
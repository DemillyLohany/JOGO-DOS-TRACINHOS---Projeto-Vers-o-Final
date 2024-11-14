# ranking.py

def guardar_ranking(nome: str, pontuacao: str) -> None:
    '''Essa função é responsável por criar um arquivo 'ranking_jogo.txt',
    ele guarda a pontuacão e o nome do jogador e do computador a cada rodada.
    Dito isso, a criação desse arquivo tem como principal objetivo,
    arquivar a pontuação de todos os jogadores e do computador em cada rodada'''
    open('ranking_jogo.txt', 'a').close()

    # Daqui pra baixo vai ficar dentro do laço
    # Lê do arquivo
    while True:
        arq = open('ranking_jogo.txt')
        conteúdo = arq.readlines()
        arq.close()
        ranking = []
        nome_pontuacao = [pontuacao, nome]
        ranking.append(nome_pontuacao)

        # Exibe a lista ordenada
        ranking.sort()
        
        arq = open('ranking_jogo.txt', 'a', encoding='utf-8')
        arq.write(nome + '\n')
        arq.write(pontuacao  + '\n')
        arq.close()
        break

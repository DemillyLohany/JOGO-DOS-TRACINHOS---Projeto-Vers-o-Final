
import colorama

def mostrar_tabuleiro(tabuleiro: list[list[str]]) -> None:
    '''Esta fução recebe a matriz "tabuleiro" e é responsável
    por exibir o tabuleiro formatado e seu conteúdo  ao jogador'''
    for linha in tabuleiro:
        print(''.join(linha))
    print()
    print('-' * 40)

def repetir_traços() -> None:
    '''Essa função é responsável por criar traços que auxiliam, visualmente ao jogador,
    a separar uma jogada válida do jogador da do computador'''
    for traços in range(0,2):
        print('-' * 40)
        # traços = '-' * 40
        # traços_centralizados = centralizar_texto(traços)
        # print(traços_centralizados)

def exibir_jogada_inválida(cor_vermelha: str) -> None:
    '''Essa função fica responsável por exibir uma mensagem quando a jogada é inválida,
    e também formatar e colorir essa mensagem'''
    print()
    print(cor_vermelha + 'Jogada inválida, tente novamente.')
    print()
    print(colorama.Style.RESET_ALL + '-' * 40)
    print()

def imprimir_jogadas_computador(COR_AZUL, COMPUTADOR, linha1_computador, coluna1_computador, linha2_computador, coluna2_computador):
    print()
    print(COR_AZUL + f'Agora é a vez do computador: {COMPUTADOR}' + colorama.Style.RESET_ALL)
    print()
    print('Posições escolhidas pelo computador:')
    print(f'Linha do primeiro ponto: {linha1_computador}')
    print(f'Coluna do primeiro ponto: {coluna1_computador}')
    print(f'Linha do segundo ponto: {linha2_computador}')
    print(f'Coluna do segundo ponto: {coluna2_computador}')

def pedir_jogada() -> list:
    valido = False
    jogada = []
    while not valido:
        cont = 0  # Quantidade de números digitados
        entrada = input('Digite a posição de início e de fim (ex.: 11 12):')
        for c in entrada:
            if c.isnumeric():
                cont += 1
        if cont < 4:
            print(f'Faltou digitar {4-cont} números.')
            continue
        elif cont > 4:
            print(f'Digite apenas 4 números.')
            continue
        else:
            valido = True
        
        for c in entrada:
            if c.isnumeric():
                jogada.append(int(c))
    return jogada

def instrucoes_do_jogo() -> None:
    print('Instruções do Jogo: \n \n 1. Funcionamento:\n - Os jogadores(usuário e o computador) se revezam para jogar.')
    print('2. Objetivo: \n - O objetivo é formar linhas  tracejadas entre os pontos, que são representados por sua linha e coluna. O jogador que completar mais quadrados(linhas fechadas) vence.')
    print('3. Como Jogar: \n - Em cada turno, um jogador deve desenhar uma linha entre dois pontos adjacentes (horizontal ou vertical). \n - Não é permitido desenhar linhas diagonais.')
    print('4. Fechando Quadrados: \n - Se um jogador(usuário) fechar um quadrado ao desenhar uma linha, ele coloca sua marca(primeira letra do seu nome, \n assim como uma cor de background já estabelecida) dentro do quadrado.')
    print('5. Fim do Jogo: \n - O jogo termina quando todas as linhas possíveis forem desenhadas. \n - O jogador com mais quadrados fechados vence.')
    print('Dicas: \n - Pense estrategicamente para bloquear seu oponente de fechar quadrados. \n - Tente criar oportunidades para você mesmo fechar mais quadrados.')
    print('Divirta-se jogando!')
    print()


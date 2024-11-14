# jogo.py
import colorama, random, time
from auxiliares import mudar, mudar_posicao_aparente, centralizar_texto
from interface import repetir_traços, mostrar_tabuleiro, exibir_jogada_inválida, pedir_jogada, imprimir_jogadas_computador, instrucoes_do_jogo
from ranking import guardar_ranking

FUNDO_VERDE = colorama.Back.GREEN
FUNDO_PRETO = colorama.Fore.GREEN
COR_VERDE = colorama.Fore.GREEN
COR_VERMELHA = colorama.Fore.RED
COR_AZUL = colorama.Fore.BLUE
COMPUTADOR = '🤖 '


def criar_tabuleiro() -> None:
        '''Retorna o tabuleiro do jogo'''
        tabuleiro = [
            ['1,1','   ','1,2','   ','1,3','   ','1,4','   ','1,5','   ','1,6','   ','1,7'],
            ['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   '],
            ['2,1','   ','2,2','   ','2,3','   ','2,4','   ','2,5','   ','2,6','   ','2,7'],
            ['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   '],
            ['3,1','   ','3,2','   ','3,3','   ','3,4','   ','3,5','   ','3,6','   ','3,7'],
            ['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   '],
            ['4,1','   ','4,2','   ','4,3','   ','4,4','   ','4,5','   ','4,6','   ','4,7'],
            ['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   '],
            ['5,1','   ','5,2','   ','5,3','   ','5,4','   ','5,5','   ','5,6','   ','5,7'],
            ['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   '],
            ['6,1','   ','6,2','   ','6,3','   ','6,4','   ','6,5','   ','6,6','   ','6,7'],
            ['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   '],
            ['7,1','   ','7,2','   ','7,3','   ','7,4','   ','7,5','   ','7,6','   ','7,7']
        ]
        return tabuleiro

def verificar_jogada(tabuleiro: list[list[str]], linha1: int, coluna1: int, linha2: int, coluna2: int, linha_1: int, linha_2: int, coluna_1: int, coluna_2: int) -> bool:
    '''Esta função verifica se a jogada do jogador ou do computador, é válida ou não.
    A jogada só é válida se as linhas dos pontos forem iguais ou se colunas deles forem iguais,
    Além disso, e a diferença das colunas ou das linhas deve ser igual a dois,
    consecutivamente, de acordo com cada caso.'''
    if linha1 == linha2 and abs(coluna1 - coluna2) == 2:
        maior_coluna = max(coluna1, coluna2)
        if tabuleiro[linha1][maior_coluna - 1] == '---':
            return True
        return tabuleiro[linha1][maior_coluna - 1] == '   '
    elif coluna1 == coluna2 and abs(linha1 - linha2) == 2:
        maior_linha = max(linha1, linha2)
        if tabuleiro[maior_linha - 1][coluna1] == ' ¦ ':
            return True
        return tabuleiro[maior_linha - 1][coluna1] == '   '
    elif linha_1 == '' or linha_2 == '' or coluna_1 == '' or coluna_2 == '':
        return False
    return False

def fazer_jogada(tabuleiro: list[list[str]], linha1: int, coluna1: int, linha2: int, coluna2: int) -> bool:
    '''Esta função verifica e faz a jogada que o jogador ou que o computador escolheu,
    verificando se as linhas são iguais e a diferença das colunas é igual a dois
    (colocando uma linha horizontal no espaço vazio) ou se as colunas são iguais e a diferença das linhas é 
    igual a dois (colocando uma linha vertical no espaço vazio). 
    Após verificar que a jogada é válida e não é repetida, 
    ela é efetuada no tabuleiro através dessa função('fazer_jogada').'''
    if linha1 == linha2 and abs(coluna1 - coluna2) == 2:
        maior_coluna = max(coluna1, coluna2)
        if tabuleiro[linha1][maior_coluna - 1] == '---':
            return False
        tabuleiro[linha1][maior_coluna - 1] = '---'
        return True
    elif coluna1 == coluna2 and abs(linha1 - linha2) == 2:
        maior_linha = max(linha1, linha2)
        if tabuleiro[maior_linha - 1][coluna1] == ' ¦ ':
            return False
        tabuleiro[maior_linha - 1][coluna1] = ' ¦ '
        return True
    return False

def verificar_quadradinhos(tabuleiro: list[list[str]], símbolo: str, contador_jogadas_válidas: int, computador: str, letra_jogador: str) -> None:
    '''Esta função verifica se já há quadradinho(os) formado(os) no tabuleiro, adicionando o símbolo, no meio dele(s),
    do respónsavel pelo último tracinho que o(os) completou/completaram.
    Se quem formou o quadradinho foi o computador, será adicionado um emoji de robô no meio do quadrado azul,
    e se foi o jogador, será atribuida a primeira letra do nome dele no quadradinho com cor verde.'''
    for linha in range(-1, len(tabuleiro)-1):
        for coluna in range(len(tabuleiro)):
            if tabuleiro[linha][coluna] == '   ' and tabuleiro[linha][coluna] != símbolo:
                if tabuleiro[linha+1][coluna] == '---' and tabuleiro[linha-1][coluna] == '---':
                    if tabuleiro[linha][coluna+1] == ' ¦ ' and tabuleiro[linha][coluna-1] == ' ¦ ':
                        if contador_jogadas_válidas % 2 == 1:
                            símbolo = letra_jogador
                            tabuleiro[linha][coluna] = símbolo
                            cor_quadradinho = colorama.Back.GREEN
                        else:
                            símbolo = computador
                            tabuleiro[linha][coluna] = símbolo
                            cor_quadradinho = colorama.Back.BLUE
                        tabuleiro[linha][coluna] = cor_quadradinho + símbolo + colorama.Style.RESET_ALL 

def listar_posições_válidas(tabuleiro: list[list[str]], posições_válidas: list[int]) -> None:
    '''Nessa função todas as posições que o usuário pode definir nas linhas e
    colunas são armazenadas na lista 'posições_válidas'.'''
    linhas = len(tabuleiro)
    total_linhas = int((linhas - ((linhas -1 ) / 2)))
    for posição in range(1, total_linhas+1):
        posições_válidas.append(str(posição))

def continuar_jogo(tabuleiro: list[list[str]]) -> bool:
    '''A função 'continuar_jogo' é encarregada de retornar um valor booleano(True)
    caso o tabuleiro ainda não esteja totalmente preenchido, 
    garantindo a continuidade das jogadas até o término do jogo. '''
    ha_espaço = False
    for linha in tabuleiro:
        for elemento in linha:
            if elemento == '   ':
                ha_espaço = True
                return ha_espaço == True


def ensinar_computador(tabuleiro: list[list[str]],contador_jogadas_válidas: int,posições_válidas, letra_jogador: str):
    for linha in range (0,len(tabuleiro)):
        for coluna in range (0,len(tabuleiro)-1):
            símbolo = COMPUTADOR
            if tabuleiro[linha][coluna] == '---' and tabuleiro[linha-2][coluna] == '---' and tabuleiro[linha-1][coluna-1] == ' ¦ ' and tabuleiro[linha-1][coluna+1] == '   ':
                tabuleiro[linha-1][coluna+1] = ' ¦ '
                linha1_computador = mudar_posicao_aparente(linha-2)
                coluna1_computador = mudar_posicao_aparente(coluna+1)
                linha2_computador = mudar_posicao_aparente(linha)
                coluna2_computador = mudar_posicao_aparente(coluna+1)
                print('-' * 40)
                imprimir_jogadas_computador(COR_AZUL, COMPUTADOR, linha1_computador, coluna1_computador, linha2_computador, coluna2_computador)
                verificar_quadradinhos(tabuleiro, símbolo, contador_jogadas_válidas, COMPUTADOR, letra_jogador)
                return
            if tabuleiro[linha][coluna] == '---' and tabuleiro[linha-2][coluna] == '---' and tabuleiro[linha-1][coluna+1] == ' ¦ ' and tabuleiro[linha-1][coluna-1] == '   ':
                tabuleiro[linha-1][coluna-1] = ' ¦ '
                linha1_computador = mudar_posicao_aparente(linha-2)
                coluna1_computador = mudar_posicao_aparente(coluna-1)
                linha2_computador = mudar_posicao_aparente(linha)
                coluna2_computador = mudar_posicao_aparente(coluna-1)
                print('-' * 40)
                imprimir_jogadas_computador(COR_AZUL, COMPUTADOR, linha1_computador, coluna1_computador, linha2_computador, coluna2_computador)
                verificar_quadradinhos(tabuleiro, símbolo, contador_jogadas_válidas, COMPUTADOR, letra_jogador)
                return
            if tabuleiro[linha][coluna] == ' ¦ ' and tabuleiro[linha][coluna+2] == ' ¦ ' and tabuleiro[linha+1][coluna+1] == '---' and tabuleiro[linha-1][coluna+1] == '   ':
                tabuleiro[linha-1][coluna+1] = '---'
                linha1_computador = mudar_posicao_aparente(linha-1)
                coluna1_computador = mudar_posicao_aparente(coluna)
                linha2_computador = mudar_posicao_aparente(linha-1)
                coluna2_computador = mudar_posicao_aparente(coluna+2)
                print('-' * 40)
                imprimir_jogadas_computador(COR_AZUL, COMPUTADOR, linha1_computador, coluna1_computador, linha2_computador, coluna2_computador)
                verificar_quadradinhos(tabuleiro, símbolo, contador_jogadas_válidas, COMPUTADOR, letra_jogador)
                return
            if tabuleiro[linha][coluna] == ' ¦ ' and tabuleiro[linha][coluna+2] == ' ¦ ' and tabuleiro[linha-1][coluna+1] == '---' and tabuleiro[linha+1][coluna+1] == '   ':
                tabuleiro[linha+1][coluna+1] = '---'
                linha1_computador = mudar_posicao_aparente(linha+1)
                coluna1_computador = mudar_posicao_aparente(coluna)
                linha2_computador = mudar_posicao_aparente(linha+1)
                coluna2_computador = mudar_posicao_aparente(coluna+2)
                print('-' * 40)
                imprimir_jogadas_computador(COR_AZUL, COMPUTADOR, linha1_computador, coluna1_computador, linha2_computador, coluna2_computador)
                verificar_quadradinhos(tabuleiro, símbolo, contador_jogadas_válidas, COMPUTADOR, letra_jogador)
                return
            
    # Nas três linhas seguintes são atribuidos a lista 'posições_válidas_int'
    # os valores da lista 'posições_válidas' como inteiros
    posições_válidas_int = []
    for posição in posições_válidas:
        posições_válidas_int.append(int(posição))
    while True:
        l1_computador = random.choice(posições_válidas_int)
        linha1_computador = mudar(l1_computador)
        c1_computador = random.choice(posições_válidas_int)
        coluna1_computador = mudar(c1_computador)
        l2_computador = random.choice(posições_válidas_int)
        linha2_computador = mudar(l2_computador)
        c2_computador = random.choice(posições_válidas_int)
        coluna2_computador = mudar(c2_computador)

        if verificar_jogada(tabuleiro, linha1_computador, coluna1_computador, linha2_computador, coluna2_computador, l1_computador, l2_computador, c1_computador, c2_computador):
            # ensinar_computador_completar_quadradinho(tabuleiro, linha1_computador, coluna1_computador, linha2_computador, coluna2_computador)
            # if condição_válida_jogar:
            condição_posição_disponível = fazer_jogada(tabuleiro, linha1_computador, coluna1_computador, linha2_computador, coluna2_computador)
            if condição_posição_disponível:
                print('-' * 40)
                # jogar_computador(linha1_computador, coluna1_computador, linha2_computador, coluna2_computador)
                print()
                print(COR_AZUL + f'Agora é a vez do computador: {COMPUTADOR}' + colorama.Style.RESET_ALL)
                print()
                print('Posições escolhidas pelo computador:')
                print(f'Linha do primeiro ponto: {l1_computador}')
                print(f'Coluna do primeiro ponto: {c1_computador}')
                print(f'Linha do segundo ponto: {l2_computador}')
                print(f'Coluna do segundo ponto: {c2_computador}')

                verificar_quadradinhos(tabuleiro, símbolo, contador_jogadas_válidas, COMPUTADOR, letra_jogador)
                return

def principal():
    print()
    print(centralizar_texto(FUNDO_VERDE + colorama.Fore.BLACK + 'Início do Jogo dos Tracinhos - Bem-vindo!' + colorama.Style.RESET_ALL))
    print()

    instrucoes_do_jogo()
    # Aqui é registrado o nome do jogador e o símbolo usado para representar o computador.
    # jogador = input('Qual seu nome, jogador? ')
    nome_jogador = input(COR_VERDE + 'Qual seu nome, jogador? ' + colorama.Style.RESET_ALL )
    jogador = nome_jogador
    letra_jogador = jogador[0]
    letra_jogador = f' {letra_jogador} '

    # A lista a seguir 'posições_válidas' é responsável por guardar as posições que podem ser jogadas de forma válida
    posições_válidas = []

    # Abaixo está sendo representado a formatação do "tabuleiro" inicial do jogo

    tabuleiro = criar_tabuleiro()

    listar_posições_válidas(tabuleiro, posições_válidas)

    contador_jogadas_válidas = 0
    print()
    repetir_traços()
    print()
    print(COR_VERDE + '         Tabuleiro Inicial' + colorama.Style.RESET_ALL)
    print()
    mostrar_tabuleiro(tabuleiro)
    print()

    # É feito um loop infinito que só se encerra quando
    # o tabuleiro estiver completamente preenchido,
    # pedindo que o computador e o jogador escolham posições para suas jogadas,
    # até que todos os espaços vazios do tabuleiro estejam preenchidos
    while True:
        ha_espaço = continuar_jogo(tabuleiro)
        if ha_espaço:
            print(colorama.Style.RESET_ALL + FUNDO_PRETO + (f'Agora é a sua vez: {colorama.Style.RESET_ALL + nome_jogador}'))
            print()
            jogada = pedir_jogada()
            linha_1 = jogada[0]
            coluna_1 = jogada[1]
            linha_2 = jogada[2]
            coluna_2 = jogada[3]
            linha1, coluna1 = mudar(int(linha_1)), mudar(int(coluna_1))
            linha2, coluna2 = mudar(int(linha_2)), mudar(int(coluna_2))
            
            if verificar_jogada(tabuleiro, linha1, coluna1, linha2, coluna2, linha_1, linha_2, coluna_1, coluna_2) and fazer_jogada(tabuleiro, linha1, coluna1, linha2, coluna2):
                contador_jogadas_válidas += 1
                símbolo = letra_jogador
                verificar_quadradinhos(tabuleiro,  símbolo, contador_jogadas_válidas, COMPUTADOR, letra_jogador)
            elif verificar_jogada(tabuleiro, linha1, coluna1, linha2, coluna2,  linha_1, linha_2, coluna_1, coluna_2) and not fazer_jogada(tabuleiro, linha1, coluna1, linha2, coluna2):
                if ha_espaço != True:
                    ha_espaço = False
                    continue
                else:
                    print()
                    print(COR_VERMELHA + 'Essa posição já está ocupada, tente novamente.')
                    print()
                    print(colorama.Style.RESET_ALL + '-' * 40)
                    print()
                    continue
            else:
                if ha_espaço != True:
                    ha_espaço = False
                    continue
                else:
                    exibir_jogada_inválida(COR_VERMELHA)
                    continue
            
            print()
            mostrar_tabuleiro(tabuleiro)

            time.sleep(0.75)
            contador_jogadas_válidas += 1
            ensinar_computador(tabuleiro,contador_jogadas_válidas,posições_válidas,letra_jogador)
            print()
            mostrar_tabuleiro(tabuleiro)
            print('-' * 40)
            print()
            

        else:
            break

    dados = {}
    qnt_robo = 0
    qnt_letras = 0

    # O laço de repetição abaixo e as condições a seguir são responsáveis por contar e conferir quem fez mais pontos,
    # anunciando o vencedor ou o empate.
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[0])):
            símbolo = letra_jogador
            cor_quadradinho = colorama.Back.GREEN
            quadradinho_letra_jogador = cor_quadradinho + letra_jogador + colorama.Style.RESET_ALL 
            if tabuleiro[linha][coluna] == quadradinho_letra_jogador:
                qnt_letras += 1
            cor_quadradinho = colorama.Back.BLUE
            quadradinho_computador =  cor_quadradinho + COMPUTADOR + colorama.Style.RESET_ALL
            if tabuleiro[linha][coluna] == quadradinho_computador:
                qnt_robo += 1
    if qnt_letras > qnt_robo:
        print(f'Meus parabéns, você ganhou!')
    elif qnt_robo > qnt_letras:
        print(f'O vencedor é o computador! Boa sorte na próxima, jogador.')
    else:
        print(f'O jogo empatou!')

    #São colocados elementos em um dicionário, informando os jogadores, os pontos e o vencedor.'''
    dados['jogador_1'] = jogador
    dados['pontos_jogador_1'] = qnt_letras
    dados['jogador_2'] = 'computador'
    dados['pontos_jogador_2'] = qnt_robo
    if qnt_letras > qnt_robo:
        dados['vencedor'] = jogador
    elif qnt_letras < qnt_robo:
        dados['vencedor'] = 'computador'
    else:
        dados['vencedor'] = 'nenhum'

    # É exibido o nome dos participantes e suas respectivas pontuações
    print('Participantes: ')
    for chave, valor in dados.items():
        pontos = qnt_robo
        if chave != 'vencedor':
            if chave == 'jogador_1':
                pontos = qnt_letras
                print(f'{valor} obteve {pontos} pontos ')
                pontuação = str(pontos)
                guardar_ranking(valor, pontuação)
            elif chave == 'jogador_2':
                print(f'{valor} obteve {pontos} pontos ')
                pontuação = str(pontos)
                guardar_ranking(valor, pontuação)
            # else:
            #     print(f'{chave}: obteve {valor} pontos ')
    print(f'O vencedor é: {dados['vencedor']}')

    print()
    print(centralizar_texto(FUNDO_VERDE + colorama.Fore.BLACK + 'Obrigado por jogar!' + colorama.Style.RESET_ALL))
    print()
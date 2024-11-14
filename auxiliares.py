import os

def mudar(n: int) -> int:
    '''Esta função é responsável por alterar as posições das linhas e colunas
    escolhidas pelo jogador pelas correspondentes no tabuleiro'''
    return (n - 1) * 2

def mudar_posicao_aparente(n: int) -> int:
    '''Esta função é responsável por alterar as posições das linhas e 
    colunas reais do tabuleiro pelas aparentes, visualmente'''
    return int((n - n/2) + 1)

def centralizar_texto(texto: str) -> str:
    '''Essa função centraliza o texto'''
    terminal_width = os.get_terminal_size().columns  # Obtém a largura do terminal
    return texto.center(terminal_width)  # Centraliza o texto em relação à largura do terminal
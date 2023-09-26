#!/usr/bin/python3
"""
Exibir temporizador que recebe o tempo via rede do SevMicrofone
"""

import tkinter as tk
import socket ## Rede
import threading ## Linhas funcionar com varios comandos
import math
import sys
import signal
import getopt
# import time  # apenas para DEBUG


servidor_ativo = True
tempo_acabando = False
limite_tempo = 30
# Formato da msg do SevMicrofone: CPPPTTTTNNNNDB (14 caracteres)
TAM_MSG_SEVMIC = 14
intervalo_piscar = 1000

def ajuda():
    print(f"Uso do comando:\n{sys.argv[0]}\n")
    print('Opções:')
    print('  -j: modo janela. Padrão: em tela cheia')
    print('  -t N: tamanho da fonte. Padrão: cálculo automático')
    print('  -m N: tamanho da moldura. Padrão: 20') # era 8
    print('  -p N: porta para o servidor. Padrão: 5000')

ajuda()

def pegar_opcoes_cmd():
    # valores padrão
    opcoes = {'tela_cheia': False, 'tam_fonte': 0, 'tam_moldura': 20,
               'porta': 2000}

    try:
        opcoes_longas = ['janela', 'tam_fonte=', 'tam_moldura=', 'porta=']
        opcoes_cmd, _args = getopt.getopt(sys.argv[1:], 'hjtm:p:', opcoes_longas)
    except getopt.GetoptError:
        ajuda()
        sys.exit(2)
    for opcao, arg in opcoes_cmd:
        if opcao in ('-h', '--help'):
            ajuda()
            sys.exit()
        elif opcao in ('-j', '--janela'):
            opcoes['tela_cheia'] = False
        elif opcao in ('-t', '--tam_fonte'):
            opcoes['tam_fonte'] = int(arg)
        elif opcao in ('-m', '--tam_moldura'):
            opcoes['tam_moldura'] = int(arg)
        elif opcao in ('-p', '--porta'):
            opcoes['porta'] = int(arg)

    return opcoes
def tratar_conexao(cli, endereco): #2
    global mostrador
    global servidor_ativo
    global limite_tempo
    global tempo_acabando
    print(f'tratar_conexao: Nova conexão de: {endereco}')
    conectado = True


opcoes = pegar_opcoes_cmd() # 3

TAM_BLOCO = 14
servidor_ativo = True
servidor = None

root = tk.Tk() # 4
root.title('Temporizador SevMicrofone')



def iniciar_servidor(): ### 1
    global servidor_ativo
    global servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(('', opcoes['porta'])) # ouvir em todas as interfaces
    servidor.listen()
    print(f"Servidor ouvindo em {opcoes['porta']}")
    while servidor_ativo:
        cli, endereco = servidor.accept()
        thread = threading.Thread(target=tratar_conexao, args=(cli, endereco))
        thread.start()


iniciar_servidor()
#!/usr/bin/python3
"""
Exibir temporizador que recebe o tempo via rede do SevMicrofone
"""

import tkinter as tk
import socket
import threading
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

def mostrar_info():
    global root
    print(f"larg tela: {root.winfo_screenwidth()}, alt tela: {root.winfo_screenheight()}")
    print(f"larg janela: {root.winfo_width()}, alt janela: {root.winfo_height()}")
    print(f"maxsize {root.maxsize()}")
    print(f"tam_fonte: {opcoes['tam_fonte']}")
    print(f"tela_cheia?: {opcoes['tela_cheia']}")

def seg2tempo(s):
    return f"{math.floor(s / 60):02}:{math.floor(s % 60):02}"

def tratar_conexao(cli, endereco):
    global mostrador
    global servidor_ativo
    global limite_tempo
    global tempo_acabando
    print(f'tratar_conexao: Nova conexão de: {endereco}')
    conectado = True
    while conectado and servidor_ativo:
        # print(f'tratar_conexao: esperando cliente {time.time()}...')  # DEBUG
        msg = cli.recv(TAM_BLOCO).decode()
        if not len(msg) == TAM_MSG_SEVMIC:
            print(f'tratar_conexao: msg nula ou pequena: {len(msg)}')
            break
        # Formato da msg: CPPPTTTTNNNNDB (só interessa o TTTT)
        seg = int(msg[4:8])
        tempo = seg2tempo(seg)
        tempo_acabando = (0 < int(seg) <= limite_tempo)
        mostrador.config(text=tempo)
        # print(f'Mostrador: {tempo} - Segundos: {seg}')  # DEBUG
        if seg == 0:
            break
    print(f'tratar_conexao: Fim da conexão de: {endereco}')
    # precisa? Re: para o caso de 1 conexão por minuto, para de piscar
    # tempo_acabando = False
    cli.close()

def iniciar_servidor():
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

def desligar_servidor(sig, frame):
    global servidor_ativo
    global servidor
    servidor_ativo = False
    servidor.shutdown(socket.SHUT_RDWR)
    servidor.close()
    print ("Servidor Desligado")
    # sys.exit()

def piscar_borda():
    """ Piscar a moldura se o tempo estive acabando. Executada periodicamente """
    global moldura
    global intervalo_piscar
    if not tempo_acabando:
        moldura['bg'] = 'black'
    else:
        cor = 'black' if moldura['bg'] == 'red' else 'red'
        moldura['bg'] = cor
    moldura.after(intervalo_piscar, piscar_borda)

#------------------------------------------------------------------------------

opcoes = pegar_opcoes_cmd()

TAM_BLOCO = 14
servidor_ativo = True
servidor = None

root = tk.Tk()
root.title('Temporizador SevMicrofone')

if opcoes['tela_cheia']:
    print("Em tela cheia")
    root.attributes('-fullscreen', True) # tela cheia, sem título da janela!

if opcoes['tam_fonte'] == 0:
    # calcular fonte baseado no tamanho da tela
    # 8.5 no enterprise # 3.2 no RPi
    opcoes['tam_fonte'] = int(root.winfo_screenwidth() / 3.2) if opcoes['tela_cheia'] else 150

moldura = tk.Frame(root, padx=opcoes['tam_moldura'], pady=opcoes['tam_moldura'], bg='black')
moldura.pack(expand=1, fill=tk.BOTH)
mostrador = tk.Label(moldura, font=('calibri', opcoes['tam_fonte'], 'bold'),
                     background='black', foreground='red', text="00:00")

mostrador.pack(expand=1, fill=tk.BOTH)
piscar_borda()
root.update()
mostrar_info()

servidor_thread = threading.Thread(target=iniciar_servidor)
servidor_thread.start()

signal.signal(signal.SIGINT, desligar_servidor)

tk.mainloop()

print("FIM")

desligar_servidor(False, False)

sys.exit()
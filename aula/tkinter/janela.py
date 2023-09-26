from tkinter import *

def pegar_cotacoes():
    texto = '''String com varias linhas:
    Texto em cascata
    Cotações'''
    print(texto)


    texto_cotacao["text"] = texto


janela = Tk()

janela.title("Teste de Janela")

texto_orietacao = Label(janela, text="===== Label comum!!! =====")
texto_orietacao.grid(column=0, row=0, padx=200, pady=30) # padx largura pady altura

texto_orietacao2 = Label(janela, text="===== Label2 comum!!! =====")
texto_orietacao2.grid(column=0, row=1)

botao = Button(janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes) ##Sem parentese() por que se não o comando e executado sem aperta o botão
botao.grid(column=0,row=2)

texto_cotacao = Label(janela, text=" ")
texto_cotacao.grid(column=0, row=3, padx=0, pady=20)

janela.mainloop()
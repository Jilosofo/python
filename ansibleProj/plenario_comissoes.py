class teste():
     print("testo")

class principal():
      #Separador
    my_sep = tb.Separator(janela, bootstyle="warning", orient="horizontal")
    my_sep.pack(fill="x", padx="1") # fill x  dividi toda a janela

    label2 = tb.Label(janela, text="-----", bootstyle="light") 
    label2.pack(pady=1)

    # default labelframe style Comissões
    frame1 = tb.Labelframe(janela, bootstyle="light" , text="Comissões")
    #frame1.pack(side=LEFT, fill=BOTH, expand=True)
    frame1.pack(pady=1, padx=1)
    frame1.place(x=9,y=73, width=200, height=600)

    texto_orietacao = Label(frame1, text="=======================")
    texto_orietacao.pack(pady=2)
    ## Button
    button1 = tb.Button(frame1,text="Plenário 1", bootstyle="sucess, outline", command=comissoes)
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 2", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 3", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 4", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 5", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 6", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 7", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 8", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 9", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 10", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 11", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 12", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 13", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 14", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 15", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 16", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")

    # info colored labelframe style
    #Labelframe(bootstyle="info")

    # default labelframe style
    frame2 = tb.Labelframe(janela, bootstyle="light" , text="Comissões")
    frame2.pack(side=LEFT, fill=BOTH, expand=True)
    frame2.place(x=320,y=303, width=230, height=100)

    texto_orietacao = Label(frame2, text="==================")
    texto_orietacao.pack(pady=2)
    button2 = tb.Button(frame2,text="Todas Comissões", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")




class comissoes():
        result = subprocess.run(["cat", "/home/rodrigo/Documentos/python/python/ansibleProj/sample.txt"], stderr=subprocess.PIPE, text=True)
        print(result.stderr)

        #Tela Principal
        janela = Tk()
        janela.geometry("500x400+500+200")

        tab_control = ttk.Notebook(janela)

        #Criar os tabs
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)

        #Tabs
        tab_control.add(tab1, text='Server')
        tab_control.add(tab2, text='Computer')


        #Estrutura das tabs

        def plenario1():
            subprocess.run("xterm -e ansible-playbook -i /home/rodrigo/Documentos/ansible/ansible-pautaeletronica-des/hosts-tes /home/rodrigo/Documentos/ansible/ansible-pautaeletronica-des/pauta-playbook.yml", shell=True)
            messagebox.showinfo('SSH Paco', 'SSH Paco successfully!')
        btn = Button(tab1, text="Plenário 1", command=plenario1, height=1, width=12)
        btn.grid(column=2, row=8, sticky='news')
        

        tab_control.pack(expand=1, fill='both') #Sem esse tab_control não exibe os tabs

      
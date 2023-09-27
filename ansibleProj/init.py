from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#janela = Tk()
janela = tb.Window(themename="superhero")

janela.title("Ansible!")
#janela.iconbitmap('images/codemy.ico')
janela.geometry('950x750')

label1 = tb.Label(janela, text="Gerenciador Ansible", font=("Helvetica", 28), bootstyle="light")
label1.pack(pady=10)

#Separador
my_sep = tb.Separator(janela, bootstyle="warning", orient="horizontal")
my_sep.pack(fill="x", padx="1") # fill x  dividi toda a janela

label2 = tb.Label(janela, text="Label 2", bootstyle="light")
label2.pack(pady=1)

# default labelframe style Plenário
frame1 = tb.Labelframe(janela, bootstyle="light" , text="Plenário")
#frame1.pack(side=LEFT, fill=BOTH, expand=True)
frame1.pack(pady=1, padx=1)
frame1.place(x=10,y=73, width=220, height=250)
texto_orietacao = Label(frame1, text="========Plenário========")
texto_orietacao.pack(pady=2)

texto_orietacao = Label(frame1, text="=======================")
texto_orietacao.pack(pady=2)
## Button
button1 = tb.Button(frame1,text="Quiosques", bootstyle="sucess, outline")
button1.pack(pady=2, fill="x")
button2 = tb.Button(frame1,text="Commons", bootstyle="sucess, outline")
button2.pack(pady=2, fill="x")
button3 = tb.Button(frame1,text="-------", bootstyle="sucess, outline")
button3.pack(pady=2, fill="x")
button4 = tb.Button(frame1,text="-------", bootstyle="sucess, outline")
button4.pack(pady=2, fill="x")

# default labelframe2 style Comissões
frame2 = tb.Labelframe(janela, bootstyle="light" , text="Comissões")
frame2.pack(pady=1, padx=1)
frame2.place(x=10,y=330, width=220, height=250)
texto_orietacao = Label(frame2, text="========Comissões========")
texto_orietacao.pack(pady=2)

texto_orietacao = Label(frame2, text="========================")
texto_orietacao.pack(pady=2)
## Button
button1 = tb.Button(frame2,text="Comissões", bootstyle="sucess, outline")
button1.pack(pady=2, fill="x")
button2 = tb.Button(frame2,text="Quiosques", bootstyle="sucess, outline")
button2.pack(pady=2, fill="x")
button3 = tb.Button(frame2,text="Lab", bootstyle="sucess, outline")
button3.pack(pady=2, fill="x")
button4 = tb.Button(frame2,text="-------", bootstyle="sucess, outline")
button4.pack(pady=2, fill="x")

# info colored labelframe style
#Labelframe(bootstyle="info")


janela.mainloop()
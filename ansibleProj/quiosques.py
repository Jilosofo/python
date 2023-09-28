from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#janela = Tk()
janela = tb.Window(themename="superhero")

janela.title("Ansible!")
#janela.iconbitmap('images/codemy.ico')
janela.geometry('750x750')

label1 = tb.Label(janela, text="Gerenciador Ansible", font=("Helvetica", 28), bootstyle="light")
label1.pack(pady=10)

#Separador
my_sep = tb.Separator(janela, bootstyle="warning", orient="horizontal")
my_sep.pack(fill="x", padx="1") # fill x  dividi toda a janela

label2 = tb.Label(janela, text="-----", bootstyle="light") 
label2.pack(pady=1)

# default labelframe style Comissões
frame1 = tb.Labelframe(janela, bootstyle="light" , text="Plenário")
#frame1.pack(side=LEFT, fill=BOTH, expand=True)
frame1.pack(pady=1, padx=1)
frame1.place(x=250,y=173, width=300, height=400)

texto_orietacao = Label(frame1, text="=======================")
texto_orietacao.pack(pady=2)
## Button
button1 = tb.Button(frame1,text="QC-335273", bootstyle="sucess, outline")
#button1.pack(pady=2)
button1.grid(column=1, row=1)

button2 = tb.Button(frame1,text="QC-335287", bootstyle="sucess, outline")
button2.pack(pady=2)
#button2.grid(column=2, row=1)

button3 = tb.Button(frame1,text="QC-335298", bootstyle="sucess, outline")
button3.pack(pady=2)
#button3.grid(column=3, row=1)

# info colored labelframe style
#Labelframe(bootstyle="info")

# default labelframe style

##10.245.128.90
janela.mainloop()
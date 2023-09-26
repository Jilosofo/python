from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#janela = Tk()
janela = tb.Window(themename="superhero")

janela.title("TTK Bootstrap!")
#janela.iconbitmap('images/codemy.ico')
janela.geometry('500x350')

# Label
texto1 = tb.Label(janela,text="Click no checkbox",font=("Helvetica", 28), 
    bootstyle="light, inverse")
texto1.pack(pady=(40,10))
# Funções
def checker():
    if var1.get() == 1:
        texto1.config(text="Check Selecionado!!!")
    else:
        texto1.config(text="Check não está selecionado!!!")
def checker2():
    if var2.get() == 1:
        texto1.config(text="Check Selecionado!!!")
    else:
        texto1.config(text="Check não está selecionado!!!")
def checker3():
    if var3.get() == 1:
        texto1.config(text="Check Selecionado!!!")
    else:
        texto1.config(text="Check não está selecionado!!!")
def checker4():
    if var4.get() == 1:
        texto1.config(text="Check Selecionado!!!")
    else:
        texto1.config(text="Check não está selecionado!!!")
def checker5():
    if var5.get() == 1:
        texto1.config(text="Check Selecionado!!!")
    else:
        texto1.config(text="Check não está selecionado!!!")
def verificar():
    valor = var4.get()
    print(valor)
# CheckButton
var1 = IntVar()
check1 = tb.Checkbutton(bootstyle="danger", text="Check Me Out!",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)
check1.pack(pady=10)
# ToolButton
var2 = IntVar()
check2 = tb.Checkbutton(bootstyle="danger, toolbutton",
    text="Tool button!!!",
    variable=var2,
    onvalue=1,
    offvalue=0,
    command=checker2)
check2.pack(pady=10)
#Outlines Toolbutton
var3 = IntVar()
check3 = tb.Checkbutton(bootstyle="danger, toolbutton, outline",
    text="Outline Tool button!!!",
    variable=var3,
    onvalue=1,
    offvalue=0,
    command=checker3)
check3.pack(pady=10)
# Round Toggle Button
var4 = IntVar()
check4 = tb.Checkbutton(bootstyle="success, round-toggle",
    text="Round Tougle!!!",
    variable=var4,
    onvalue=1,
    offvalue=0,
    command=checker4)
check4.pack(pady=10)
var5 = IntVar()
check5 = tb.Checkbutton(bootstyle="warning, square-toggle",
    text="Square Tougle!!!",
    variable=var5,
    onvalue=1,
    offvalue=0,
    command=checker5)
check5.pack(pady=10)
janela.mainloop() ## Final da instrução

### 63761 Gsttenyo
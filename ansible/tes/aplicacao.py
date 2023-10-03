#1 importa os modulos
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#2 Criar objetos, titulo e janela size

janela = Tk()
janela.title("Ansible!")
#
window_height = 700
window_width = 900

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
#janela.iconbitmap('images/codemy.ico')
janela.iconbitmap(r'')
janela.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#4 variavel global
fonte1 = ('Times new roman', 14)
amtvar = IntVar()
dopvar = StringVar()


#5 frame widgets
f2 = Frame(janela)
f2.pack() 

f1 = Frame(
    janela,
    padx=10,
    pady=10,
)
f1.pack(expand=True, fill=BOTH)


# #6 Label Widget Só pra texto
Label(f1, text='ITEM NAME', font=fonte1).grid(row=0, column=0, sticky=W)
Label(f1, text='ITEM PRICE', font=fonte1).grid(row=1, column=0, sticky=W)
Label(f1, text='PURCHASE DATE', font=fonte1).grid(row=2, column=0, sticky=W)

# #7 Entry Widgets 
item_name = Entry(f1, font=fonte1)
item_amt = Entry(f1, font=fonte1, textvariable=amtvar)
transaction_date = Entry(f1, font=fonte1, textvariable=dopvar)

#8 Entry grid placement
item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))


#9 Action buttons
cur_date = Button(
    f1, 
    text='Current Date', 
    font=fonte1, 
    bg='#04C4D9', 
    command=None,
    width=15
    )

submit_btn = Button(
    f1, 
    text='Save Record', 
    font=fonte1, 
    command=None, 
    bg='#42602D', 
    fg='white'
    )


clr_btn = Button(
    f1, 
    text='Clear Entry', 
    font=fonte1, 
    command=None, 
    bg='#D9B036', 
    fg='white'
    )

quit_btn = Button(
    f1, 
    text='Exit', 
    font=fonte1, 
    command=None, 
    bg='#D33532', 
    fg='white'
    )

total_bal = Button(
    f1,
    text='Total Balance',
    font=fonte1,
    command=None
)

total_bal = Button(
    f1,
    text='Total Balance',
    font=fonte1,
    bg='#486966',
    fg='white',
    command=None
)

total_spent = Button(
    f1,
    text='Total Spent',
    font=fonte1,
    fg='white',
    command=None
)

update_btn = Button(
    f1, 
    text='Update',
    bg='#C2BB00',
    command=None,
    fg='white',
    font=fonte1
)

del_btn = Button(
    f1, 
    text='Delete',
    bg='#BD2A2E',
    fg='white',
    command=None,
    font=fonte1
)

#10 Button grid placement
cur_date.grid(row=3, column=1, sticky=EW, padx=(10, 0))
submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
quit_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))
total_bal.grid(row=0, column=3, sticky=EW, padx=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0))

#11 treeview to view the record
tv = ttk.Treeview(f2, selectmode='browse', columns=(1, 2, 3, 4), show='headings', height=8, )
tv.pack(side="left")


janela.mainloop()
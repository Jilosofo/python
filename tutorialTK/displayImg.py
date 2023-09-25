import tkinter as tk
from tkinter import ttk

# create the root window
root = tk.Tk()
root.geometry('500x400')
root.resizable(False, False)
root.title('Label Widget Image')

# display an image label
photo = tk.PhotoImage(file='/home/rodrigo/Imagens/clusterkubernates.png')
image_label = ttk.Label(
    root,
    image=photo,
    text='Kubernates',
    #padding=5
    compound='top'
)
image_label.pack()

root.mainloop()
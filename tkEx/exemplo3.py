from tkinter import *
import customtkinter

#https://github.com/TomSchimansky/CustomTkinter
#Here is the link to their official documentation:
#https://github.com/TomSchimansky/CustomTkinter/wiki



# Create CTK window like you do with the Tk window
root = customtkinter.CTk()

# Setting window width and Height
root.geometry("300x400")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root, text="Hello World!")

# Showing at the center of the screen
button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Running the app
root.mainloop()
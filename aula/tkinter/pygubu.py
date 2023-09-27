#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        frame2 = ttk.Frame(master)
        frame2.configure(height=200, width=200)
        panedwindow1 = ttk.Panedwindow(frame2, orient="horizontal")
        panedwindow1.configure(height=200, width=200)
        panedwindow1.pack(side="top")
        frame2.pack(side="top")

        # Main widget
        self.mainwindow = frame2

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = NewprojectApp(root)
    root.geometry('500x350')
    app.run()

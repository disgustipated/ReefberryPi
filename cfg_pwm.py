import tkinter as tk
from tkinter import *
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)


class PagePWM(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Pulse Width Modulation Configuration", font=LARGE_FONT)
        label.pack(side=TOP, pady=10, anchor=W)

        label2 = tk.Label(self, text="Coming Soon...", font=LARGE_FONT)
        label2.pack(side=TOP, pady=50)

        

